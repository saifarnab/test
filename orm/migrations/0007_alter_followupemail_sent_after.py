# Generated by Django 4.2.6 on 2023-12-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0006_followupemail_sent_after_sentemail_is_followup_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followupemail",
            name="sent_after",
            field=models.PositiveSmallIntegerField(
                default=1,
                help_text="this followup email will sent after specified day from the original email",
                unique=True,
            ),
        ),
    ]