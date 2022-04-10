# Generated by Django 4.0.3 on 2022-04-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_merch_merch_size_num_merch_merch_size_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='merch_size_num',
        ),
        migrations.AddField(
            model_name='merchsizenum',
            name='merch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.merch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchsizenum',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size'),
        ),
    ]
