from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('adminhome/', views.AdminHome, name='admin_home'),
    path('contactenqlist/', views.ContactUsList.as_view(), name='contactus_list'),
    path('serviceenqlist/', views.ServiceEnqList.as_view(), name='service_enq_list'),
    path('courseenqlist/', views.CourseEnqList.as_view(), name='course_enq_list'),
    # path('contactenq/<id>', views.ContactEnq.as_view(), name='contact'),

    path('deletecontactenq/<id>', views.DeleteContactEnq, name='delete_contact_enq'),
    path('deleteserviceenq/<id>', views.DeleteServiceEnq, name='delete_service_enq'),
    path('deletecourseenq/<id>', views.DeleteCourseEnq, name='delete_course_enq'),

]
