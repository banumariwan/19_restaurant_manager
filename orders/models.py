from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - (${self.price})"




class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()
    status = models.CharField(max_length=100,choices=[('Free','Free'),('Occupied','Occupied')],default='Free')


    def __str__(self):
        return f"Table {self.number} - ({self.status})"




class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE,related_name='orders')
    items = models.ManyToManyField(MenuItem,related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=[('Pending','Pending'),('Completed','Completed')],default='Open')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return f"Order {self.id} - Table({self.table.number})"
