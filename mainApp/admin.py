from django.contrib import admin
from .models import *
from extraApp.models import *

admin.site.register([Category, SubCategory, Owner, ProductImage])


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image',)


class DisplayInline(admin.TabularInline):
    model = Display
    fields = ('surface', 'touch_screen', 'frame_rate', 'matrix_type', 'resolution', 'dioganal')


class ProcessorInline(admin.TabularInline):
    model = Processor
    fields = (
        'model', 'brand', 'family', 'gen', 'core',
        'thread', 'min_frequency', 'max_frequency', 'cache', 'video_card'
    )


class RAMInline(admin.TabularInline):
    model = RAM
    fields = ('model', 'type', 'brand', 'size',)


class VideoCardInline(admin.TabularInline):
    model = VideoCard
    fields = ('model', 'type', 'brand', 'size')


class CameraInline(admin.TabularInline):
    model = Camera
    fields = ('model', 'type', 'brand', 'pixel_size')


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImageInline, DisplayInline, ProcessorInline, RAMInline, VideoCardInline, CameraInline]


admin.site.register(Product, ProductAdmin)
