from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your docs models here.

class doc_m_docmaster(models.Model):
    doc_area = models.CharField(max_length=10)
    doc_subarea = models.CharField(max_length=10,blank=True)
    doc_tag = models.CharField(max_length=30,blank=True)
    doc_sub = models.CharField(max_length=100)
    doc_public = models.TextField(blank=True)
    doc_register = models.TextField(blank=True)
    doc_private = models.TextField(blank=True)
    doc_ref = models.TextField(blank=True)

class doc_m_files(models.Model):
    id = models.AutoField( primary_key=True)
    file_name = models.CharField(max_length=200,blank=True)
    file_url = models.CharField(max_length=800,blank=True)
    file_gname = models.CharField(max_length=800,blank=True)
    file_data_public = models.FileField(upload_to='ITBones_Public', storage=gd_storage,blank=True)
    file_data_private = models.FileField(upload_to='ITBones_Private', storage=gd_storage,blank=True)
    file_data_local = models.FileField(upload_to='Documents',blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.file_name

