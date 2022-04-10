from django.contrib import admin
from .models import *


class Merch_admin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('category',)


class MerchSizeNum_admin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('size', )


class Category_admin(admin.ModelAdmin):
    search_fields = ('title',)


class Profile_admin(admin.ModelAdmin):
    search_fields = ('title',)


class Size_admin(admin.ModelAdmin):
    pass


class Orders_admin(admin.ModelAdmin):
    pass


admin.site.register(Merch, Merch_admin)
admin.site.register(MerchSizeNum, MerchSizeNum_admin)
admin.site.register(Category, Category_admin)
admin.site.register(Size, Size_admin)
admin.site.register(Profile, Profile_admin)
admin.site.register(Orders, Orders_admin)

