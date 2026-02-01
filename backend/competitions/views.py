from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Competition
from .serializers import CompetitionSerializer


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [AllowAny]
