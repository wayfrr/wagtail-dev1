# Generated by Django 3.2.7 on 2021-09-21 08:14

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogauthorsorderable_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]
