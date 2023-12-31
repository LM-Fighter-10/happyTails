# Generated by Django 4.2 on 2023-12-17 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webApp", "0003_client_name_vet_first_name_vet_last_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="name",
            new_name="first_name",
        ),
        migrations.RenameField(
            model_name="vet",
            old_name="first_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="vet",
            name="last_name",
        ),
        migrations.AddField(
            model_name="client",
            name="last_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]
