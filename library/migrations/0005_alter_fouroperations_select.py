# Generated by Django 3.2 on 2021-04-28 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_fouroperations_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fouroperations',
            name='select',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')], max_length=1, null=True),
        ),
    ]
