from django.db import models

# Create your models here.


class Stocks(models.Model):
    market = models.CharField(db_column='Market', primary_key=True, max_length=6)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=6)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=20, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    listingdate = models.CharField(db_column='ListingDate', max_length=8, blank=True, null=True)  # Field name made lowercase.
    settlemonth = models.CharField(db_column='SettleMonth', max_length=2, blank=True, null=True)  # Field name made lowercase.
    representative = models.CharField(db_column='Representative', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homepage = models.CharField(db_column='HomePage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=200, blank=True, null=True)  # Field: name made lowercase.