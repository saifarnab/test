# Generated by Django 4.2.6 on 2024-01-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0003_followupemail_tag_followupemail_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailvariant",
            name="tag",
            field=models.CharField(
                choices=[
                    ("tag1", "tag1"),
                    ("tag2", "tag2"),
                    ("tag3", "tag3"),
                    ("tag4", "tag4"),
                    ("tag5", "tag5"),
                ],
                max_length=100,
            ),
        ),
    ]
