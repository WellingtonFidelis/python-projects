from django.contrib import admin
from core.models import Role, Employee, Service


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