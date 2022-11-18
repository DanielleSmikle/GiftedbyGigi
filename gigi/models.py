from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length =255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'collections'

    def __str__(self):
        return self.name

class Feature(models.Model):
    collection = models.ForeignKey(Collection, related_name='feature', on_delete=models.CASCADE)
    scent = models.CharField(max_length= 255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural= 'Features'
        ordering=('-created', )

    def __str__(self):
        return self.scent







