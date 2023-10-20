# Generated by Django 4.2.6 on 2023-10-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.CharField(choices=[('I', 'Info'), ('SC', 'Suspension clases'), ('SA', 'Suspension actividades')], default='I', max_length=5),
        ),
    ]