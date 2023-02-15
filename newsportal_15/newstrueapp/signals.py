from django.shortcuts import render, reverse, redirect
from django.dispatch import receiver
from django.core.mail import send_mail, mail_managers
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string

from .models import Post, User, PostCathegory, SubscribersCathegory
from newstrue import settings

def post_for_subscribers(title, text, subscribers_email,):
    for i in subscribers_email:
        html_content = render_to_string('post_for_subscribers.html')
        message = EmailMultiAlternatives(
            subject=title,
            body=text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to= i
            )
        message.attach_alternative(html_content, "text/html")  # добавляем htm
        message.send()

@receiver(m2m_changed, sender=PostCathegory)
def send_post_for_subscribers(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        cathegories = list(PostCathegory.objects.filter(post=instance.id).
                            values('cathegory'))
        subscribers_list = []
        for cathegory in cathegories:
            subscribers_all = list(SubscribersCathegory.objects.filter(cathegory=cathegory['cathegory']).values
                               ('subscriber__username',
                                'subscriber__email'))
            for person in subscribers_list:
                subscribers_list.append(person.subscriber__email)
            post_for_subscribers(instance.head_post, instance.text_post, subscribers_list)
