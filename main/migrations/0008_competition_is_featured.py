# Generated by Django 4.0.6 on 2022-09-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_branch_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
