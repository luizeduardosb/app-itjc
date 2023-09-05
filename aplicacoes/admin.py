from django.contrib import admin

from .models import Edital
from .models import Empresa

admin.site.register(Edital)
admin.site.register(Empresa)