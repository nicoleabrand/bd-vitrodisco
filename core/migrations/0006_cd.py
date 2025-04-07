# Generated by Django 5.1.7 on 2025-04-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_disco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('tracks', models.IntegerField()),
                ('lancamento', models.DateField()),
                ('descricao', models.CharField(max_length=250)),
                ('preco', models.CharField(max_length=6)),
                ('estoque', models.IntegerField()),
            ],
        ),
    ]
