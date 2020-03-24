from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

course_category = [
    ('Academics', 'Academics'),
    ('Business', 'Business'),
    ('Design', 'Design'),
    ('Development', 'Development'),
    ('Health & Fitness', 'Health & Fitness'),
    ('IT & Software', 'IT & Software'),
    ('Marketing', 'Marketing'),
    ('Music', 'Music'),
    ('Office Productivity', 'Office Productivity')
]


class ECourses(models.Model):
    image = models.ImageField(upload_to='pictures/', blank=True, null=True)
    # image_binary = models.BinaryField(blank=True, null=True, editable=True)
    # image_link = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=course_category)
    torrent_file = models.FileField(upload_to='torrent/', blank=True, null=True)
    # torrent_link = models.CharField(max_length=255, blank=True, null=True)
    # torrent_binary = models.BinaryField(blank=True, null=True, editable=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'E-Course'
        verbose_name_plural = 'E-Courses'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TopAd(models.Model):
    name = models.CharField(max_length=100)
    ad_link = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class BottomAd(models.Model):
    name = models.CharField(max_length=100)
    ad_link = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
