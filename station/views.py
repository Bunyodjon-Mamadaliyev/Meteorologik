from rest_framework import generics, permissions
from .models import Station
from .serializers import StationSerializer
from common.permissions import IsAdminOrReadOnly
from common.pagination import DefaultPagination


class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    lookup_field = 'pk'
