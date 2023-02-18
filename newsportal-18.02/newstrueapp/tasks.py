from celery import shared_task
from .signals import post_for_subscribers
from .models import PostCathegory, SubscribersCathegory
from newstrue import settings

import datetime
import time
import datetime

@shared_task
def send_post_for_subscribers_celery(post_pk):
    cathegories = list(PostCathegory.objects.filter(id = post_pk).
                             values('cathegory'))
    subscribers_all = []
    for cathegory in cathegories:
        subscribers_all += (SubscribersCathegory.objects.filter(cathegory=cathegory['cathegory']).values
                            ('subscribers__username',
                            'subscribers__email'
                              ))
        subscribers_list = []
        for person in subscribers_all:
            subscribers_list.append(person['subscribers__email'])
            post_for_subscribers(person['subscribers__email'], post.head_post, post.text_post[:50], subscribers_list, post.pk)


