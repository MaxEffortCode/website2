from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
class ItemInline(admin.TabularInline):
	model = Item
	extra = 3




class ItemAdmin(admin.ModelAdmin):
	inlines = [ItemInline]
	list_filter = ['name']
	search_fields = ['name']
	list_display = ('name', 'user')

admin.site.register(ToDoList, ItemAdmin)
