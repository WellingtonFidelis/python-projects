from django.contrib import admin
from core.models import Role, Employee, Service, Feature


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
  list_display = (
    'role',
    'is_active',
    'modified',    
  )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = (
    'service',
    'icon',
    'is_active',
    'modified'
  )
  
  
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'role',
    'is_active',
    'modified'
  )
  

@admin.register(Feature)
class ServiceAdmin(admin.ModelAdmin):
  list_display = (
    'feature',
    'icon',
    'is_active',
    'modified'
  )