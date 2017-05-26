from django.contrib import admin
from fpickapp import models

# Register your models here.
# fpickModels = [models.Memory,models.Chipset,models.Audio,models.Connectivity,models.Battery,models.Operating_System,models.Dimension,models.After_Sale_Service,models.Display_Features,models.Computer_Specification,
# 			models.Computer_Feature,models.Computer_Brand,models.Computer,models.Computer_and_peripherials]
# admin.site.register(models.Electronics)
# admin.site.register(fpickModels)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Category,CategoryAdmin)

class Computer_kindAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Computer_kind,Computer_kindAdmin)

class MemoryAdmin(admin.ModelAdmin):
	list_display = ('ram','memory_type','speed')

admin.site.register(models.Memory, MemoryAdmin)

class ChipsetAdmin(admin.ModelAdmin):
	list_display = ('gpu_model','gpu_memory_shared','hdmi_port')

admin.site.register(models.Chipset, ChipsetAdmin)

class AudioAdmin(admin.ModelAdmin):
	list_display = ('speaker',)

admin.site.register(models.Audio, AudioAdmin)

class ConnectivityAdmin(admin.ModelAdmin):
	list_display = ('usb_port','bluetooth','digital_media_reader')

admin.site.register(models.Connectivity, ConnectivityAdmin)

class BatteryAdmin(admin.ModelAdmin):
	list_display = ('battery_type','battery_cell')

admin.site.register(models.Battery, BatteryAdmin)

class Operating_SystemAdmin(admin.ModelAdmin):
	list_display = ('os',)

admin.site.register(models.Operating_System, Operating_SystemAdmin)

class DimensionAdmin(admin.ModelAdmin):
	list_display = ('dimensions','weight')

admin.site.register(models.Dimension, DimensionAdmin)

class After_Sale_ServiceAdmin(admin.ModelAdmin):
	list_display = ('warranty',)

admin.site.register(models.After_Sale_Service, After_Sale_ServiceAdmin)

class Display_FeaturesAdmin(admin.ModelAdmin):
	list_display = ('screen_size','maximum_display_resolution','panel_type')

admin.site.register(models.Display_Features, Display_FeaturesAdmin)

class Computer_SpecificationAdmin(admin.ModelAdmin):
	list_display = ('processor_description','memory','hard_drive','display_features','chipset','audio','connectivity','battery',
		'operating_systems','dimension','after_sale_service')

admin.site.register(models.Computer_Specification, Computer_SpecificationAdmin)


class Computer_FeatureAdmin(admin.ModelAdmin):
	list_display = ('processor','ram','inbuilt_hdd','os')

admin.site.register(models.Computer_Feature, Computer_FeatureAdmin)

class Computer_BrandAdmin(admin.ModelAdmin):
	list_display = ('brand_name','brand_logo')

admin.site.register(models.Computer_Brand, Computer_BrandAdmin)

class ComputerAdmin(admin.ModelAdmin):
	list_display = ('name','brand','feature','specification','computer_type','description','image','color','price',
		'stock','available','created','updated','category')
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Computer,ComputerAdmin)







