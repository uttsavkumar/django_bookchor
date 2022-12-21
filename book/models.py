from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    cat_title = models.TextField()
    cat_description = models.TextField()

    def __str__(self) -> str:
        return self.cat_title


class Books(models.Model):
    title = models.TextField()
    original_price = models.IntegerField()
    current_price = models.IntegerField()
    author = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='bookimages/',null=True,default=None)
    description = models.TextField()
    isbn = models.TextField()

    def __str__(self) -> str:
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username

ADDRESS_TYPE = (
    ("H","Home"),
    ("O","Office"),
)
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField()
    address_type = models.CharField(max_length=50,choices=ADDRESS_TYPE)
    default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

class Coupon(models.Model):
    code = models.CharField( max_length=50)
    amount = models.FloatField()

    def __str__(self) -> str:
        return self.code

class Payment(models.Model):
    txn_id = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=200,null=True,blank=True)
    items = models.ManyToManyField(OrderItem)
    status = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    order_date = models.DateTimeField(null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL,null=True)
    being_delivered = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user