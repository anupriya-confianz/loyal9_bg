from django.db import models
from django.db import models

class Contact(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20,default='')
    Company = models.CharField(max_length=50, default='')
    CrmId = models.IntegerField(default=0)
    PhoneNumber = models.CharField(max_length=35, default='')
    def __str__(self):
     return self.FirstName

class Invoice(models.Model):
    ContactId = models.IntegerField(default=0)
    TotalPaid = models.CharField(max_length=10,default='')
    TotalDue = models.CharField(max_length=10, default='')
    InvoiceId = models.IntegerField(default=0)
    InvoiceTotal = models.CharField(max_length=35, default='')
    RefundStatus = models.CharField(max_length=35, default='')
    DateCreated = models.CharField(max_length=40, default='')
    def __int__(self):
     return self.InvoiceId

class Payment(models.Model):
    PaymentId = models.CharField(max_length=35,default=0)
    UserId = models.IntegerField(default=0)
    InvoiceId = models.IntegerField(default=0)
    PayAmt = models.CharField(max_length=35, default='')
    def __str__(self):
     return self.PaymentId

class Order(models.Model):
    OrderId = models.IntegerField(default=0)
    ProductId = models.IntegerField(default=0)
    def __int__(self):
     return self.OrderId

class ItemOrder(models.Model):
    ItemOrderId = models.IntegerField(default=0)
    InvoiceId = models.IntegerField(default=0)
    OrderItemId = models.IntegerField(default=0)
    def __int__(self):
     return self.ItemOrderId