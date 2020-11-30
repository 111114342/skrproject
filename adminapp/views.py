from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from app1.models import Contact, ServiceEnq, CourseEnq

# Create your views here.

def AdminHome(reqest):
    return render(reqest, 'adminapp/adminhome.html')

# =========================contact us ============================
# Contact Us list view
@method_decorator(login_required, name='dispatch')
class ContactUsList(ListView):
    model = Contact
    template_name = 'adminapp/contactuslist.html'
    context_object_name = 'contactenq'


@login_required
def DeleteContactEnq(request, id):
    mydict = {'msg':'Enquiry Deleted'}
    del_enq = Contact.objects.get(id=id)
    del_enq.delete()
    del_enq = Contact.objects.all()
    return HttpResponseRedirect("/contactenqlist/")

#
# class DeleteContactEnq(DeleteView):
#     model = Contact
#     def get_success_url(self):
#         return reverse('contactus_list')


# =========================Service Enq ============================
# Service Enq list view
@method_decorator(login_required, name='dispatch')
class ServiceEnqList(ListView):
    model = ServiceEnq
    template_name = 'adminapp/serviceenqlist.html'
    context_object_name = 'serviceenq'

@login_required
def DeleteServiceEnq(request, id):
    mydict = {'msg':'Service Enq Deleted'}
    del_serv_enq = ServiceEnq.objects.get(id=id)
    del_serv_enq.delete()
    del_serv_enq = ServiceEnq.objects.all()
    return HttpResponseRedirect("/serviceenqlist/")

# =========================Course Enq ============================
#Course Enq list view
@method_decorator(login_required, name='dispatch')
class CourseEnqList(ListView):
    model = CourseEnq
    template_name = 'adminapp/courseenqlist.html'
    context_object_name = 'courseenq'

@login_required
def DeleteCourseEnq(request, id):
    mydict = {'msg':'Service Enq Deleted'}
    del_course_enq = CourseEnq.objects.get(id=id)
    del_course_enq.delete()
    del_course_enq = CourseEnq.objects.all()
    return HttpResponseRedirect("/courseenqlist/")
