from django.shortcuts import render
from django.http import  JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from .models import FirstMaster, SecondMaster, ThirdMaster


# Create your views here.

# пометил декоратором "@csrf_exempt", чтобы можно было тестировать через postman
# @csrf_exempt
def register(request):

    if request.method == "POST":

        # проверяем валидность JSON'а
        try:
            js_request = json.loads(request.body.decode())
        except json.decoder.JSONDecodeError:
            return JsonResponse({"response": "warning", "message": "json isn't valid!"})

        # проверяем заполнена ли форма
        for x in ["name", "surname", "patronymic", "auto_mark", "date_time", "master"]:
            if not js_request.get(x):
                return JsonResponse({ "response":"warning", "message": "form isn't filled!"})

        # проверяем указано ли время в правильном формате
        try:
            request_datetime = datetime.strptime( js_request["date_time"],  "%Y-%m-%dT%H:%M")
        except:
            return JsonResponse({"response": "warning", "message": "date-time isn't valid!"})

        # проверяем запись на прошедшее время
        # чтобы не допустить возможность записи на прошедшую дату или прошедшее время
        if (request_datetime-datetime.now()).days <= -1:
            return JsonResponse(
                {"response": "warning", "message": "registration on the past date-time is not allowed!"})

        # проверяем указанный день недели т.к. автомастерская работает с пн по пт
        if request_datetime.weekday() > 4:
            return JsonResponse(
                {"response": "warning", "message": "Car repair shop works from Monday to Friday from 10:00 to 20:00"})

        # проверяем указанное время т.к. автомастерская работает с 10:00 до 20:00
        if request_datetime.hour >= 20 or request_datetime.hour < 10:
            return JsonResponse(
                {"response": "warning", "message": "Car repair shop works from Monday to Friday from 10:00 to 20:00"})

        # проверяем правильнось указанного номера мастера
        if js_request["master"] not in ["1", "2", "3"]:
            return JsonResponse(
                {"response": "warning", "message": "invalid number of master!"})

        # request_day_upper_bound и request_day_lower_bound необходиы для фильтрации записей в указазнный день,
        # request_day_upper_bound служит как потолок(верхняя граница),
        # а request_day_lower_bound служит как пол(нижняя граница)
        request_day_upper_bound = datetime.strptime("{}-{}-{}T10:00".format(request_datetime.year, request_datetime.month,
                                                                       request_datetime.day), "%Y-%m-%dT%H:%M")

        request_day_lower_bound = datetime.strptime("{}-{}-{}T20:00".format(request_datetime.year, request_datetime.month,
                                                                       request_datetime.day), "%Y-%m-%dT%H:%M")

        if js_request["master"] == "1":
            if (request_datetime+timedelta(hours=1)).hour>=20:
                return JsonResponse({"response": "warning",
                     "message": "Car repair shop works from Monday to Friday from 10:00 to 20:00"})

            # получаем все записи на дату указанную в запросе
            qs_records_for_the_day = FirstMaster.objects.filter(register_date__gte=request_day_upper_bound,
                                                                register_date__lt=request_day_lower_bound)
            # если записей на укзанную дату не имеется, то записываем пользователя
            if qs_records_for_the_day.count() == 0:
                FirstMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                   patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                   register_date=request_datetime)
                return JsonResponse({"response": "Success!"})

            # если есть записи на указанную дату, то проверяем не пересекаются ли по времени имеющиеся записи
            # со временем указанным в запросе
            else:
                if qs_records_for_the_day.filter(register_date__gt=(request_datetime - timedelta(hours=1)),
                                              register_date__lt=(request_datetime + timedelta(hours=1))).count() == 0:

                    FirstMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                               patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                               register_date=request_datetime)
                    return JsonResponse({"response": "Success!"})
                else:
                   return JsonResponse({"response": "warning", "message": "requested time already are busy"})

        # работает по точно такой же логике как и для 1 мастера
        elif js_request["master"] == "2":
            if (request_datetime+timedelta(hours=1)).hour>=20:
                return JsonResponse({"response": "warning",
                     "message": "Car repair shop works from Monday to Friday from 10:00 to 20:00"})
            qs_records_for_the_day = SecondMaster.objects.filter(register_date__gte=request_day_upper_bound,
                                                                register_date__lt=request_day_lower_bound)

            if qs_records_for_the_day.count() == 0:
                SecondMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                   patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                   register_date=request_datetime)
                return JsonResponse({"response": "Success!"})
            else:
                if qs_records_for_the_day.filter(register_date__gt=(request_datetime - timedelta(hours=1)),
                                              register_date__lt=(request_datetime + timedelta(hours=1))).count() == 0:

                    SecondMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                               patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                               register_date=request_datetime)
                    return JsonResponse({"response": "Success!"})
                else:
                    return JsonResponse({"response": "warning", "message": "requested time already are busy"})

        # работает по точно такой же логике как и для 1 мастера
        elif js_request["master"] == "3":
            if (request_datetime+timedelta(hours=1)).hour>=20:
                return JsonResponse({"response": "warning",
                     "message": "Car repair shop works from Monday to Friday from 10:00 to 20:00"})

            qs_records_for_the_day = ThirdMaster.objects.filter(register_date__gte=request_day_upper_bound,
                                                                register_date__lt=request_day_lower_bound)
            if qs_records_for_the_day.count() == 0:
                ThirdMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                   patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                   register_date=request_datetime)
                return JsonResponse({"response": "Success!"})
            else:
                if qs_records_for_the_day.filter(register_date__gt=(request_datetime - timedelta(hours=1)),
                                              register_date__lt=(request_datetime + timedelta(hours=1))).count() == 0:

                    ThirdMaster.objects.create(surname=js_request["surname"], name=js_request["name"],
                                               patronymic=js_request["patronymic"], auto_mark=js_request["auto_mark"],
                                               register_date=request_datetime)
                    return JsonResponse({"response": "Success!"})
                else:
                    return JsonResponse({"response": "warning", "message": "requested time already are busy"})

    else:
        return render(request, "car_repair_shop/index.html")
