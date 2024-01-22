# Generated by Django 5.0.1 on 2024-01-07 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lekarze', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiadomosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.TextField(verbose_name='Treść')),
                ('data_wyslania', models.DateTimeField(auto_now_add=True)),
                ('konsultacja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wiadomosci', to='lekarze.konsultacja')),
                ('nadawca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
