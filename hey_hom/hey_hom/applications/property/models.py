from django.db import models

# Create your models here.
class PropertyModel(models.Model):
    SHIFT_CHOICES = (
        ('house','house'),
        ('apartment','apartment')
    )

    title = models.CharField('Title',max_length=30)
    description = models.TextField('Description')
    price = models.DecimalField('Price',max_digits=9,decimal_places=2)
    location = models.CharField('Location',max_length=30)
    property_type = models.CharField('Property Type',max_length=20,choices=SHIFT_CHOICES)
    bedrooms = models.IntegerField('Bedrooms')
    bathrooms = models.IntegerField('Bathrooms')
    square_feet = models.IntegerField('Square Feet')
    available = models.BooleanField('Available',default=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        ordering = ['title']

    def __str__(self):
        return self.title
