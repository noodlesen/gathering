#imports tags made by tagcloud

from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join, isdir, exists
import json
from gthapp.models import Author, Footage, Tag, Key, Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs='+', type=int)

        parser.add_argument(
            '--upto',
            action='store_true',
            help='',
        )

    def handle(self, *args, **options):
        if not options['upto']:
            for i in options['ids']:
                print ('Ready to deploy', i)
            posts = Post.objects.filter(pk__in=ids)
            if len(posts)!=len(ids):
                print('SOME IDs ARE MISSING')
        else:
            posts = Post.objects.filter(pk__lte=max(options['ids']))
            for p in posts:
                print('Ready to deploy', p.id)
        print ('TOTAL: %d posts' % len(posts))
        ans = input('Are you sure? y/n: ')
        if ans in ['y', 'Y']:
            for p in posts:
                p.deployed = True
                p.save()

