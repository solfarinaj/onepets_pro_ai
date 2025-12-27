from django.core.exceptions import ValidationError
from django.db import models


class Paciente(models.Model):
    UNIDADES_PESO = [
        ('k', 'Kilogramos'),
        ('g', 'Gramos'),
    ]

    dueno = models.CharField(max_length=100, verbose_name="Nombre del dueno")
    mascota = models.CharField(max_length=100, verbose_name="Nombre de la mascota")
    especie = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    peso = models.FloatField()
    unidad_peso = models.CharField(max_length=1, choices=UNIDADES_PESO, default='k')
    esterilizado = models.BooleanField(default=False)
    fecha_registro = models.DateField(auto_now_add=True)

    def clean(self):
        dueno = (self.dueno or '').strip()
        mascota = (self.mascota or '').strip()

        if dueno and mascota and dueno.lower() == mascota.lower():
            raise ValidationError("El nombre del dueno y de la mascota no pueden ser iguales.")

        if self.peso is not None and self.peso <= 0:
            raise ValidationError("El peso debe ser un valor positivo mayor a cero.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.mascota} ({self.dueno})"
