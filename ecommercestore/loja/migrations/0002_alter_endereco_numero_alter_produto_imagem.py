# Generated by Django 5.1.3 on 2024-12-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
