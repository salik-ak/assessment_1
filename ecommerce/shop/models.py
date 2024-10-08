from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

# Use the key defined in settings
KEY = settings.FERNET_KEY

# Check if the key is valid
if len(KEY) != 44:  # 32 bytes + 12 bytes for padding in base64
    raise ValueError("Invalid Fernet key length.")

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
        try:
            return fernet.decrypt(self.encrypted_price).decode()
        except Exception as e:
            return f"Error decrypting price: {e}"

    def set_price(self, price):
        fernet = Fernet(KEY)
        self.encrypted_price = fernet.encrypt(str(price).encode())

    price = property(get_price, set_price)
