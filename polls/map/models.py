from django.db import models

class SeouljRent(models.Model):
    class Meta:
        db_table = 'SeouljRent'

    year = models.CharField(max_length=50, null=True, blank=True)
    gucd = models.CharField(max_length=50, null=True, blank=True)
    gunm = models.CharField(max_length=50, null=True, blank=True)
    dongcd = models.CharField(max_length=50, null=True, blank=True)
    dongnm = models.CharField(max_length=50, null=True, blank=True)
    distin = models.CharField(max_length=30, null=True, blank=True)
    distinnm = models.CharField(max_length=30, null=True, blank=True)
    bn = models.CharField(max_length=50, null=True, blank=True)
    sbn = models.CharField(max_length=50, null=True, blank=True)
    fl = models.CharField(max_length=50, null=True, blank=True)
    cont = models.CharField(max_length=200, null=True, blank=True)
    distin2 = models.CharField(max_length=50, null=True, blank=True)
    spa = models.CharField(max_length=100, null=True, blank=True)
    depos = models.CharField(max_length=50, null=True, blank=True)
    depos2 = models.CharField(max_length=50, null=True, blank=True)
    bdnm = models.TextField(null=True, blank=True)
    bdcont = models.CharField(max_length=50, null=True, blank=True)
    bdusa = models.CharField(max_length=50, null=True, blank=True)
    cont2 = models.CharField(max_length=500, null=True, blank=True)
    newcont = models.CharField(max_length=50, null=True, blank=True)
    newcont2 = models.CharField(max_length=20, null=True, blank=True)
    olddepos = models.CharField(max_length=50, blank=True, null=True)
    olddepos2 = models.CharField(max_length=50, blank=True, null=True)
    lat = models.CharField(max_length=300, null=True, blank=True)
    lng = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.bn

# 서울 실거래가
class SeoulReal(models.Model):
    class Meta:
        db_table = 'SeoulReal'

    year = models.CharField(max_length=50, null=True, blank=True)
    gucd = models.CharField(max_length=50, null=True, blank=True)
    gunm = models.CharField(max_length=50, null=True, blank=True)
    dongcd = models.CharField(max_length=50, null=True, blank=True)
    dongnm = models.CharField(max_length=50, null=True, blank=True)
    distin = models.CharField(max_length=30, null=True, blank=True)
    distinnm = models.CharField(max_length=30, null=True, blank=True)
    bn = models.CharField(max_length=50, null=True, blank=True)
    sbn = models.CharField(max_length=50, null=True, blank=True)
    bdnm = models.TextField(null=True, blank=True)
    cont = models.CharField(max_length=200, null=True, blank=True)
    depos = models.CharField(max_length=50, null=True, blank=True)
    spa = models.CharField(max_length=100, null=True, blank=True)
    spa2 = models.CharField(max_length=100, null=True, blank=True)
    fl = models.CharField(max_length=50, null=True, blank=True)
    authr = models.CharField(max_length=50, null=True, blank=True)
    cancel = models.CharField(max_length=50, null=True, blank=True)
    bdcont = models.CharField(max_length=50, null=True, blank=True)
    bdusa = models.CharField(max_length=50, null=True, blank=True)
    noti = models.CharField(max_length=50, null=True, blank=True)
    notibu = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=300, null=True, blank=True)
    lng = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.bn
