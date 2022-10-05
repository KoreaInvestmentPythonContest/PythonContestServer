from django.db import models
from django.conf import settings

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
    region = models.CharField(db_column='Region', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCKS'
        unique_together = (('market', 'symbol'),)


class News(models.Model):
    seq = models.AutoField(db_column='SEQ', primary_key=True)  # Field name made lowercase.
    occr_dt = models.CharField(db_column='OCCR_DT', max_length=8, db_collation='utf8_general_ci')  # Field name made lowercase.
    occr_loc = models.CharField(db_column='OCCR_LOC', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='TEXT', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    anal_yn = models.CharField(db_column='ANAL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    extr_yn = models.CharField(db_column='EXTR_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    extr_stck_cd_list = models.CharField(db_column='EXTR_STCK_CD_LIST', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    img_url_list = models.CharField(db_column='IMG_URL_LIST', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEWS'
        unique_together = (('seq', 'occr_dt'),)


class Clientcomment(models.Model):
    seq = models.AutoField(db_column='SEQ', primary_key=True)  # Field name made lowercase.
    newseq = models.IntegerField(db_column='NEWSEQ', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='TEXT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'ClientComment'

class Clientheart(models.Model):
    clientid = models.IntegerField(db_column='ClientId', primary_key=True)  # Field name made lowercase.
    newsseq = models.IntegerField(db_column='NewsSeq')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientHeart'
        unique_together = (('clientid', 'newsseq'),)

class Clientfollowstock(models.Model):
    seq = models.AutoField(db_column='Seq', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId')  # Field name made lowercase.
    market = models.CharField(db_column='Market', max_length=6, blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientFollowStock'
        unique_together = (('seq', 'clientid'),)