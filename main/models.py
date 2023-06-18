from django.db import models

# Create your models here.
class AssameseBodoDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L1 = models.CharField( max_length=1000,blank=True, null=True)
    sentence_L2 = models.CharField( max_length=1000,blank=True, null=True)
    score = models.CharField("Score ", max_length=1000,blank=True, null=True)
    remark = models.CharField("Remark ", max_length=1000,blank=True, null=True)
    typee = models.CharField("Type ", max_length=1000,blank=True, null=True)
    dataset_lang = models.CharField("Dataset Language", max_length=100,blank=True, null=True,default="ab")

class AssameseEnglishDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L1 = models.CharField( max_length=1000,blank=True, null=True)
    sentence_L2 = models.CharField( max_length=1000,blank=True, null=True)
    score = models.CharField("Score ", max_length=1000,blank=True, null=True)
    remark = models.CharField("Remark ", max_length=1000,blank=True, null=True)
    typee = models.CharField("Type ", max_length=1000,blank=True, null=True)
    dataset_lang = models.CharField("Dataset Language", max_length=100,blank=True, null=True,default="ae")

class BodoEnglishDataset(models.Model):
    domain = models.CharField("Domain", max_length=1000,blank=True, null=True)
    sentence_L1 = models.CharField( max_length=1000,blank=True, null=True)
    sentence_L2 = models.CharField( max_length=1000,blank=True, null=True)
    score = models.CharField("Score ", max_length=1000,blank=True, null=True)
    remark = models.CharField("Remark ", max_length=1000,blank=True, null=True)
    typee = models.CharField("Type ", max_length=1000,blank=True, null=True)
    dataset_lang = models.CharField("Dataset Language", max_length=100,blank=True, null=True,default="be")
