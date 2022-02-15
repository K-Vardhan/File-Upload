from django.db import models

class PdfUpload(models.Model):
    name = models.CharField(max_length=50)
    pdf_file = models.FileField(blank=True, upload_to="./uploads")

    def __str__(self):
        return str(self.name)

class XmlUploade(models.Model):
    xml_file_name = models.CharField (max_length=50)
    xml_file = models.FileField(blank=True)

    def __str__(self):
        return str(self.xml_file_name)