from django.db import models
from django.template.defaultfilters import slugify

from e_book_app.accounts.validators import validate_file_size


# Create your models here.
class User(models.Model):
    name = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        blank=True,
        null=True
    )
    personal_photo = models.ImageField(
        null=True,
        blank=True,
        validators=[
            validate_file_size,
        ]
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        blank=False,
        null=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)
