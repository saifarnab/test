# Generated by Django 4.2.6 on 2023-12-13 04:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailvariant",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
