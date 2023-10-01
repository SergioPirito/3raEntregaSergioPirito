from django.urls import path
from .views import proyecto_view, productora_view, autor_view, productor_view
from .views import lista_proyecto, lista_productor, lista_productora, lista_autor
from .views import inicio, vista_proyecto, vista_productor, vista_productora, vista_autor, formulario_proyecto,formulario_autores, formulario_productores, formulario_productoras, proyecto_detalles
from .views import editar_proyecto, eliminar_proyecto

app_name = 'AppElevator'
urlpatterns = [
    path('agregar-proyecto/<nombre>/<logline>/<plot>/<genero>/',proyecto_view),
    path('agregar-productora/<nombre>/<pag_web>/<email>/<pais>/',productora_view),
    path('agregar-autor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/',autor_view),
    path('agregar-productor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/',productor_view),
    path('lista-productor/',lista_productor),
    path('lista-proyecto/', lista_proyecto, name='lista_proyecto'),
    path('proyecto-detalles/<nombre>/', proyecto_detalles),
    path('lista-productora/',lista_productora),
    path('lista-autor/',lista_autor),
    path('', inicio),
    path('vista-autor/',vista_autor),
    path('vista-productor/',vista_productor),
    path('vista-productora/',vista_productora),
    path('vista-proyecto/',vista_proyecto),
    path('formulario-proyecto/',formulario_proyecto, name= 'formularioProyecto'),
    path('formulario-autores/',formulario_autores, name= 'formularioAutores'),
    path('formulario-productores/',formulario_productores, name= 'formularioProductores'),
    path('formulario-productoras/',formulario_productoras, name= 'formularioProductoras'),
    path('editar-proyecto/<nombre>/', editar_proyecto, name='editarProyecto'),
    path('eliminar-proyecto/<nombre>/', eliminar_proyecto, name='eliminarProyecto'),
    
    


]
