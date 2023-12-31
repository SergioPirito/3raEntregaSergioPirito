from django.urls import path
from .views import editar_perfil, agregar_avatar, register, logout_view
from .views import proyecto_view, productora_view, autor_view, productor_view
from .views import lista_proyecto, lista_productor, lista_productora, lista_autor
from .views import inicio, vista_proyecto, vista_productor, vista_productora, vista_autor
from .views import formulario_proyecto,formulario_autores, formulario_productores, formulario_productoras
from .views import proyecto_detalles, productor_detalles, productora_detalles,autor_detalles
from .views import editar_proyecto, eliminar_proyecto, editar_autor, eliminar_autor
from .views import editar_productor, eliminar_productor, editar_productora, eliminar_productora
from django.contrib.auth.views import LogoutView
from .views import login_view

app_name = 'AppElevator'
urlpatterns = [
    path('agregar-proyecto/<nombre>/<logline>/<plot>/<genero>/',proyecto_view),
    path('agregar-productora/<nombre>/<pag_web>/<email>/<pais>/',productora_view),
    path('agregar-autor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/',autor_view),
    path('agregar-productor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/',productor_view),
    
    # LISTAS 

    path('lista-productor/',lista_productor, name='lista_productor'),
    path('lista-proyecto/', lista_proyecto, name='lista_proyecto'),
    path('lista-productora/',lista_productora, name='lista_productora'),
    path('lista-autor/',lista_autor, name='lista_autor'),
    path('', inicio),
    
    # VISTAS
    path('vista-autor/',vista_autor),
    path('vista-productor/',vista_productor),
    path('vista-productora/',vista_productora),
    path('vista-proyecto/',vista_proyecto),
    
    # PRODUCTORES
    path('productor-detalles/<nombre>/', productor_detalles),

    path('formulario-productores/',formulario_productores, name= 'formularioProductores'),
    path('editar-productor/<nombre>/', editar_productor, name='editarProductor'),
    path('eliminar-productor/<nombre>/', eliminar_productor, name='eliminarProductor'),

    # PRODUCTORA AUDIOVISUAL
    path('productora-detalles/<nombre>/', productora_detalles),
    path('formulario-productoras/',formulario_productoras, name= 'formularioProductoras'),
    path('editar-productora/<nombre>/', editar_productora, name='editarProductora'),
    path('eliminar-productora/<nombre>/', eliminar_productora, name='eliminarProductora'),
    
    # PROYECTO
    path('proyecto-detalles/<nombre>/', proyecto_detalles),
    path('formulario-proyecto/',formulario_proyecto, name= 'formularioProyecto'),
    path('editar-proyecto/<nombre>/', editar_proyecto, name='editarProyecto'),
    path('eliminar-proyecto/<nombre>/', eliminar_proyecto, name='eliminarProyecto'),
    
    # AUTOR
    path('autor-detalles/<nombre>/', autor_detalles),
    path('formulario-autores/',formulario_autores, name= 'formularioAutores'),
    path('editar-autor/<nombre>/', editar_autor, name='editarAutor'),
    path('eliminar-autor/<nombre>/', eliminar_autor, name='eliminarAutor'),
    
    # REGISTRO
    path('login/', login_view, name='Login'),
    path('registrar/', register, name="Registrar"),
    path('logout/', logout_view, name='Logout'),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),

    # AVATAR
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),

    
]

