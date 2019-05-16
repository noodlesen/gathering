from django.db import models

# Create your models here.


class Key(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    common = models.BooleanField(default=False)


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)
    local_count = models.IntegerField(default=None, null=True)
    global_count = models.IntegerField(default=None, null=True)
    original = models.BooleanField(default=True)
    rating = models.IntegerField(default=None, null=True)
    key = models.ForeignKey(Key, null=True, on_delete=models.CASCADE)
    permanent = models.BooleanField(default=False)


class UsersGroup(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    def __str__(self):
        return self.nickname

    nickname = models.CharField(max_length=100)
    group = models.ManyToManyField(UsersGroup, blank=True)
    key = models.ManyToManyField(Key, blank=True)


class Footage(models.Model):
    def __str__(self):
        return self.path

    url = models.CharField(max_length=255)
    path = models.CharField(max_length=255, null=True)
    text = models.TextField(default=None, null=True)
    tags = models.TextField(default=None, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    shortcode = models.CharField(max_length=30, null=True)


class Post(models.Model):
    tags = models.TextField(default=None)
    text = models.TextField(default=None)
    approved = models.BooleanField(default=False)
    deployed = models.BooleanField(default=False)
    footage = models.ForeignKey(Footage, on_delete=models.SET_NULL, null=True)


##****

class Project(models.Model):
    name = models.CharField(max_length=255)
    keys = models.ManyToManyField(blank=True)
    tags = models.ManyToManyField(blank=True)
    footages = models.ManyToManyField(blank=True)
    posts = models.ManyToManyField(blank=True)








