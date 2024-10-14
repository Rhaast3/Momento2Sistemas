from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm  
from django.shortcuts import render, get_object_or_404, redirect
from curso.models import curso

def lista_matriculas(request):
    cursos = curso.objects.all()  # Asegúrate de que Curso está correctamente en mayúscula si ese es el nombre del modelo
    curso_seleccionado = request.GET.get('curso')  # Obtener el curso seleccionado desde el filtro

    if curso_seleccionado:
        matriculas = Matricula.objects.filter(estudiante_curso__curso=curso_seleccionado)  # Aplicar filtro por curso
    else:
        matriculas = Matricula.objects.all()  # Si no se seleccionó un curso, mostrar todas las matrículas

    return render(request, 'lista_matricula.html', {
        'title': 'Lista de Matrículas',
        'matriculas': matriculas,
        'cursos': cursos,
        'curso_seleccionado': curso_seleccionado  # Pasar el curso seleccionado para mantenerlo en el formulario
    })

# Vista para agregar o editar una matrícula
def formulario_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-matriculas')  
    else:
        form = MatriculaForm()  

    return render(request, 'formulario_matricula.html', {'form': form})

def eliminar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('lista-matriculas')