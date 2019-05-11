#imports tags made by tagcloud

from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join, isdir, exists
import json
from gthapp.models import Author, Footage, Tag, Key


class Command(BaseCommand):

    def handle(self, *args, **options):

        inp = input('ALL TAGS AND KEYS WILL BE ERASED. ARE YOU SURE? ')
        if inp=='y' or inp=='Y':

            Tag.objects.all().delete()
            Key.objects.all().delete()

            with open('import/hashdict_paint.txt', 'r') as f:
                lines = f.read().split('\n')
                for l in lines:
                    if l!='' and l!=' ' and l!='\n':
                        words = l.split(' ')
                        key = Key(name=words[0])
                        key.save()
                        for w in words[1:]:
                            name, rating = w.split(':')
                            tag = Tag(name=name, rating=int(rating), key=key)
                            tag.save()