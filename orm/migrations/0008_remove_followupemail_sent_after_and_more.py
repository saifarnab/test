# Generated by Django 4.2.6 on 2023-12-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0007_alter_followupemail_sent_after"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followupemail",
            name="sent_after",
        ),
        migrations.AddField(
            model_name="followupemail",
            name="wait_for",
            field=models.PositiveSmallIntegerField(
                default=1,
                help_text="this followup email will wait specified day from the original email",
                unique=True,
            ),
        ),
    ]