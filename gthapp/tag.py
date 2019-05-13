from random import sample
from operator import itemgetter
from gthapp.models import Tag, Key


def get_tags(keys):

    TAG_LIMIT = 90
    BLOCK_LIMIT = 30

    tags = []
    for k in keys:
        ktags = [(t.name, t.rating,) for t in k.tag_set.all()]
        tags.extend(ktags)

    tags = list(set(tags))

    smp = sorted(sample(tags, TAG_LIMIT), key=itemgetter(1), reverse=True)

    blocks = []
    i = 0
    while i < 90:
        blocks.append(smp[i:i+BLOCK_LIMIT])
        i += BLOCK_LIMIT

    res = []
    for b in blocks:
        res.append(' '.join(['#'+t[0] for t in b]))

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
