from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Classes(models.Model):
    # fields for user input
    CRN = models.CharField(max_length=6)
    name = models.CharField(max_length=30, help_text='Enter course name:')
    credits = models.PositiveIntegerField(help_text='Enter course credits:', default=0)
    professor = models.CharField(max_length=30, help_text='Enter professor name:')
    location = models.CharField(max_length=50, help_text='Enter location:')
    start_time = models.DateTimeField(help_text='Enter starting time of class:')
    end_time = models.DateTimeField(help_text='Enter ending time of class:')
    for_user = models.ForeignKey(User, on_delete=models.CASCADE)

    # methods
    def get_absolute_url(self):  # returns a URL to display individual model records on website
        return reverse('course-detail', args=str(self.id))

    # string representation
    def __str__(self):
        myStr = ''
        myStr += 'CRN: ' + str(self.CRN) + '\nCourse Name: ' + self.name + \
                 '\nCourse Credits: ' + str(self.credits)
        return myStr

    def get_name(self):
        return self.name

    def get_CRN(self):
        return self.CRN

    def get_credits(self):
        return self.credits

    def get_professor(self):
        return self.professor

    def get_location(self):
        return self.location

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
