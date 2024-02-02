from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from pheno.views import ExperimentAPIList, ExperimentAPIUpdate, ExperimentAPIDetailView, VarietyAPIList, VarietyAPIDetailView, VarietyAPIUpdate, BoxAPIDetailView, BoxAPIList, BoxAPIUpdate, CurrentValuesAPIList, CurrentValuesAPIDetailView, CurrentValuesAPIUpdate

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/experiment', ExperimentAPIList.as_view()),
    path('api/experiment/<int:pk>', ExperimentAPIUpdate.as_view()),
    path('api/experimentdetail/<int:pk>', ExperimentAPIDetailView.as_view()),
    
    path('api/variety', VarietyAPIList.as_view()),
    path('api/variety/<int:pk>', VarietyAPIUpdate.as_view()),
    path('api/varietydetail/<int:pk>', VarietyAPIDetailView.as_view()),
    
    path('api/box', BoxAPIList.as_view()),
    path('api/box/<int:pk>', BoxAPIUpdate.as_view()),
    path('api/boxdetail/<int:pk>', BoxAPIDetailView.as_view()),
    
    path('api/currentvalues', CurrentValuesAPIList.as_view()),
    path('api/currentvalues/<int:pk>', CurrentValuesAPIUpdate.as_view()),
    path('api/currentvaluesdetail/<int:pk>', CurrentValuesAPIDetailView.as_view()),
]

urlpatterns += router.urls