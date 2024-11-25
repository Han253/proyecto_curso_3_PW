# Generated by Django 5.1.3 on 2024-11-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_created=True)),
                ('modelo', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=50)),
                ('valor', models.BigIntegerField()),
            ],
        ),
    ]
