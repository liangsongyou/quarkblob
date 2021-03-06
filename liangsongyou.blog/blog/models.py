from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(default='',blank=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.slug)])


class Post(models.Model):
    title = models.CharField(max_length=255, default='', unique=True)
    slug = models.SlugField(default='', blank=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(default='', blank=True)
    body = models.TextField(default='',blank=True)
    image = models.ImageField(default='', blank=True, upload_to='post_images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(250,100)],
                                     format='JPEG',
                                     options={'quality':60})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(700,250)],
                                 format='JPEG',
                                 options={'quality':60})
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-post_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('item', args=[str(self.slug)])









































