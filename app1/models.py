from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 55)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    def __str__(self):
        return self.name

class CourseEnq(models.Model):
    GENDER_CHOICES = (('male','Male'),('female','Female'),('other','Other'))
    COURSE_CHOICES = (('Programming Language','Programming Language'), ('Web Development', 'Web Development'), ('Ethical Hacking', 'Ethical Hacking'), ('Digital Marketing', 'Digital Marketing'), ('Networking & CCNA', 'Networking & CCNA'), ('Cloud Computing', 'Cloud Computing'), ('Graphic Designing', 'Graphic Designing'), ('Basic Computer', 'Basic Computer'))
    StudentName = models.CharField(max_length = 55, verbose_name="Student's Name")
    StudentMobile = models.IntegerField(verbose_name="Student's Mobile")
    StudentEmail = models.EmailField(verbose_name="Student's Email")
    Qualification = models.CharField(max_length = 55, verbose_name="Highest Qualification" )
    Gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "MALE")
    FatherName = models.CharField(max_length = 55, verbose_name="Father's Name")
    FatherMobile = models.IntegerField(verbose_name="Father's Mobile")
    CourseChoice = models.CharField(max_length = 55,choices = COURSE_CHOICES,default = "--Select a Course--", verbose_name="Select a Course")
    def __str__(self):
        return self.StudentName +"  "+ self.CourseChoice

class ServiceEnq(models.Model):
    SERVICE_CHOICES = (('Corporate Training','Corporate Training'), ('Workshop & Seminar', 'Workshop & Seminar'), ('Web Developement', 'Web Developement'), ('Digital Marketing', 'Digital Marketing'), ('Hardware & Networking', 'Hardware & Networking'), ('Accounting Service', 'Accounting Service'), ('Graphic Designing', 'Graphic Designing'))
    GENDER_CHOICES = (('male','Male'),('female','Female'),('other','Other'))
    ClientName = models.CharField(max_length = 55,verbose_name="Name")
    Mobile = models.IntegerField()
    Email = models.EmailField()
    WorkingOrganization = models.CharField(max_length = 55)
    Gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "MALE")
    ServiceChoice = models.CharField(max_length = 55,choices = SERVICE_CHOICES,default = "--Select a Service--", verbose_name="Select a Service")
    def __str__(self):
        return self.ClientName + " " + self.ServiceChoice
