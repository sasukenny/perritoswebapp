# Generated by Django 4.0.3 on 2022-03-24 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perritos', '0012_remove_perrito_likes_alter_perrito_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='hired_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('symptoms_priori', models.TextField(blank=True, null=True)),
                ('perrito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perritos.perrito')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.service')),
            ],
        ),
    ]