from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'Manufacturer', ManufacturerViewSet)
router.register(r'ShoeColor', ShoeColorViewSet)
router.register(r'ShoeType', ShoeTypeViewSet)
router.register(r'Shoe', ShoeViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls))
]