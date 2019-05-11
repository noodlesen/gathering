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

        RES_FOLDER = 'res'
        POSTS_PER_AUTHOR = 5

        Post.objects.filter(deployed=False).delete()
        deployed_footage_scs =[p.footage.shortcode for p in Post.objects.filter(deployed=True)]
        status = subprocess.call('rm -rf '+RES_FOLDER, shell=True)
        status = subprocess.call('mkdir '+RES_FOLDER, shell=True)

        # ftgs = Footage.objects.all()[:200]
        # ftgs_count = len(ftgs)
        # ssc = [ftg.shortcode for ftg in ftgs]
        # shuffle(ssc)

        # for ftg in ftgs:
        #     if ftg.shortcode in scl:
        #         p = Post(footage=ftg,)
        #         p.approved = True
        #         p.save()

        

        authors = Author.objects.all()
        shortcodes = []
        for a in authors:
            footages = a.footage_set.all()
            ftgs_count = len(footages)
            sample_len = POSTS_PER_AUTHOR if ftgs_count>POSTS_PER_AUTHOR else ftgs_count
            choice = sample([f.shortcode for f in footages], sample_len)
            shortcodes.extend(choice)
        shuffle(shortcodes)

        shortcodes = [s for s in shortcodes if s not in deployed_footage_scs]

        common_keys = Key.objects.filter(common=True)

        for i, sc in enumerate(shortcodes):
            print(i)
            ftg = Footage.objects.get(shortcode=sc)
            guess_keys = guess_keys_by_tags(ftg.tags.split(' '))
            keys = []
            keys.extend(common_keys)
            keys.extend(guess_keys)
            tags_blocks = get_tags(keys)
            tags_text = "<br/><br/>".join(tags_blocks)
            p = Post(footage=ftg, tags=tags_text, text="by @"+ftg.author.nickname)
            p.approved = True
            p.save()

        #common_keys = [k.name for k in Key.objects.filter(common=True)]
        
        texts={}
        with open('feed.html', 'w') as f:
            print('file is open')
            posts = Post.objects.all()
            f.write('<html><head></head><body>')
            for i, p in enumerate(posts):
                print('making post', i)
                f.write('<div>')
                f.write('<h3>%d.</h3><img src="%s" width=300><p>%s</p><p>%s</p><p><i>%s</i></p>' % (p.id, p.footage.path, p.text, p.tags,  p.footage.text))
                f.write('</div>')
                status = subprocess.call('cp %s %s' % (p.footage.path, RES_FOLDER+'/'+str(p.id)+'.jpg'), shell=True)
                texts[str(p.id)]= "\n\n".join([p.text, p.tags, p.footage.text])
            f.write('</body></html>')

        for k,v in texts.items():
            with open(RES_FOLDER+'/%s.txt' % k, 'w') as f:
                f.write(v.replace('<br/>', '\n'))

