from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Paciente


class PacienteForm(forms.ModelForm):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Roedor', 'Roedor'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]

    especie = forms.ChoiceField(
        choices=ESPECIES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Paciente
        fields = ['dueno', 'mascota', 'especie', 'fecha_nacimiento', 'peso', 'unidad_peso', 'esterilizado']
        widgets = {
            'dueno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del dueno'}),
            'mascota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidad_peso': forms.Select(attrs={'class': 'form-select'}),
            'esterilizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def _contiene_letra(self, valor):
        return any(char.isalpha() for char in valor)

    def clean(self):
        cleaned_data = super().clean()
        dueno = (cleaned_data.get('dueno') or '').strip()
        mascota = (cleaned_data.get('mascota') or '').strip()

        if dueno and mascota and dueno.lower() == mascota.lower():
            raise ValidationError("El nombre del dueno y de la mascota no pueden ser iguales.")

        return cleaned_data

    def clean_dueno(self):
        dueno = (self.cleaned_data.get('dueno') or '').strip()
        if not dueno:
            raise ValidationError("El nombre del dueno no puede estar vacio.")
        if not self._contiene_letra(dueno):
            raise ValidationError("El nombre del dueno debe contener al menos una letra.")
        return dueno

    def clean_mascota(self):
        mascota = (self.cleaned_data.get('mascota') or '').strip()
        if not mascota:
            raise ValidationError("El nombre de la mascota no puede estar vacio.")
        if not self._contiene_letra(mascota):
            raise ValidationError("El nombre de la mascota debe contener al menos una letra.")
        return mascota

    def clean_especie(self):
        especie = (self.cleaned_data.get('especie') or '').strip()
        if not especie:
            raise ValidationError("La especie no puede estar vacia.")
        if len(especie) < 2:
            raise ValidationError("La especie debe tener al menos 2 caracteres.")
        if not self._contiene_letra(especie):
            raise ValidationError("La especie debe contener al menos una letra.")
        return especie

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso <= 0:
            raise ValidationError("El peso debe ser un valor positivo mayor a cero.")
        return peso

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > timezone.localdate():
            raise ValidationError("La fecha de nacimiento no puede ser futura.")
        return fecha_nacimiento
