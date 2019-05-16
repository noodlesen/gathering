from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join, isdir, exists
import json
from random import shuffle, sample
from gthapp.models import Author, Footage, Tag, Post, Key
import subprocess

from gthapp.tag import get_tags, guess_keys_by_tags


class Command(BaseCommand):
    def handle(self, *args, **options):

        # tag_objects = Tag.objects.all()
        # with open('tags_real.txt', 'r') as f:
        #     txt = f.read()
        #     lines = [l.strip().replace(',','')[1:] for l in txt.split('posts')]
        #     tags = []
        #     tagnames = []
        #     for l in lines:
        #         if l:
        #             t = l.split('\n')
        #             tags.append((t[0],int(t[1]),))
        #             tagnames.append(t[0])

        #     print (tags)

        #     for t in tags:
        #         tag = Tag.objects.get(name=t[0])
        #         tag.rating = t[1]
        #         tag.save()
