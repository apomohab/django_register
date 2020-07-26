from django.contrib import admin

#profile

from  .models import profile

# Register your models here.

@admin.register(profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']