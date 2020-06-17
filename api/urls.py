from django.conf.urls import include, url
from django.urls import path

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoeViewSet
from api.views import index
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'Manufacturer', ManufacturerViewSet)
router.register(r'ShoeColor', ShoeColorViewSet)
router.register(r'ShoeType', ShoeTypeViewSet)
router.register(r'Shoe', ShoeViewSet)

urlpatterns = [
    path('', index),
    url(r"^api/", include(router.urls))
]