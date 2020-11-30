"""gsct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('about-us/', views.About),
    path('blog/', views.Blog),
    path('blogdetails/', views.BlogDetails),
    path('courses/', views.Courses, name='courses'),
    path('course-enquiry/', views.CourseEnq.as_view(), name='courseenq'),
    path('course-details/', views.CourseDetails),
    path('contact-us/', views.Contact.as_view(), name = 'contact'),

            # -----------------Services------------------------->>>>>>>>>>>>>>>>>>>>
    path('service-enquiry/', views.ServiceEnqForm.as_view(), name = 'service-enquiry'),
        path('carporate-training/', views.Carporate, name='carporate-services'),
        path('accounting-services/', views.Accounting, name='accounting-services'),
        path('digital-marketing/', views.DigitalMarketing, name='digital-training'),
        path('workshop-seminar/', views.WorkshopSeminar, name='workshop-seminar'),
        path('networking/', views.Networking, name='networking'),
        path('website-development/', views.WebsiteDevelopment, name='website-development'),

    path('map/', views.default_map, name='map'),

# ==================================Admin Login===================================
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('adminapp.urls')),
]
