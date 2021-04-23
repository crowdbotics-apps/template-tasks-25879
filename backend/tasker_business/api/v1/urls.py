from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    BusinessPhotoViewSet,
    TaskerAvailabilityViewSet,
    TaskerSkillViewSet,
    TimeslotViewSet,
)

router = DefaultRouter()
router.register("taskerskill", TaskerSkillViewSet)
router.register("businessphoto", BusinessPhotoViewSet)
router.register("taskeravailability", TaskerAvailabilityViewSet)
router.register("timeslot", TimeslotViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
