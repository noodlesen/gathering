from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join, isdir, exists
import json
from gthapp.models import Author, Footage, Tag


class Command(BaseCommand):

    def handle(self, *args, **options):

        Author.objects.all().delete()
        Footage.objects.all().delete()

        mypath = 'igs_selected'
        dirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]
        for d in dirs:
            print('\n\nDIRECTORY:', d)
            dl = listdir(join(mypath, d))

            with open(join(mypath,d,d+'.json'), 'r') as j:

                try:
                    a = Author.objects.get(nickname=d)
                except Author.DoesNotExist:
                    a = Author(nickname=d)
                    a.save()

                jj = json.loads(j.read())
                for im in jj['GraphImages']:

                    sc = im.get('shortcode', None)

                    tags = im.get('tags', None)
                    print (tags)

                    try:
                        text = im['edge_media_to_caption']['edges'][0]['node']['text']
                    except:
                        print('no text')
                        print (im['edge_media_to_caption'])

                    imf = im['urls'][0].split('?')[0].split('/')[-1]
                    print(imf)

                    fpth = join(mypath, d, imf)
                    if (exists(fpth)) and not fpth.endswith('.mp4'):
                        try:
                            ftg = Footage.objects.get(path=fpth)
                        except Footage.DoesNotExist:
                            tags = " ".join(tags) if tags else ''
                            ftg = Footage(path=fpth, author=a, url=im['urls'][0], tags=tags, shortcode=sc, text=text)
                            ftg.save()
                    else:
                        print('MISSING!')

