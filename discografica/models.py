from django.db import models
from django.utils import timezone


class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    letra = models.TextField()

    def __str__(self):
        return self.titulo


class Estilo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista)
    titulo = models.CharField(max_length=100)
    fecha = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="static/img/album", default="static/img/no-album.png")

    def __str__(self):
        return self.titulo + " (" + str(self.fecha) + ")"


class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album)
    cancion = models.ForeignKey(Cancion)
    visitas = models.PositiveIntegerField(default=0)
    upload_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        unique_together = ("id", "album", "cancion")

    def __str__(self):
        return str(self.cancion) + " (" + str(self.album.artista) + ")" + " (" + str(self.album.fecha) + ")"
