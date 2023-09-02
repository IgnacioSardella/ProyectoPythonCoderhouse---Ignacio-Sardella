from django.urls import include, path
from .views import *

from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', home, name="home"),
    path('about_me', aboutPage, name="about_me"),
    
    path('cursos/', CursoList.as_view(), name="cursos"),
    path("create_curso/", CursoCreate.as_view(), name="create_curso"),
    path("update_curso/<int:pk>/", CursoUpdate.as_view(), name="update_curso"),
    path("delete_curso/<int:pk>/", CursoDelete.as_view(), name="delete_curso"),
    path("buscar_curso/", buscarCurso, name="buscar_curso"),
    path("buscar2/", buscar2, name="buscar2"),
    
    path('carreras/', CarreraList.as_view(), name='carreras'),
    path("create_carrera/", CarreraCreate.as_view(), name="create_carrera"),
    path('update_carrera/<int:pk>/', CarreraUpdate.as_view(), name='update_carrera'),
    path('delete_carrera/<int:pk>/', CarreraDelete.as_view(), name='delete_carrera'),
    path("buscar_carrera/", buscarCarrera, name="buscar_carrera"),
    path("buscarCarrera2/", buscarCarrera2, name="buscarCarrera2"),
    
    path('estudiantes/', EstudianteList.as_view(), name='estudiantes'),
    path("create_estudiante/", EstudianteCreate.as_view(), name="create_estudiante"),
    path('update_estudiante/<int:pk>/', EstudianteUpdate.as_view(), name='update_estudiante'),
    path('delete_estudiante/<int:pk>/', EstudianteDelete.as_view(), name='delete_estudiante'),
    path("buscar_estudiante/", buscarEstudiante, name="buscar_estudiante"),
    path("buscar_estudiante2/", buscarEstudiante2, name="buscar_estudiante2"),
    
    path('profesores/', ProfesorList.as_view(), name='profesores'),
    path("create_profesor/", ProfesorCreate.as_view(), name="create_profesor"),
    path('update_profesor/<int:pk>/', ProfesorUpdate.as_view(), name='update_profesor'),
    path('delete_profesor/<int:pk>/', ProfesorDelete.as_view(), name='delete_profesor'),
    path('buscar_profesor/', buscarProfesor, name="buscar_profesor"),
    path('buscar_profesor2/', buscarProfesor2, name="buscar_profesor2"),
    
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="aplication/logout.html"), name="logout"),
    path("registro/", register, name="registro"),
    path("editar_perfil/", editarPerfil, name="editar_perfil"),
    path("agregar_avatar/", agregarAvatar, name="agregar_avatar"),
    
    

]
