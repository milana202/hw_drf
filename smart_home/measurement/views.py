# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def post(self, request):
        return self.create(request)

class ChangeSensorView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def putch(self, request):
        return self.put(request)

class AddMeasureView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        return self.create(request)

class GetSensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request):
        return Response({'status': 'ok'})
