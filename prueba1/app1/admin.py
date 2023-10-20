from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.site_header = 'Ci'


admin.site.register(Post)