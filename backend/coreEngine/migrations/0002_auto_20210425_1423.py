# Generated by Django 3.2 on 2021-04-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreEngine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='down_votes_total',
            field=models.SmallIntegerField(blank=True, default=0, help_text='To store a total of all the Down-votes received.', null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='up_votes_total',
            field=models.SmallIntegerField(blank=True, default=0, help_text='To store a total of all the Up-votes received.', null=True),
        ),
    ]
