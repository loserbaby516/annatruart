from django.db import models

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=64)
    full_pic = models.ImageField(null=True, blank=True)
    preview_pic = models.ImageField(default='default.png', blank=True)
    medium = models.CharField(max_length=64, blank=True)
    dimensions = models.CharField(max_length=64, blank=True)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} ({self.date})"
    
class Description(models.Model):
    art_piece = models.OneToOneField(ArtPiece, on_delete=models.CASCADE, related_name="description")
    pic = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.art_piece.title} Description"
    


