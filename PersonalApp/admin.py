from django.contrib import admin
from .models import home_model, about_model, contacts_model,contactinfo_model, post_detail_model,related_fields
from django.utils import timezone
class Homeadmin(admin.ModelAdmin):

    list_display = ('id', 'hello_message','main_image')
    list_display_links = ('id', 'hello_message','main_image',)
    search_fields = ('msg1',)
    list_per_page = 24



class Aboutadmin(admin.ModelAdmin):

    list_display = ('id', 'about_me')
    list_display_links = ('id', 'about_me')
    search_fields = ('about_me',)
    list_per_page = 24



class ContactInfoadmin(admin.ModelAdmin):

    list_display = ('id', 'adress',)
    list_display_links = ('id', 'adress',)
    search_fields = ('adress',)
    list_per_page = 24

class Contactadmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name','email')
    search_fields = ('description','title', 'subject','email')
    list_per_page = 24


class PostDetetailAdmin(admin.ModelAdmin):

    list_display=('id','post_head')
    list_display_links=('id','post_head')
    search_fields=('post_text_one','post_text_two')


class relatedFieldAdmin(admin.ModelAdmin):
    list_display=('topics','id')
    list_display_links=('id','topics')
    search_fields=('topics',)


admin.site.register(related_fields,relatedFieldAdmin)
admin.site.register(home_model, Homeadmin)

admin.site.register(about_model, Aboutadmin)

admin.site.register(contacts_model, Contactadmin)

admin.site.register(contactinfo_model, ContactInfoadmin)
admin.site.register(post_detail_model, PostDetetailAdmin)