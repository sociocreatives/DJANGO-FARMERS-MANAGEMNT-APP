# Generated by Django 3.1.4 on 2021-04-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilosahihi', '0002_auto_20210423_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfarmers',
            name='contact',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userfarmers',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userfarmers',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userfarmers',
            name='status',
            field=models.CharField(default='NotRegistered', max_length=10),
        ),
    ]
