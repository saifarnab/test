# Generated by Django 4.2.6 on 2023-12-13 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0011_rename_email_variant_sentemail_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="sentemail",
            name="followup_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="orm.followupemail",
            ),
        ),
    ]