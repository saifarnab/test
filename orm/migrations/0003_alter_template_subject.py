# Generated by Django 4.2.6 on 2023-12-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0002_remove_template_updated_at_alter_template_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="template",
            name="subject",
            field=models.CharField(max_length=1500),
        ),
    ]
