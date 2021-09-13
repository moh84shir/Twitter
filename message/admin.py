from django.contrib import admin
from . import models

# Display model for site admin
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'from_user', 'time']

    class Meta:
        model = models.Messages


# Register models in site admin
admin.site.register(models.Messages, MessageAdmin)