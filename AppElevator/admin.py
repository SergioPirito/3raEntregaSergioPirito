from django.contrib import admin
from .models import autor
from .models import productora_audiovisual
from .models import Proyecto
from .models import productor
# Register your models here.
admin.site.register(autor)
admin.site.register(productora_audiovisual)
admin.site.register(Proyecto)
admin.site.register(productor)