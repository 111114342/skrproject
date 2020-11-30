from django.contrib import admin
from .models import Contact, CourseEnq, ServiceEnq
# Register your models here.

admin.site.register(Contact)
admin.site.register(CourseEnq)
admin.site.register(ServiceEnq)
