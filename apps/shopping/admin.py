from django.contrib import admin


from . import models


admin.site.register(models.Customer)
admin.site.register(models.ShippingAddress)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
admin.site.register(models.Product)
admin.site.register(models.Tags)
admin.site.register(models.Categories)
admin.site.register(models.Review)
admin.site.register(models.Colors)
admin.site.register(models.Brands)
admin.site.register(models.Sizes)