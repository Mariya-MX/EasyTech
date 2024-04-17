from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=20)  # Add any additional fields you need




  


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    education_field = models.CharField(max_length=50, blank=True, null=True)
    

    
    
    def __str__(self):
        return self.user.username if self.user else 'No User'
    


class TechnicianProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    service = models.CharField(max_length=50)  # electrician, plumber, repairer, etc.
    resume = models.FileField(upload_to='technician_resumes/', blank=True, null=True, help_text='Upload a PDF file')
    id_proof = models.ImageField(upload_to='id_proofs/', blank=True, null=True, help_text='Upload an image for ID proof')
    experience = models.PositiveIntegerField(null=True, blank=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    # Additional fields for job application
    tech_first_name = models.CharField(max_length=255, blank=True, null=True)
    tech_last_name = models.CharField(max_length=255, blank=True, null=True)
    tech_email = models.EmailField(blank=True, null=True)
    tech_number = models.CharField(max_length=15, blank=True, null=True)
    # Image field for technician's profile
    tech_image = models.ImageField(upload_to='technician_profile_images/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # New field for approval status

    def __str__(self):
        return f"{self.user.username} - {self.service}"
    


    
class ApprovedTechnician(models.Model):
    technician_profile = models.OneToOneField(TechnicianProfile, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approved Technician: {self.technician_profile.tech_first_name} {self.technician_profile.tech_last_name}"




class TechnicianAvailability(models.Model):
    technician = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.technician.username} - {self.date} - {self.time_slot}"


# models.py

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.TextField()
    availability_id = models.IntegerField()
    technician_id = models.IntegerField()
    user_email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(max_length=20)

    def __str__(self):
        return f"Booking - {self.name} ({self.date}, {self.time_slot})"



class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -  {self.message}'
    

class CustomerNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.message}'
    


# models.py
from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


# models.py
from django.db import models
class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"



# main project 


from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ad_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    contact = models.CharField(max_length=20)  # Assuming the contact number is a string
    image1 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending..')
    ordered = models.BooleanField(default=False)  
    
    

    def __str__(self):
        return f"{self.brand_name} - {self.ad_title}"
    



class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Address"
    
    

class FavoriteProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Ensures each user can only favorite a product once


from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='transactions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_needed = models.BooleanField(default=False)
    






