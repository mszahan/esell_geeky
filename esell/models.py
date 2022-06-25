from django.db import models
from django.contrib.auth.models import User

Division_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Sylhet', 'Sylhet'),
    ('Mymenshingh', 'Mymenshingh'),
    ('Rangpur', 'Rangpur')
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    delivary_mail = models.EmailField(max_length=254)
    district = models.CharField( max_length=50)
    village = models.CharField(max_length=100)
    postal = models.IntegerField()
    division = models.CharField(choices=Division_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def single_total_cost(self):
        return self.quantity * self.product.discounted_price
    
    def __str__(self):
        return str(self.id)


STATUS_CHOICES =(
    ('Pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('Delivered', 'Delivered')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def single_total_cost(self):
        return self.quantity * self.product.discounted_price
