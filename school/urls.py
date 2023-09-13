from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
