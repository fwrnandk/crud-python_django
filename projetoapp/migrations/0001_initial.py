# Generated by Django 5.0.2 on 2024-02-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('sobrenome', models.TextField()),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
