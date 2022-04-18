from django.urls import path
from .views import PerritoServicioContratadoViewSet, ServicioContratadoViewSet, ServiciosViewSet

urlpatterns = [
    path('servicios',ServiciosViewSet.as_view(
        {'get': 'list',
        'post': 'create'}
    )),
    path('servicios/<str:pk>', ServiciosViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('servicioscontratados',ServicioContratadoViewSet.as_view(
        {'get': 'list',
        'post': 'create'}
    )),
    path('servicioscontratados/<str:pk>', ServicioContratadoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('perritosservicioscontratados/<str:pk>', PerritoServicioContratadoViewSet.as_view({
        'get': 'filter',
        'put': 'update',
        'delete': 'destroy'
    })),
    # path('user', UserAPIView.as_view())
]
