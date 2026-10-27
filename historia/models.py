from django.db import models

class Escena(models.Model):
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=200)
    capitulo = models.CharField(max_length=100, blank=True)
    texto = models.TextField()
    es_final = models.BooleanField(default=False)
    clase_extra = models.CharField(max_length=50, blank=True)
    opciones = models.ManyToManyField(
        'self',
        through='Opcion',
        symmetrical=False,
        blank=True
    )


    def __str__(self):
        return self.titulo




class Opcion(models.Model):
    escena_origen = models.ForeignKey(Escena, on_delete=models.CASCADE,
                                      related_name='opciones_salida')
    escena_destino = models.ForeignKey(Escena, on_delete=models.CASCADE,
                                       related_name='opciones_entrada')
    texto_link = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.escena_origen} -> {self.escena_destino}"
