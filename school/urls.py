from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for school project.

"""

from django.contrib import admin
from django.urls import path 

from .assignments.views import (
        AssignmentListView,
        AssignmentDetailView,
        SubmissionListView,
        SubmissionDetailView,
    ) 
from .attendance.views import (
        AttendanceListView,
        AttendanceDetailView,
    )
from .categories.views import (
        CategoryListCreateView,
        CategoryDetailView,
    )
from .classes.views import (
        ClassListView,
        ClassDetailView,
    )
from .course.views import (
        CourseListView,
        CourseDetailView,
        CoursesPerCycleListView,
        CoursesPerCycleDetailView,
    )
from .cycle.views import (
        CycleListView,
        CycleDetailView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('api/assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('api/submissions/', SubmissionListView.as_view(), name='submission-list'),
    path('api/submission/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('api/attendances/', AttendanceListView.as_view(), name='attendance-list'),
    path('api/attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('api/category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/classes/', ClassListView.as_view(), name='class-list'),
    path('api/class/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('api/courses/', CourseListView.as_view(), name='course-list'),
    path('api/course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('api/coursespercycles/', CoursesPerCycleListView.as_view(), name='course-per-cycle-list'),
    path('api/coursespercycle/<int:pk>/', CoursesPerCycleDetailView.as_view(), name='course-per-cycle-detail'),
    path('api/cycles/', CycleListView.as_view(), name='cycle-list'),
    path('api/cycle/<int:pk>/', CycleDetailView.as_view(), name='cycle-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
