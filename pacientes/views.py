from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PacienteForm
from .models import Paciente


def index(request):
    query = request.GET.get('q', '').strip()
    if query:
        pacientes = Paciente.objects.filter(
            Q(mascota__iexact=query) | Q(dueno__iexact=query)
        )
    else:
        pacientes = Paciente.objects.all()

    return render(request, 'pacientes/index.html', {'pacientes': pacientes, 'query': query})


def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form_paciente.html', {'form': form})


def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form_paciente.html', {'form': form})


@permission_required('pacientes.delete_paciente', raise_exception=True)
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('index')
    return render(request, 'pacientes/confirm_delete.html', {'paciente': paciente})
