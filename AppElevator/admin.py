from django.contrib import admin
from .models import Autor
from .models import Productora_audiovisual
from .models import Proyecto
from .models import Productor

class ProyectoAdmin (admin.ModelAdmin):
    list_display = ['nombre', 'Autor',]
    search_fields = ['nombre']
    list_filter = ['nombre']
    


# Register your models here.
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Autor)
admin.site.register(Productora_audiovisual)
admin.site.register(Productor)