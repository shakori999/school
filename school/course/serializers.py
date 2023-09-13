from rest_framework import serializers

from .models import Course, CoursesPerCycle


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_code(self, value):
        # Add your custom validation logic here
        if not value.startswith('COURSE'):
            raise serializers.ValidationError("Course code must start with 'COURSE'")
        return value

    def validate_dates(self, data):
        # Validate that start_date is earlier than end_date
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError("Start date must be earlier than end date")
        
        return data

    def get_full_description(self, obj):
        return f"{obj.name}: {obj.description}\nBibliography: {obj.bibliography}"


class CoursesPerCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesPerCycle
        fields = '__all__'

    def validate_date_range(self, data):
        """
        Custom validation to ensure that the course date range falls within the cycle date range.
        """
        coursestartdate = data.get('coursestartdate')
        courseenddate = data.get('courseenddate')
        cycle = data.get('cycle')

        if coursestartdate < cycle.cyclestartdate or courseenddate > cycle.cycleenddate:
            raise serializers.ValidationError("Course date range must fall within the cycle date range.")

        return data

    def validate_overlap(self, data):
        """
        Custom validation to check for overlapping date ranges with other courses in the same cycle.
        """
        coursestartdate = data.get('coursestartdate')
        courseenddate = data.get('courseenddate')
        cycle = data.get('cycle')

        # Check if there are any overlapping courses within the same cycle
        overlapping_courses = CoursesPerCycle.objects.filter(
            cycle=cycle,
            courseenddate__gte=coursestartdate,
            coursestartdate__lte=courseenddate,
        ).exclude(pk=self.instance.pk if self.instance else None)

        if overlapping_courses.exists():
            raise serializers.ValidationError("Overlap detected with other courses in the same cycle.")

        return data

    def validate_duration(self, data):
        """
        Custom validation to verify that the course duration is within acceptable limits.
        """
        coursestartdate = data.get('coursestartdate')
        courseenddate = data.get('courseenddate')

        # Calculate the course duration in days
        duration_days = (courseenddate - coursestartdate).days

        # Add your minimum and maximum duration limits here
        min_duration = 10  # Adjust this value as needed
        max_duration = 90  # Adjust this value as needed

        if duration_days < min_duration or duration_days > max_duration:
            raise serializers.ValidationError("Course duration is not within acceptable limits.")

        return data

    def validate_unique_constraint(self, data):
        """
        Custom validation to ensure uniqueness of courses within the same cycle.
        """
        course = data.get('course')
        cycle = data.get('cycle')

        # Check if a course with the same cycle already exists
        if CoursesPerCycle.objects.filter(course=course, cycle=cycle).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("A course with the same cycle already exists.")

        return data
