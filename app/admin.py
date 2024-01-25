from django.contrib import admin

from app.models import User, ChatPrivateMessage, ChatPrivate
# Register your models here.


admin.site.register(User)
admin.site.register(ChatPrivate)
admin.site.register(ChatPrivateMessage)
