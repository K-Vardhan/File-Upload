from django.urls import include, path
from rest_framework import routers
from backendapi import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/FileUploade', views.PdfViewSet)
router.register('api/XmlUploade', views.XmlViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
