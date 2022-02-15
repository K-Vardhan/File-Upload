
import imp
from rest_framework import viewsets
from .models import PdfUpload, XmlUploade
from .serializers import PdfUploadSerializers
from .serializers import XmlUploadSerializers


class PdfViewSet(viewsets.ModelViewSet):
    queryset = PdfUpload.objects.all()
    serializer_class = PdfUploadSerializers

class XmlViewSet(viewsets.ModelViewSet):
    queryset = XmlUploade.objects.all()
    serializer_class = XmlUploadSerializers
