from django.urls import path
from courses.api import views


app_name = 'api'
urlpatterns = [
    path('subjects/',views.SubjectListView.as_view(),name='subject_list'),
    # path('modules/',views.ModuleListView.as_view(),name='module_list'),
    path('courses/<pk>/enroll/',views.CourseEnrollView.as_view(),name='course_enroll')
]