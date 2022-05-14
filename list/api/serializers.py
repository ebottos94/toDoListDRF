from rest_framework import serializers
from list.models import List

class ListSerialzers(serializers.ModelSerializer) :
    class Meta:
        model = List
        fields = '__all__'