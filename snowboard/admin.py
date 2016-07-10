from django.contrib import admin
from snowboard.models import video
from snowboard.models import learningsnowboarding
from snowboard.models import learningsking

# Register your models here.
class videoAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_field=('title',)


class learningsnowboardingAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_field=('title',)
    filter_horizaontal=('similar')

class learningskingAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_field=('title',)
    filter_horizaontal=('similar')


admin.site.register(video, videoAdmin)
admin.site.register(learningsnowboarding, learningsnowboardingAdmin)
admin.site.register(learningsking, learningskingAdmin)
