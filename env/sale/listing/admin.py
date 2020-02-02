from django.contrib import admin
from.models import Item
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title',)
admin.site.register(Item,PostAdmin)