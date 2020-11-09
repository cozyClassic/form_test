from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class apply_inform(models.Model) :
    
    고객명 = CharField(max_length = 20)
    고객주소 = CharField(max_length = 100, default='Empty')
    주민등록번호 = IntegerField(default=-1)
    연락처 = IntegerField(default=-1)
    신분증사진 = models.ImageField(("ID"), null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self): return self.고객명

