from django.contrib import admin

from .models import Edital
from .models import Empresa
from .models import Email
from .models import Processos

admin.site.register(Edital)
admin.site.register(Empresa)
admin.site.register(Email)
admin.site.register(Processos)
