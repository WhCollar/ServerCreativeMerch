# Generated by Django 4.0.3 on 2022-04-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_basket_value_orders_basket_coast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='merch_size',
        ),
        migrations.AddField(
            model_name='orders',
            name='size_count',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchsizenum',
            name='merch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merch_size_num', to='main.merch'),
        ),
    ]
