from django.contrib import admin

from .models import Skills,Projects

# Register your models here.
@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
   pass
   

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
   pass
   
