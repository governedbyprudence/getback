import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .postvalidator import validate
from django.views.decorators.csrf import csrf_exempt
from .models import users
# Create your views here.
def check_user_exists(request):
    if request.method == "GET":
        try:
            username = request.GET.get("username")
            try:
                queryset=users.objects.get(username=username)
                return JsonResponse({"message":"User present"},status=status.HTTP_200_OK)
            except users.DoesNotExist:
                return JsonResponse({"message":"Not found","exception":e},status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return JsonResponse({"message":"Wrong request","exception":e},status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def user_view(request):
    if request.method == "POST":
        data=json.loads(request.body.decode('utf-8'))
        if validate(data,"first_name","last_name","username","password"):
            first_name=data["first_name"]
            last_name=data["last_name"]
            username=data["username"]
            password=data["password"]
            try:
                userdata=users(first_name=first_name,last_name=last_name,username=username,password=password)
                userdata.save()
                return JsonResponse({"message":"User registered"},status=status.HTTP_201_CREATED)
            except Exception:
                return JsonResponse({"message":"Error occured"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
                return JsonResponse({"message":"Bad Request. Missing data"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"message":"Only post requests allowed"},status=status.HTTP_400_BAD_REQUEST)
