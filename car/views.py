import json

from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from .serializers import CarsSerializers
# Create your views here.


class getCars(APIView):
    def get(self, request):
        cars = Car.objects.all()
        car_serializers = CarsSerializers(cars, many=True)
        cars = car_serializers.data
        return Response(cars, status=status.HTTP_200_OK)

    def post(self, request):
        pass

