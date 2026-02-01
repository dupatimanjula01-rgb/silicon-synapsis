from rest_framework.routers import DefaultRouter
from .views import CompetitionViewSet

router = DefaultRouter()
router.register("competitions", CompetitionViewSet, basename="competitions")

urlpatterns = router.urls
