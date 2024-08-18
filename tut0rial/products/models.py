from django.db import models


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(db_column='bookprice')
    vatpercentage = models.FloatField(db_column='bookvatpercentage')
    created = models.DateTimeField(auto_now_add=True)
