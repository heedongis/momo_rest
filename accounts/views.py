from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Accounts
from .serializers import AccountsSerializer


# Create your views here.

@csrf_exempt
def accounts_list(request):
    # 전체 회원 조회
    if request.method == 'GET':
        query_set = Accounts.objects.all()
        serializer = AccountsSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    # 회원 등록
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def accounts(request, pk):

    obj = Accounts.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AccountsSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountsSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = Accounts.objects.get(name=search_name)

        if data['password'] == obj.password:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)