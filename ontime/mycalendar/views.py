from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import Classes
from datetime import date
from .forms import CoursesForm


def classes_from_db(request):
    class_list = Classes.objects.all()
    return render(request, 'classlist.html', {'classes': class_list})


def classadd(request):
    if request.method == 'POST':
        print(request)
        form = CoursesForm(request.POST)
        if form.is_valid():
            course_item = form.save(commit=False)
            course_item.save()
    else:
        form = CoursesForm()
    return render(request, 'addclasses.html', {'form': form})


def mycalendar_view(request):
    return render(request, 'mycalendar.html')


def send_events(request):
    starty = request.GET.get("start").replace("%3A", ":")
    endy = request.GET.get("end").replace("%3A", ":")
    print(starty)
    print(endy)
    start_date = datetime.datetime.fromisoformat(starty)
    end_date = datetime.datetime.fromisoformat(endy)
    events = Classes.objects.filter(for_user__username__exact=request.user)
    x = []
    for event in events:
        # if start_date <= event.get_start_time() and end_date >= event.get_end_time():
        dicty = {}
        dicty["title"] = event.get_name()
        temp_date_start = event.get_start_date()
        temp_time_start = event.get_start_time()
        dicty["start"] = datetime.datetime.combine(temp_date_start, temp_time_start)
        temp_date_end = event.get_end_date()
        temp_time_end = event.get_end_time()
        dicty["end"] = datetime.datetime.combine(temp_date_end, temp_time_end)
        dicty["startRecur"] = event.get_start_date()
        dicty["startTime"] = event.get_start_time()
        frequ = event.frequency_of_course.all()
        temp1 = []
        print("\n\n", frequ, "\n\n")
        for day in frequ:
            day = str(day)
            if day == 'Sunday':
                temp1.append(0)
            elif day == 'Monday':
                temp1.append(1)
            elif day == 'Tuesday':
                temp1.append(2)
            elif day == 'Wednesday':
                temp1.append(3)
            elif day == 'Thursday':
                temp1.append(4)
            elif day == 'Friday':
                temp1.append(5)
            elif day == 'Saturday':
                temp1.append(6)
            else:
                pass
        dicty["daysOfWeek"] = temp1
        dicty["url"] = "http://google.com/"
        dicty["endRecur"] = event.get_end_date()
        dicty["endTime"] = event.get_end_time()
        x.append(dicty)
    print(x)
    print(start_date)
    print(end_date)

    return JsonResponse(x, safe=False)
