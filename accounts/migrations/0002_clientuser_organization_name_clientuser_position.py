# Generated by Django 4.0.3 on 2022-03-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientuser',
            name='organization_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientuser',
            name='position',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]