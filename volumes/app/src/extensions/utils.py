from . import jalali
from django.utils import timezone

def jalali_datetime(time):

    jalali_months = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    time_to_str = "{0},{1},{2}".format(time.year,time.month,time.day)
    gregorain_to_jalali = jalali.Gregorian(time_to_str).persian_tuple()
    time = timezone.localtime(time)
    
    if time.hour < 10:
        hour = "0{0}".format(time.hour)
    else:
        hour = time.hour
    
    if time.minute < 10:
        minute = "0{0}".format(time.minute)
    else:
        minute = time.minute

    outPut = "{0} {1} {2} | {3}:{4}".format(
        gregorain_to_jalali[2],
        jalali_months[gregorain_to_jalali[1]-1],
        #gregorain_to_jalali[1], #month number
        gregorain_to_jalali[0],
        hour,
        minute
    )
    
    return outPut