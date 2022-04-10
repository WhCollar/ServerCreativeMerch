# Generated by Django 4.0.3 on 2022-04-09 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_size_merch_price_merch_category_merch_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='size',
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(null=True)),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.merch')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.size')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
                'ordering': ['id'],
            },
        ),
    ]