from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet

router = DefaultRouter()
router.register("registrations", RegistrationViewSet, basename="registrations")

urlpatterns = router.urls
