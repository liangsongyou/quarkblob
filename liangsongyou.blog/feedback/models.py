from django.db import models

from django.utils.text import slugify
from django.urls import reverse

class Feedback(models.Model):

    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('feedback_item',args=[str(self.slug)])