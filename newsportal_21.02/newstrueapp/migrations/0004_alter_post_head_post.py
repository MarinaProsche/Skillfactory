# Generated by Django 4.1.5 on 2023-02-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstrueapp', '0003_subscriberscathegory_cathegory_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_post',
            field=models.TextField(null=True),
        ),
    ]