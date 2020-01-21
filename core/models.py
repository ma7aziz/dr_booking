from django.db import models

# Create your models here.


class Doctor(models.Model):
    SPECIALITY_CHOICES = [
        ('general', 'GENERAL'),
        ('immunology', 'IMMUNOLOGY'),
        ('dermatology', 'DERMATOLOGY'),
        ('internal-medicine', 'INTERNAL-MEDICINE'),
        ('neurology', 'NEUROLOGY'),
        ('gynecology', 'GYNECOLOGY'),
        ('ophthalmology', 'OPHTHALMOLOGY'),
        ('pediatrics', 'PEDIATRICS'),
        ('psychiatry', 'PSYCHIATRY')
    ]

    CITY_CHOICES = [
        ('Cairo', 'cairo'),
        ('Alexandria', 'alexandira')
    ]

    name = models.CharField(max_length=200)
    speciality = models.CharField(
        choices=SPECIALITY_CHOICES,
        default='general',
        max_length=50)
    address = models.CharField(max_length=300, null=True)
    area = models.CharField(max_length=100, null=True)
    city = models.CharField(
        choices=CITY_CHOICES,
        max_length=100)
    image = models.ImageField(
        upload_to='media/images/drs', blank=True, null=True)
    featured = models.BooleanField(default=False)
    price = models.IntegerField()
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
