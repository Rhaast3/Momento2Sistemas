from django.shortcuts import render, redirect
from .models import EstudianteCurso
from .forms import EstudianteCursoForm
from django.shortcuts import render, get_object_or_404, redirect


# Vista para listar los estudiantes y cursos
def Estudiante_Curso(request):
    estudianteCurso = EstudianteCurso.objects.all()  # Obtener todos los objetos EstudianteCurso
    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudianteCurso,
    })

# Vista para agregar o editar una relación de estudiante con curso
def formulario_estudiante_curso(request):
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario
            return redirect('lista-estudiantes-cursos')  # Asegúrate de que este nombre coincida
    else:
        form = EstudianteCursoForm()  # Formulario vacío si no es POST

    return render(request, 'formulario_estudiante_curso.html', {'form': form})

#Vista para eliminar un estudiante-curso

def eliminar_estudiante_curso(request, id):
    relacion = get_object_or_404(EstudianteCurso, id=id)
    relacion.delete()
    return redirect('lista-estudiantes-cursos')  

