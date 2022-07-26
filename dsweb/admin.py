from django.contrib import admin
from .models import Inquiry


class InquiryAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Inquiry, InquiryAdmin)
