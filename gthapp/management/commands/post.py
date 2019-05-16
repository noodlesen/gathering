#imports tags made by tagcloud

from django.core.management.base import BaseCommand
from os import listdir, remove
from os.path import isfile, join, isdir, exists
import json
from gthapp.models import Author, Footage, Tag, Key, Post


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('command', type=str)
        parser.add_argument('ids', nargs='+', type=int)

        parser.add_argument(
            '--upto',
            action='store_true',
            help='',
        )

        parser.add_argument(
            '--footage',
            action='store_true',
            help='',
        )

        parser.add_argument(
            '--file',
            action='store_true',
            help='',
        )

    def handle(self, *args, **options):

            print (options)
            if not options['upto']:
                for i in options['ids']:
                    print ('Ready to deploy', i)
                posts = Post.objects.filter(pk__in=options['ids'])
                if len(posts)!=len(options['ids']):
                    print('SOME IDs ARE MISSING')
            else:
                posts = Post.objects.filter(pk__lte=max(options['ids']))
                for p in posts:
                    print('Posts ready', p.id)
            print ('TOTAL: %d posts' % len(posts))

            if options['command'] == 'mark_deployed':
                ans = input('Are you sure you want to deploy it? y/n: ')
                if ans in ['y', 'Y']:
                    for p in posts:
                        p.deployed = True
                        p.save()

            elif options['command'] == 'delete':
                ans = input('Are you sure you want to delete it? y/n: ')
                if ans in ['y', 'Y']:
                    for p in posts:
                        p.delete()
                        if options['footage'] is True:
                            if options['file'] is True:
                                print ('removing ', p.footage.path)
                                input()
                                try:
                                    remove(p.footage.path)
                                except:
                                    print('Error')
                                else:
                                    print('File has been removed succesfully')
                            p.footage.delete()

            elif options['command']=='cleanup':
                ftg = Footage.objects.all()
                broken = []
                for f in ftg:
                    if not exists(f.path) or not f.path:
                        broken.append(f)

                for b in broken:
                    print(b)
                    b.delete()










