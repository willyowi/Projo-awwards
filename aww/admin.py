from django.contrib import admin
from aww.models import *
# Register your models here.
# register profile
admin.site.register(Profile)
# register project
admin.site.register(Project)
# register review
admin.site.register(Review)
