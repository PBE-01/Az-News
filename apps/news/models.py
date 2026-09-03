from django.db import models
from apps.base.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Category Name', help_text='The field is saved news category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name='News title', help_text='The field is saved news title')
    description = models.TextField(verbose_name='News description', help_text='The field is saved news description')
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='News Image', help_text='The field is saved news image')
    content = CKEditor5Field('Content', config_name='extends', verbose_name='News content', help_text='The field is saved news content')

    def __str__(self):
        return self.title