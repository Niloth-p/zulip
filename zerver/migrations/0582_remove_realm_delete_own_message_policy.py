# Generated by Django 5.0.7 on 2024-09-09 12:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0581_alter_realm_can_delete_own_message_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="delete_own_message_policy",
        ),
    ]