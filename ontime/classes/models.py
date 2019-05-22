from django.db import models

# Create your models here.
class Courses(models.Model):
    #fields for user input
    course_CRN = models.PositiveIntegerField(max_length=6)
    course_name = models.CharField(max_length=30, help_text='Enter course name:')
    professor_name = models.CharField(max_length=40, help_text='Enter professor name:')
    course_location = models.CharField(max_length=20, help_text='Enter course location:')
    course_credits = models.PositiveIntegerField(max_length=1, help_text='Enter course credits:')

    #metadata
    class Meta:
        ordering = ['course_CRN', 'course_name', 'professor_name', 'course_location', 'course_credits']

    #methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=str(self.id))

    #string representation
    def __str__(self):
        myStr = ''
        myStr += 'CRN: ' + str(self.course_CRN) + '\nCourse Name: ' + self.course_name + '\nCourse Professor: '+ self.professor_name + '\nCourse Location: ' + self.course_name + '\nCredit Number: '
        return myStr

class CourseFrequency(models.Model):
    MONDAY = 'MON'
    TUESDAY = 'TUES'
    WEDNESDAY = 'WED'
    THURSDAY = 'THURS'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    DAYS_OF_THE_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    frequency_of_course = models.CharField(choices=DAYS_OF_THE_WEEK, default=None)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['frequency_of_course', 'start_time', 'end_time']

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.frequency_of_course