from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Details)
admin.site.register(Feedback)
admin.site.register(Image)
admin.site.register(Tran)