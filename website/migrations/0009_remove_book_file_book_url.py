# Generated by Django 5.0 on 2024-10-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0008_alter_clubabout_club_alter_teammember_club"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="file",
        ),
        migrations.AddField(
            model_name="book",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
