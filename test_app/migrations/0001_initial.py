# Generated by Django 4.2.4 on 2023-08-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='files/employees/%(slug)s')),
                ('cv', models.FileField(upload_to='files/employees/%(slug)s')),
            ],
        ),
    ]
