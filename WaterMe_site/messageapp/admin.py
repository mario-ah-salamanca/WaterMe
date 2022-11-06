from django.contrib import admin
from .models import Message, TwilioAccount, SensorData


class SingletonModelAdmin(admin.ModelAdmin):
    """
    Prevents Django admin users deleting the singleton or adding extra rows.
    """
    actions = None  # Removes the default delete action.

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Message)
admin.site.register(TwilioAccount)
admin.site.register(SensorData)
