from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class DaysOfTheWeek(models.Model):
    day = models.CharField(max_length=9)

    def __str__(self):
        return self.day


# Create your models here.
class Classes(models.Model):
    # fields for user input
    CRN = models.CharField(max_length=6)
    name = models.CharField(max_length=30, help_text='Enter course name:')
    credits = models.PositiveIntegerField(help_text='Enter course credits:', default=0)
    professor = models.CharField(max_length=30, help_text='Enter professor name:')
    location = models.CharField(max_length=50, help_text='Enter location:')
    frequency_of_course = models.ManyToManyField(DaysOfTheWeek)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    for_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'

    # methods
    def get_absolute_url(self):  # returns a URL to display individual model records on website
        return reverse('course-detail', args=str(self.id))

    # string representation
    def __str__(self):
        myStr = 'CRN: ' + str(self.CRN) + '\nCourse Name: ' + self.name + '\nCourse Credits: ' + str(self.credits)
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

    def get_end_date(self):
        return self.end_date

    def get_start_date(self):
        return self.start_date
