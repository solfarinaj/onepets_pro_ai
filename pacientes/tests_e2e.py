import os

import pytest


BASE_URL = os.getenv("E2E_BASE_URL", "http://127.0.0.1:8000")


@pytest.mark.e2e
def test_registro_exitoso(page):
    page.goto(f"{BASE_URL}/crear/")

    page.get_by_label("Nombre del dueno").fill("Ana Lopez")
    page.get_by_label("Nombre de la mascota").fill("Roco")
    page.get_by_label("Especie").select_option("Perro")
    page.get_by_label("Fecha de nacimiento").fill("2020-05-12")
    page.get_by_label("Peso").fill("12.5")
    page.get_by_label("Unidad peso").select_option("k")
    page.get_by_label("Esterilizado").check()

    page.get_by_role("button", name="Guardar Paciente").click()

    page.wait_for_url(f"{BASE_URL}/")
    assert page.get_by_text("Roco").is_visible()


@pytest.mark.e2e
def test_error_peso_cero(page):
    page.goto(f"{BASE_URL}/crear/")

    page.get_by_label("Nombre del dueno").fill("Luis Perez")
    page.get_by_label("Nombre de la mascota").fill("Mika")
    page.get_by_label("Especie").select_option("Gato")
    page.get_by_label("Peso").fill("0")
    page.get_by_label("Unidad peso").select_option("k")

    page.get_by_role("button", name="Guardar Paciente").click()

    assert page.get_by_text("El peso debe ser un valor positivo mayor a cero.").is_visible()


@pytest.mark.e2e
def test_error_dueno_y_mascota_iguales(page):
    page.goto(f"{BASE_URL}/crear/")

    page.get_by_label("Nombre del dueno").fill("Luna")
    page.get_by_label("Nombre de la mascota").fill("Luna")
    page.get_by_label("Especie").select_option("Perro")
    page.get_by_label("Peso").fill("8")
    page.get_by_label("Unidad peso").select_option("k")

    page.get_by_role("button", name="Guardar Paciente").click()

    assert page.get_by_text(
        "El nombre del dueno y de la mascota no pueden ser iguales."
    ).is_visible()


@pytest.mark.e2e
def test_busqueda_exacta_por_nombre(page):
    page.goto(f"{BASE_URL}/crear/")

    page.get_by_label("Nombre del dueno").fill("Sofia Gomez")
    page.get_by_label("Nombre de la mascota").fill("Nina")
    page.get_by_label("Especie").select_option("Gato")
    page.get_by_label("Peso").fill("4.2")
    page.get_by_label("Unidad peso").select_option("k")

    page.get_by_role("button", name="Guardar Paciente").click()
    page.wait_for_url(f"{BASE_URL}/")

    page.get_by_placeholder("Buscar por nombre de mascota o dueno...").fill("Nina")
    page.get_by_role("button", name="Buscar").click()

    assert page.get_by_text("Nina").is_visible()
