# Generated by Django 5.0.7 on 2024-07-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mesaj', models.TextField()),
                ('data_trimiterii', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eveniment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=200)),
                ('descriere', models.TextField()),
                ('data', models.DateField()),
                ('ora', models.TimeField()),
                ('pret_bilet', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dj_artisti_invitati', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Membru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
                ('descriere', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('fotografie', models.ImageField(blank=True, upload_to='membri')),
            ],
        ),
        migrations.CreateModel(
            name='Mesaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continut', models.TextField()),
                ('data_trimiterii', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rezervare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_utilizator', models.CharField(max_length=100)),
                ('data_rezervarii', models.DateField()),
                ('zona_rezervata', models.CharField(max_length=100)),
                ('numar_persoane', models.IntegerField()),
                ('status_rezervare', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
