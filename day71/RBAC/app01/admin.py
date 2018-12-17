from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.User2Role)
admin.site.register(models.Role)
admin.site.register(models.Action)
admin.site.register(models.Permission)
admin.site.register(models.Permission2Action)
admin.site.register(models.Permission2Action2Role)
admin.site.register(models.Menu)

#python manager.py createsuperuser
#root
#root!2345