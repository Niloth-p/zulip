# Generated by Django 5.0.8 on 2024-08-31 08:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0582_remove_realm_delete_own_message_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="namedusergroup",
            name="creator",
            field=models.ForeignKey(
                db_column="creator_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="namedusergroup",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
