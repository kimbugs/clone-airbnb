from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at", "updated_at"
    )
    search_fields = (
        "name",
        "^price",
        "=owner__username"
    )

    list_filter = (
        "country",
        "city",
        "decription",
        "address",
        "pet_friendly",
        "kind",
        "owner",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name", "created_at", "updated_at"
    )
    readonly_fields = (
        "created_at",
        "updated_at"
    )
