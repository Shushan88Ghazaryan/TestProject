from django.contrib import admin
from .models import *
class CountryAdmin(admin.ModelAdmin):
    list_display = ('state','capital','dates')
admin.site.register(Country,CountryAdmin)






# class LanguageAdmin(admin.ModelAdmin):
#     list_display = ('prog_lang','lang')
# class StyleAdmin(admin.ModelAdmin):
#     list_display = ('prog_style','st')
# class ChoiceAdmin(admin.ModelAdmin):
#      list_display = ('langknow','stknow')
# admin.site.register(Language,LanguageAdmin)
#admin.site.register(Style,StyleAdmin)
# admin.site.register(Choice)
# admin.site.register(Prog_lang)
# admin.site.register(Tech)
# admin.site.register(Worker)
