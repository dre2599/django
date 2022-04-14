# Generated by Django 4.0.4 on 2022-04-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clienti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('indirizzo', models.CharField(max_length=1024)),
                ('telefono', models.CharField(max_length=100)),
                ('agente', models.IntegerField()),
            ],
            options={
                'db_table': 'clienti',
                'managed': False,
            },
        ),
    ]
