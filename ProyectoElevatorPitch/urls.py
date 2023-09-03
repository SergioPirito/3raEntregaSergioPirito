from django.contrib import admin
from django.urls import path
from AppElevator.views import proyecto_view
from AppElevator.views import productora_view
from AppElevator.views import autor_view
from AppElevator.views import productor_view, lista_productor
from AppElevator.views import lista_proyecto
from AppElevator.views import lista_productora
from AppElevator.views import lista_autor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar-proyecto/<nombre>/<logline>/<plot>/<genero>/', proyecto_view),
    path('agregar-productora/<nombre>/<pag_web>/<email>/<pais>/', productora_view),
    path('agregar-autor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/', autor_view),
    path('agregar-productor/<nombre>/<apellido>/<int:edad>/<email>/<pais>/', productor_view),
    path('lista-productor/', lista_productor),

    path('lista-proyecto/', lista_proyecto),
    path('lista-productora/', lista_productora),
    path('lista-autor/', lista_autor),
]



