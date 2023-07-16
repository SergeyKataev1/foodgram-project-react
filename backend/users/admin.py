from django.contrib import admin

from users.models import ExtendedUser, Subscribe


class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )


admin.site.register(ExtendedUser, ExtendedUserAdmin)
admin.site.register(Subscribe)
