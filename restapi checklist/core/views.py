from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView    
from core.models import CheckList,CheckListItem 
from rest_framework import status
from django.http import Http404

from core.serializers import CheckListSerializer,CheckListItemSerializer
# Create your views here.


class TestAPIView(APIView):
    
    def get(self,request,format=None):
        return Response({'name':'Gaurav from clas api'})



class CheckListsApiView(APIView):
    serializer_class = CheckListSerializer

    def get(self,request):
        data = CheckList.objects.all()

        serializer = self.serializer_class(data,many=True)
        serialized_data= serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self,request,format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status= status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)    


class CheckListApiView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self,pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404
            

    def get(self,request,pk,format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data

        return Response(serialized_data,status = status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateApiView(APIView):
    serializer_class = CheckListItemSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    

class CheckListItemApiView(APIView):
    serializer_class = CheckListItemSerializer

    def get_object(self,pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item,data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serialized_data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
