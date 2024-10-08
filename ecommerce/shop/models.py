from django.db import models
from cryptography.fernet import Fernet
import base64
from django.conf import settings

# Generate a Fernet key (save this securely!)
KEY = Fernet.generate_key()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    encrypted_price = models.BinaryField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_price(self):
        fernet = Fernet(KEY)
        return fernet.decrypt(self.encrypted_price).decode()

    def set_price(self, price):
        fernet = Fernet(KEY)
        self.encrypted_price = fernet.encrypt(str(price).encode())

    price = property(get_price, set_price)

