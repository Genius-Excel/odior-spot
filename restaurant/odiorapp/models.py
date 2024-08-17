from django.db import models


item_choices = (
    ("Regular Shawarma", "Regular Shawarma"),
    ("Peppered Snail", "Peppered Snail"),
    ("Combo Shawarma", "Combo Shawarma"),
    ("Spaghetti", "Spaghetti"),
    ("Peppered Chicken", "Peppered Chicken"),
    ("Small Pan of Asun", "Big Pan of Asun"),

)

item_quantities = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class OrderRequest(models.Model):
    customer_name = models.CharField(max_length=150)
    email = models.EmailField()
    order_item = models.CharField(max_length=150, choices=item_choices)
    order_quantity = models.CharField(max_length=150, choices=item_quantities)
    special_request = models.TextField()