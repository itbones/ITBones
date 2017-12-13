from django.db import models

# Create your models here.

class m_webmaster(models.Model):
    folder = models.CharField(max_length=30)
    topic = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.topic

class m_webitem(models.Model):
    weblink = models.CharField(max_length=300)
    master = models.ForeignKey(m_webmaster, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.weblink



class m_webmark(models.Model):
    folder = models.CharField(max_length=30)
    topic = models.CharField(max_length=100)
    addinfo = models.CharField(max_length=300)
    link = models.CharField(max_length=150)
    linkinfo = models.TextField()
    user = models.CharField(max_length=50)
    stamp = models.DateTimeField()

