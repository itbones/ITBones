from django.db import models

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

