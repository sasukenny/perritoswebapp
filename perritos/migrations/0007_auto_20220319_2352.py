# Generated by Django 3.2.4 on 2022-03-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perritos', '0006_rename_gender_perrito_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perrito',
            name='likes',
        ),
        migrations.AlterField(
            model_name='perrito',
            name='gender',
            field=models.BooleanField(),
        ),
    ]