# Generated by Django 4.2.3 on 2023-07-08 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_userfile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='utilisateur',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_files', to='dashboard.utilisateur'),
        ),
    ]
