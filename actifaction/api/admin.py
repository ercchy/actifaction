from django.contrib import admin


import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(models.ActionCategory)
admin.site.register(models.Action)
admin.site.register(models.UserProfile, UserProfileAdmin)
