from django.urls import path
from measurement.views import CreateSensorView, ChangeSensorView, AddMeasureView, GetSensorsList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('create_sensor/', CreateSensorView.as_view()),
    path('change_sensor/<pk>/', ChangeSensorView.as_view()),
    path('add_measure/', AddMeasureView.as_view()),
    path('get_sensor/', GetSensorsList.as_view()),
]
