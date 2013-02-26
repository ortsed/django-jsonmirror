from django.contrib import admin
from jsonmirror.models import JSON_Archive, JSON_Archive_Set

class JSON_Archive_Set_Admin(admin.ModelAdmin):
	pass

class JSON_Archive_Admin(admin.ModelAdmin):

	pass


admin.site.register(JSON_Archive_Set, JSON_Archive_Set_Admin)
admin.site.register(JSON_Archive, JSON_Archive_Admin)