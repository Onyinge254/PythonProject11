# Generated by Django 4.2.4 on 2023-08-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAL_INSIGHTS', '0002_alter_files_account_number_alter_files_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]