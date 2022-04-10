# Generated by Django 4.0.3 on 2022-04-09 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='merch',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='merch',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category'),
        ),
        migrations.AddField(
            model_name='merch',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.size'),
        ),
    ]
