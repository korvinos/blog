# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Заголовок')
    text = RichTextUploadingField(blank=True, default='')
    tags = models.CharField(blank=True, null=True, max_length=500, verbose_name='Ключевые слова')
    created = models.DateTimeField(blank=True, auto_created=True, verbose_name=u'Дата публикации')
    changed = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=u'Последние изменение')
    photo = models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
    created = models.DateTimeField(blank=True, auto_created=True)

