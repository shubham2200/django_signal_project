# Generated by Django 4.0.1 on 2022-01-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signal_history', '0002_remove_authenticate_history_records_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticate_history',
            name='recordstype',
            field=models.CharField(choices=[('reg', 'register'), ('li', 'login'), ('lo', 'logout')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]