# Generated by Django 3.2.7 on 2021-10-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='product_image',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]