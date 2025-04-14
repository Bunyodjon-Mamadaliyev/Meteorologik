from django.urls import path
from . import views

urlpatterns = [
    path('exports/', views.ExportListCreateView.as_view(), name='export-list'),
    path('exports/<int:pk>/', views.ExportRetrieveDestroyView.as_view(), name='export-detail'),
    path('exports/<int:pk>/download/', views.ExportDownloadView.as_view(), name='export-download'),
]