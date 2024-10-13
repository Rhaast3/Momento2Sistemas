from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

# Vista para listar estudiantes
def get_estudiantes(request):
    estudiantes = Persona.objects.filter(rol='Estudiante')
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

# Vista para agregar nuevos estudiantes
def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)  # No guardar aún en la base de datos
            estudiante.rol = 'Estudiante'  # Asignar el rol predeterminado
            estudiante.save()  # Ahora guarda el estudiante
            return redirect('lista-estudiantes')  # Redirige a la lista de estudiantes después de guardar
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiante.html', {'form': form})

def eliminar_estudiante(request, dni):
    estudiante = get_object_or_404(Persona, dni=dni)
    estudiante.delete()
    return redirect('lista-estudiantes')