# Generated by Django 4.2.6 on 2023-12-14 08:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0014_contact_is_unsubscribe_contact_unsubscribe_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailvariant",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]