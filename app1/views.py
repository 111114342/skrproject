from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from app1.models import Contact, CourseEnq, ServiceEnq
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse
# Create your views here.

def Home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2hla2hhcjc0NCIsImEiOiJja2dvdDQ5M3YwM2w4Mnh0ZDAyZzluaGxpIn0.1BFVovW8uLSJHaNit6_RTA'
    return render(request, 'app1/index.html' ,{'mapbox_access_token': mapbox_access_token })

def About(request):
    return render(request, 'app1/about-us.html')

def Blog(request):
    return render(request, 'app1/blog.html')

def BlogDetails(request):
    return render(request, 'app1/blogdetails.html')

def Courses(request):
    return render(request, 'app1/courses.html')

def CourseDetails(request):
    return render(request, 'app1/course-details.html')


# <<<<<<<<<<<<<<--------Services Section----------->>>>>>>>>>>>
def Carporate(request):
    return render(request, 'app1/services/carporate.html')

def WorkshopSeminar(request):
    return render(request, 'app1/services/workshop-seminar.html')

def DigitalMarketing(request):
    return render(request, 'app1/services/digital-marketing.html')

def Networking(request):
    return render(request, 'app1/services/networking.html')

def Accounting(request):
    return render(request, 'app1/services/accounting-services.html')

def WebsiteDevelopment(request):
    return render(request, 'app1/services/website-development.html')
'''

def Contact(reqest):
    if reqest.method == 'POST':
        name = reqest.POST.get('cname')
        email = reqest.POST.get('cemail')
        subject = reqest.POST.get('csubject')
        msg = reqest.POST.get('cmessage')
        contact = Contact(name=name,email=email,subject=subject,message=msg)
        contact.save()
        # print(name, email, subject, msg)
    return render(reqest, 'app1/contact.html')
'''

class Contact(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'app1/contact.html'
    def get_success_url(self):
        return reverse('contact')



class CourseEnq(CreateView):
    model = CourseEnq
    fields = '__all__'
    template_name = 'app1/regform.html'
    def get_success_url(self):
        return reverse('courseenq')

class ServiceEnqForm(CreateView):
    model = ServiceEnq
    fields = '__all__'
    template_name = 'app1/serviceform.html'
    def get_success_url(self):
        return reverse('service_enq')

def default_map(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2hla2hhcjc0NCIsImEiOiJja2dvdDQ5M3YwM2w4Mnh0ZDAyZzluaGxpIn0.1BFVovW8uLSJHaNit6_RTA'
    return render(request, 'app1/map.html', { 'mapbox_access_token': mapbox_access_token })

# ==============================Admin Login Section ==========================
def AdminLogin(request):
    return HttpResponseRedirect('/accounts/login')
