# Generated by Django 3.2 on 2021-04-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fouroperations',
            name='select',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
