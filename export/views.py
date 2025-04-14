from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Export
from common.permissions import IsOwnerOrAdmin
from .serializers import ExportSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ExportListCreateView(generics.ListCreateAPIView):
    queryset = Export.objects.all()
    serializer_class = ExportSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ExportRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Export.objects.all()
    serializer_class = ExportSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ExportDownloadView(generics.RetrieveAPIView):
    queryset = Export.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def retrieve(self, request, *args, **kwargs):
        export = self.get_object()
        if not export.file:
            return Response(
                {"detail": "Export file not ready yet."},
                status=status.HTTP_404_NOT_FOUND
            )

        response = Response()
        response['Content-Disposition'] = f'attachment; filename="{export.file.name}"'
        response['X-Accel-Redirect'] = export.file.url
        return response