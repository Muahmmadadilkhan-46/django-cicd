# Generated by Django 5.0.2 on 2024-03-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorprofile",
            name="profile_photo_url",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
