# Generated by Django 5.1.7 on 2025-04-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_midias_delete_cd_delete_disco'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCartao', models.CharField(max_length=16)),
                ('nomeTitular', models.CharField(max_length=150)),
                ('dataValidade', models.DateField()),
                ('codigoSeguranca', models.CharField(max_length=3)),
            ],
        ),
    ]
