from django.contrib import admin
from gaming_patrada.models import *


#model views

class PageAdmin(admin.ModelAdmin):
    list_display = ['name','category','release']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Games,PageAdmin)
admin.site.register(Letters)

