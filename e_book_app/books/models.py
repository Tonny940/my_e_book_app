from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=30
    )
    author = models.CharField(
        max_length=30
    )
    date_of_publishing = models.DateField(
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(10)
        ],
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0, message="Price must be higher than 0")
        ]
    )

    book_photo = models.URLField()

    slug = models.SlugField(
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')
        return super().save(*args, **kwargs)
