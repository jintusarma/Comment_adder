from django.db import models

# Create your models here.
class AssameseDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L1 = models.CharField( max_length=1000,blank=True, null=True)
    
class BodoDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L2 = models.CharField( max_length=1000,blank=True, null=True)

class EnglishDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L3 = models.CharField( max_length=1000,blank=True, null=True)

class AllDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L1 = models.CharField( max_length=1000,blank=True, null=True)
    sentence_L2 = models.CharField( max_length=1000,blank=True, null=True)
    sentence_L3 = models.CharField( max_length=1000,blank=True, null=True)
    is_updated = models.BooleanField(default=False,verbose_name="Is Updated By User")