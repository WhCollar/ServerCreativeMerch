# Generated by Django 4.0.3 on 2022-04-09 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_merchsizenum_delete_catalog_merch_merch_size_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='merch_size_num',
        ),
        migrations.AddField(
            model_name='merch',
            name='merch_size_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.merchsizenum'),
        ),
    ]