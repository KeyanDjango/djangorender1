from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from .serializers import TaskSerialzer
from rest_framework.response import Response
from rest_framework import status

from .models import TaskModel

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello World</h1>')


class TaskView(APIView):
    
    #POST
    def post(self,request):
        print(request.data)
        serializer = TaskSerialzer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #GET

    def get(self,request):

        tasktb = TaskModel.objects.all()
        serializer = TaskSerialzer(tasktb,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        try:
            tasktable = TaskModel.objects.get(id=id)
            tasktable.delete()
            return Response({'message':'Data deleted successfully'},status=status.HTTP_200_OK)
        except TaskModel.DoesNotExist:
            return Response({'message':'Data not found'},status=status.HTTP_400_BAD_REQUEST)
    #PUT
    def put(self,request,id):
        try:
            tasktable = TaskModel.objects.get(id=id)
            serializer = TaskSerialzer(tasktable,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
        except TaskModel.DoesNotExist:
            return Response({'message':'id not found'},status=status.HTTP_400_BAD_REQUEST)   
            

