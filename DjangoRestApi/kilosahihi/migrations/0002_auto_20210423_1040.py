# Generated by Django 3.1.4 on 2021-04-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilosahihi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerstransactions',
            name='net_weight',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smallholderestatetransactions',
            name='net_weight',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
