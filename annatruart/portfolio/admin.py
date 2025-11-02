from django.contrib import admin
from .models import ArtPiece, Description

# Register your models here.
class ArtPieceAdmin(admin.ModelAdmin):
   list_display = ("id", "title", "full_pic", "preview_pic", "medium", "dimensions", "date")

admin.site.register(ArtPiece, ArtPieceAdmin)
admin.site.register(Description)