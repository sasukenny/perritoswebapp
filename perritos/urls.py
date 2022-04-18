from django.urls import path
from .views import PerritosViewSet

urlpatterns = [
    path('perritos', PerritosViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('perritos/<str:pk>', PerritosViewSet.as_view({
        'get': 'filter',
        'put': 'update',
        'delete': 'destroy'
    })), 
    # path('user', UserAPIView.as_view())
]
