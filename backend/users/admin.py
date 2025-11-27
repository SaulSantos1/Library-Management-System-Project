from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ProfileType

@admin.register(User)
class UserAdm(UserAdmin):
    list_display = ('username', 'full_name', 'profile_type', 'email', 'is_staff', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('full_name', 'email')}),
        ('Permissões', {'fields': ('profile_type','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    search_fields = ('username', 'full_name', 'email')
    
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'full_name', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password1') and not change:
            obj.set_password(form.cleaned_data['password1']) 
        super().save_model(request, obj, form, change)

admin.site.register(ProfileType)