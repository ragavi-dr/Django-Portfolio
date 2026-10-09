from django.contrib import admin

# Register your models here.

from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    def short_message(self,obj):
        return obj.message[:50]
    short_message.short_description = 'Message'