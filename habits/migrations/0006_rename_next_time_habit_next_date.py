# Generated by Django 5.0 on 2024-07-13 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_habit_next_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="next_time",
            new_name="next_date",
        ),
    ]
