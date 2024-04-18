from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.FlightViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('flights/<str:pk>/', views.FlightViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('user/', views.UserAPIView.as_view())
]