# Generated by Django 3.0.5 on 2020-04-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_ngo_table_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='reg_number',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
