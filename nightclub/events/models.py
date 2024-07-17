from django.db import models

class Eveniment(models.Model):
    titlu = models.CharField(max_length=200)
    descriere = models.TextField()
    data = models.DateField()
    ora = models.TimeField()
    pret_bilet = models.DecimalField(max_digits=8, decimal_places=2)
    dj_artisti_invitati = models.CharField(max_length=200)

    def __str__(self):
        return self.titlu

from django.db import models

class Contact(models.Model):
    nume = models.CharField(max_length=100)
    email = models.EmailField()
    mesaj = models.TextField()
    data_trimiterii = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nume

from django.db import models

class Rezervare(models.Model):
    nume_utilizator = models.CharField(max_length=100)
    data_rezervarii = models.DateField()
    zona_rezervata = models.CharField(max_length=100)
    numar_persoane = models.IntegerField()
    status_rezervare = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nume_utilizator} - {self.data_rezervarii}"

from django.db import models

class Membru(models.Model):
    nume = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    descriere = models.TextField()
    email = models.EmailField()
    fotografie = models.ImageField(upload_to='membri', blank=True)

    def __str__(self):
        return self.nume

from django.db import models

class Mesaj(models.Model):
    continut = models.TextField()
    data_trimiterii = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.continut[:50]


