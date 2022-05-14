from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from list.models import List
from list.api.serializers import ListSerialzers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet


class ProvaVIewSet(ModelViewSet) :
    querySet = List.objects.all()
    lookup_field = "slug"
    serializer_class = ListSerialzers

    def perform_create(self, serializer):
        serializer.save()

class ListCreateAPIView(APIView):

    def get(self, request) :
        list = List.objects
        serializer = ListSerialzers(list, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) :
        serializer = ListSerialzers(data = request.data['content'])
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListDetailAPIView(APIView) :

    def get_object(self, pk) :
        list = get_object_or_404(List, pk=pk)
        return list

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListSerialzers(list)
        return Response(serializer.data)

    def put(self, request, pk) :
        list = self.get_object(pk)
        serializer = ListSerialzers(list, data = request.data['content'])
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) : 
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
