from django.shortcuts import render, redirect
from .models import curso
from .forms import CursoForm
from django.shortcuts import render, get_object_or_404, redirect


# Vista para listar los cursos
def get_curso(request):
    cursos = curso.objects.all()
    return render(request, 'lista_cursos.html', {
        'title': 'Lista de cursos',
        'cursos': cursos,
    })

# Vista para agregar o editar cursos
def formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo curso
            return redirect('lista-cursos')  # Redirige a la página de lista de cursos después de guardar
    else:
        form = CursoForm()

    return render(request, 'formulario_curso.html', {'form': form})

#Vista para eliminar un curso

def eliminar_curso(request, id):
    estudiante = get_object_or_404(curso, id=id)
    estudiante.delete()
    return redirect('lista-cursos')