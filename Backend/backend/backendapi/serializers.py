from pyexpat import model
from rest_framework import serializers
from .models import PdfUpload
from .models import XmlUploade

class PdfUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = PdfUpload
        fields = '__all__'

class XmlUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = XmlUploade
        fields = '__all__'