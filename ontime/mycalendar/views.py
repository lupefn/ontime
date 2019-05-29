from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import Classes


def mycalendar_view(request):
    return render(request, 'mycalendar.html')


# 2019-03-31
# T00:00:00
# -04:00
def send_events(request):
    print(request.GET.get("start"))
    print(request.GET.get("end"))
    print(request.user)
    start_date = datetime.datetime.fromisoformat(request.GET.get("start"))
    end_date = datetime.datetime.fromisoformat(request.GET.get("end"))
    events = Classes.objects.filter(for_user__username__exact=request.user)
    x = []
    for event in events:
        # if start_date <= event.get_start_time() and end_date >= event.get_end_time():
        dicty = {}
        dicty["title"] = event.get_name()
        dicty["start"] = event.get_start_time()
        dicty["end"] = event.get_end_time()
        x.append(dicty)
    print(x)
    print(start_date)
    print(end_date)

    return JsonResponse(x, safe=False)
