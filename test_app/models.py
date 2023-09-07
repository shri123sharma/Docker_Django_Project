from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def employee_picture_path(instance, filename):
    return f'files/employees/{instance.slug}/{filename}'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=employee_picture_path, null=True, blank=True)
    cv = models.FileField(upload_to=employee_picture_path,
                          validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                          null=False,
                          blank=False)
    slug = models.SlugField(unique=True)

   
    def clean(self):
        errors = {}
        if not self.first_name:
            errors['first_name'] = 'First Name is required.'
        if not self.last_name:
            errors['last_name'] = 'Last Name is required.'
        if not self.picture:
            errors['picture'] = 'Picture is required.'
        if not self.cv:
            errors['cv'] = 'CV is required.'
       
        if errors:
            raise ValidationError(errors)
        
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name}-{self.last_name}")
        self.full_clean()
        super().save(*args, **kwargs)

