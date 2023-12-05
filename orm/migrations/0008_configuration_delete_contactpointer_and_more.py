# Generated by Django 4.2.6 on 2023-12-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm", "0007_connectedaccount_is_active_contact_is_active_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pointer", models.IntegerField(default=0, editable=False)),
                ("max_limit_per_day", models.IntegerField(default=50)),
            ],
            options={
                "verbose_name": "Configuration",
                "verbose_name_plural": "Configurations",
            },
        ),
        migrations.DeleteModel(
            name="ContactPointer",
        ),
        migrations.AlterModelOptions(
            name="connectedaccount",
            options={
                "verbose_name": "Connected Account",
                "verbose_name_plural": "Connected Accounts",
            },
        ),
    ]
