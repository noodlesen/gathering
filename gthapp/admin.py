from django.contrib import admin
from gthapp.models import Author, Footage, Post, Tag, Key

# Register your models here.

admin.site.register(Author)
admin.site.register(Footage)
admin.site.register(Post)
admin.site.register(Key)
admin.site.register(Tag)