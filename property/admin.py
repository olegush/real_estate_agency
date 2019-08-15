from django.contrib import admin

from .models import Flat, Complaint, Owner

class ComplaintInline(admin.TabularInline):
    model = Complaint
    extra = 0

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [ComplaintInline]
    fields = ['owner', ('owners_phonenumber', 'owners_phonenumber_pure'), 'description', ('town', 'town_district'), 'address', ('floor', 'rooms_number'), ('living_area', 'has_balcony'),  ('construction_year', 'new_building'), 'liked_by', 'price', 'active', 'created_at']
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    list_per_page = 20


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'phonenumber_pure')
    raw_id_fields = ('flats',)
