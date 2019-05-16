from random import sample
from operator import itemgetter
from gthapp.models import Tag, Key


def get_tags(keys, **kwargs):

    blocks_num = kwargs.get('blocks', 3)
    BLOCK_LIMIT = 30
    tag_limit = blocks_num*BLOCK_LIMIT

    tags = []
    for k in keys:
        ktags = [(t.name, t.rating,) for t in k.tag_set.all()]
        tags.extend(ktags)

    tags = list(set(tags))

    smp = sorted(sample(tags, tag_limit), key=itemgetter(1), reverse=True)

    blocks = []
    i = 0

    while i < tag_limit:
        blocks.append(smp[i:i+BLOCK_LIMIT])
        i += BLOCK_LIMIT

    res = []
    for b in blocks:
        ratings = [t[1] for t in b]
        rmax = max(ratings)
        rmin = min(ratings)
        ravg = int(sum(ratings)/len(ratings))
        res.append({
            "text": ' '.join(['#'+t[0] for t in b]),
            "data": {
                "max": rmax,
                "min": rmin,
                "avg": ravg
            }
        })

    return res


def guess_keys_by_tags(tags):

    if tags:
        keys = []
        for t in tags:
            try:
                to = Tag.objects.get(name=t)
            except Tag.DoesNotExist:
                pass
            else:
                keys.append(to.key.name)
        res = []
        for k in list(set(keys)):
            key = Key.objects.get(name=k)
            res.append(key)
        return res
    else:
        return None
