from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    #fields for user input
    course_CRN = models.PositiveIntegerField(help_text='Enter your course CRN:',
                                             default=000000)
    #course_name field designated as the primary_key, making it a special database column to
    # uniquely ID the different table records
    course_name = models.CharField(primary_key=True, max_length=30, help_text='Enter course name:')
    course_credits = models.PositiveIntegerField(help_text='Enter course credits:',
                                                 default=0)
    #creates relationship with CourseInstance class; on_delete allows for the value of the
    # associated course instance to be Null if deleted; null = True to allow databse to store
    # Null value if no instance is selected
    instance = models.ForeignKey('CourseInstance', on_delete=models.SET_NULL, null=True)

    #metadata
    class Meta:
        ordering = ['course_CRN', 'course_name', 'course_credits']

    #methods
    def get_absolute_url(self):#returns a URL to display individual model records on website
        return reverse('course-detail', args=str(self.id))

    #string representation
    def __str__(self):
        myStr = ''
        myStr += 'CRN: ' + str(self.course_CRN) + '\nCourse Name: ' + self.course_name + \
                 '\nCourse Credits: ' + str(self.course_credits)
        return myStr

class CourseInstance(models.Model):
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
    professor_name = models.CharField(max_length=40, help_text='Enter professor name:')
    course_location = models.CharField(max_length=20, help_text='Enter course location:')
    frequency_of_course = models.CharField(
        max_length= 7,
        primary_key=True,
        choices=DAYS_OF_THE_WEEK,
        default=None,
        help_text='Course Frequency:'
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['professor_name', 'course_location', 'frequency_of_course', 'start_time',
                    'end_time', 'start_date', 'end_date']

    def get_absolute_url(self):
        return reverse('course_instance-detail', args=str(self.id))

    def __str__(self):
        return 'Professor Name: ' + self.professor_name + 'Course Location: ' + \
               self.course_location + '\nCourse Frequency: ' + self.frequency_of_course + \
               '\nStart Time: ' + str(self.start_time) + '\nEnd Time: ' + str(self.end_time) + \
               '\nStart Date: ' + str(self.start_date) + '\nEnd Date: ' + str(self.end_date)
