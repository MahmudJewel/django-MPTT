from django.db import models

# Create your models here.

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Tag(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name
    
class Descriptions(models.Model):
    tag = models.ManyToManyField(Tag, related_name='tagRelatedName')
    # tag2=models.ModelChoiceField(queryset=Tag.objects.all(), blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title