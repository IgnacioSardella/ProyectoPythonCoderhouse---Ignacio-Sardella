import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Avatar, Curso, Carrera, Estudiante, Profesor
from .forms import AvatarForm, RegistroUsuariosForm, UserEditForm
# Create your views here.

def home(request):
    return render(request, 'aplication/home.html')

def aboutPage(request):
    return render(request, 'aplication/aboutme.html')

'''
login function
'''

def login_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username = usuario, password = password)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default-avatar.png"
                finally:
                    request.session["avatar"] = avatar
                
                return render(request, "aplication/base.html")
            else:
                return render(request, "aplication/login.html", {'form': miForm})
        else:
            return render(request, "aplication/login.html", {'form': miForm})    
    else:
        miForm = AuthenticationForm()
        return render(request, "aplication/login.html", { "form": miForm} )

'''
register
'''

def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplication/base.html")
    else:
        miForm = RegistroUsuariosForm()
    return render(request, "aplication/registro.html", { "form": miForm} )


'''
editar perfil
'''

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, 'aplication/base.html')
        else:
            return render(request, 'aplication/editarPerfil.html', {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, 'aplication/editarPerfil.html', {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, 'aplication/base.html')
    else:
        form = AvatarForm()
    return render(request, 'aplication/agregarAvatar.html', {'form': form})


'''
funciones para agregar y buscar cursos
'''

class CursoList(LoginRequiredMixin, ListView):
    model = Curso

class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ['nombre', 'comision']
    success_url = reverse_lazy('cursos')

class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ['nombre', 'comision']
    template_name = 'aplication/curso_update_form.html'
    success_url = reverse_lazy('cursos')

class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')

@login_required
def buscarCurso(request):
    return render(request, 'aplication/buscarCurso.html')

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cursos = Curso.objects.filter(nombre__icontains=patron)
        if len(cursos) == 0:
            messages.warning(request, 'No se encontró ningún curso con tu patrón de búsqueda.')
            return HttpResponseRedirect(reverse('cursos'))
        else:
            contexto = {'curso_list': cursos}
            return render(request, 'aplication/curso_list.html', contexto)
    messages.warning(request, 'No se ingreso nada en el buscador')
    return HttpResponseRedirect(reverse('buscar_curso'))

'''
funciones para agregar y buscar carreras
'''

class CarreraList(LoginRequiredMixin, ListView):
    model = Carrera

class CarreraCreate(LoginRequiredMixin, CreateView):
    model = Carrera
    fields = ['comision', 'nombre', 'duracion']
    success_url = reverse_lazy('carreras')

class CarreraUpdate(LoginRequiredMixin, UpdateView):
    model = Carrera
    fields = ['comision', 'nombre', 'duracion']
    template_name = 'aplication/carrera_update_form.html'
    success_url = reverse_lazy('carreras')

class CarreraDelete(LoginRequiredMixin, DeleteView):
    model = Carrera
    success_url = reverse_lazy('carreras')

@login_required
def buscarCarrera(request):
    return render(request, 'aplication/buscarCarrera.html')

@login_required
def buscarCarrera2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        carreras = Carrera.objects.filter(nombre__icontains=patron)
        if len(carreras) == 0:
            messages.warning(request, 'No se encontró ningúna carrera con tu patrón de búsqueda.')
            return HttpResponseRedirect(reverse('carreras'))
        else:
            contexto = {'carrera_list': carreras}
            return render(request, 'aplication/carrera_list.html', contexto)
    messages.warning(request, 'No se ingreso nada en el buscador')
    return HttpResponseRedirect(reverse('buscar_carrera'))

'''
funciones para agregar y buscar profesores
'''

class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante

class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')

class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    template_name = 'aplication/estudiante_update_form.html'
    success_url = reverse_lazy('estudiantes')

class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')

@login_required
def buscarEstudiante(request):
    return render(request, 'aplication/buscarEstudiante.html')

@login_required
def buscarEstudiante2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        estudiantes = Estudiante.objects.filter(nombre__icontains=patron)
        if len(estudiantes) == 0:
            messages.warning(request, 'No se encontró ningún estudiante con tu patrón de búsqueda.')
            return HttpResponseRedirect(reverse('estudiantes'))
        else:
            contexto = {'estudiante_list': estudiantes}
            return render(request, 'aplication/estudiante_list.html', contexto)
    messages.warning(request, 'No se ingreso nada en el buscador')
    return HttpResponseRedirect(reverse('buscar_estudiante'))

''' 
Funciones para Profesores
'''

class ProfesorList(LoginRequiredMixin, ListView):
    model = Profesor

class ProfesorCreate(LoginRequiredMixin, CreateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('profesores')

class ProfesorUpdate(LoginRequiredMixin, UpdateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email']
    template_name = 'aplication/profesor_update_form.html'
    success_url = reverse_lazy('profesores')

class ProfesorDelete(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')

@login_required
def buscarProfesor(request):
    return render(request, 'aplication/buscarProfesor.html')

@login_required
def buscarProfesor2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        profesores = Profesor.objects.filter(nombre__icontains=patron)
        if len(profesores) == 0:
            messages.warning(request, 'No se encontró ningún profesor con tu patrón de búsqueda.')
            return HttpResponseRedirect(reverse('profesores'))
        else:
            contexto = {'profesor_list': profesores}
            return render(request, 'aplication/profesor_list.html', contexto)
    messages.warning(request, 'No se ingreso nada en el buscador')
    return HttpResponseRedirect(reverse('buscar_profesor'))