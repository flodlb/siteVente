# Generated by Django 5.0.6 on 2024-05-29 09:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vetement',
            fields=[
                ('vetement_description', models.CharField(max_length=200)),
                ('qnte', models.IntegerField(null=True)),
                ('prix', models.IntegerField(null=True)),
                ('id_V', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id_P', models.AutoField(primary_key=True, serialize=False)),
                ('id_Commande', models.IntegerField(null=True)),
                ('id_U', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_V', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.vetement')),
            ],
        ),
    ]
