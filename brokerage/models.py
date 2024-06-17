from django.db import models

class Truck(models.Model):
    description = models.CharField(max_length=255, verbose_name="Truck Description" ,default='No description')
    name = models.CharField(max_length=255, verbose_name="Truck Name")
    year = models.DateField(verbose_name="Year of Manufacture")
    load_capacity = models.PositiveIntegerField(verbose_name="Load Capacity (kg)")
    speed = models.PositiveIntegerField(verbose_name="Speed (km/h)")
    transmission = models.CharField(max_length=100, verbose_name="Transmission Type")
    impact_protection = models.CharField(max_length=100, verbose_name="Impact Protection")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price ($)")
    image = models.ImageField(upload_to='trucks/', verbose_name="Main Image", null=True, blank=True)
    text = models.TextField(verbose_name="Comment Text")

    def __str__(self):
        return f"{self.name} ({self.year})"

class TruckImage(models.Model):
    truck = models.ForeignKey(Truck, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='truck_images/', verbose_name="Image")

    def __str__(self):
        return f"Image for {self.truck.name}"
    

class TruckOrder(models.Model):
    # truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    text = models.TextField( verbose_name="Textarea")

    def __str__(self):
        return self.name
