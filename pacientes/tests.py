from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import PacienteForm
from .models import Paciente


class PacienteFormValidationsTests(TestCase):
    def _valid_payload(self):
        return {
            'dueno': 'Ana Lopez',
            'mascota': 'Roco',
            'especie': 'Perro',
            'fecha_nacimiento': '2020-05-12',
            'peso': '12.5',
            'unidad_peso': 'k',
            'esterilizado': 'on',
        }

    def test_dueno_requiere_letras(self):
        data = self._valid_payload()
        data['dueno'] = '1234'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('dueno', form.errors)

    def test_mascota_requiere_letras(self):
        data = self._valid_payload()
        data['mascota'] = '5678'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('mascota', form.errors)

    def test_especie_minimo_dos_caracteres(self):
        data = self._valid_payload()
        data['especie'] = 'A'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('especie', form.errors)

    def test_especie_requiere_letras(self):
        data = self._valid_payload()
        data['especie'] = '12'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('especie', form.errors)

    def test_error_peso_menor_o_igual_cero(self):
        data = self._valid_payload()
        data['peso'] = '0.0'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('peso', form.errors)

    def test_error_dueno_y_mascota_iguales(self):
        data = self._valid_payload()
        data['dueno'] = 'Luna'
        data['mascota'] = 'Luna'

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_error_fecha_nacimiento_futura(self):
        data = self._valid_payload()
        data['fecha_nacimiento'] = (timezone.localdate() + timedelta(days=1)).isoformat()

        form = PacienteForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('fecha_nacimiento', form.errors)


class PacienteViewsTests(TestCase):
    def _valid_payload(self):
        return {
            'dueno': 'Ana Lopez',
            'mascota': 'Roco',
            'especie': 'Perro',
            'fecha_nacimiento': '2020-05-12',
            'peso': '12.5',
            'unidad_peso': 'k',
            'esterilizado': 'on',
        }

    def test_registro_exitoso(self):
        response = self.client.post(reverse('crear_paciente'), data=self._valid_payload())

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Paciente.objects.count(), 1)
        self.assertEqual(Paciente.objects.first().mascota, 'Roco')

    def test_busqueda_por_nombre_mascota_o_dueno(self):
        Paciente.objects.create(
            dueno='Sofia Gomez',
            mascota='Nina',
            especie='Gato',
            fecha_nacimiento='2021-01-10',
            peso=4.2,
            unidad_peso='k',
            esterilizado=True,
        )

        response_mascota = self.client.get(reverse('index'), {'q': 'Nina'})
        self.assertEqual(response_mascota.status_code, 200)
        self.assertContains(response_mascota, 'Nina')

        response_dueno = self.client.get(reverse('index'), {'q': 'Sofia Gomez'})
        self.assertEqual(response_dueno.status_code, 200)
        self.assertContains(response_dueno, 'Sofia')
