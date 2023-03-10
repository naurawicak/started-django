from django.contrib import admin
from .models import Pertanyaan, Pilih

# Register your models here.

class PilihInline(admin.TabularInline):
    model = Pilih
    extra = 3
class PertanyaanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pertanyaan_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':'collapse'}),
    ]
    inlines = [PilihInline]
    list_display = ('id','pertanyaan_text', 'pub_date', 'was_publish_terbaru')
    list_filter = ['pub_date']
    search_fields = ['pertanyaan_text']

admin.site.register(Pertanyaan, PertanyaanAdmin)