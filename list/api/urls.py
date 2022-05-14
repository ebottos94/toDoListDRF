from django.urls import path, include
from list.api.views import ListCreateAPIView, ListDetailAPIView, ProvaVIewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
#router.register(r"list", ProvaVIewSet, 'Lista')

urlpatterns = [
    #path("", include(router.urls)),
    path('list/', ListCreateAPIView.as_view(), name='list'),
    path('list/<int:pk>/', ListDetailAPIView.as_view(), name='list_detail')

]   