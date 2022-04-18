from django.urls import path

from reports.views import ResportesViewSet


urlpatterns = [
    path('reportes', ResportesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('reportes/<str:pk>', ResportesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })), 
    # path('user', UserAPIView.as_view())
]
