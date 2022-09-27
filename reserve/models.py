from django.db import models

class Shop(models.Model):
   
    reservable_date = models.IntegerField(verbose_name='Rezervasyon Edilebilir')
    start_time = models.TimeField(verbose_name='Açılış Saatleri')
    end_time = models.TimeField(verbose_name='Kapanış Saati')
    max_reserve_num = models.IntegerField(verbose_name='Maksimum saat başına kişi sayısı')

    def __str__(self):
        return str(self.reservable_date)

class Reserve(models.Model):
    
    date_choices = (
            ('', 'Rezervasyon Tarihi'),
            ('1', '6/1'),
            ('2', '6/2'),
            ('3', '6/3'),
    )
    num_choices = (
            ('', 'Kişi Sayısı'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
    )
    time_choices = (
            ('', 'Rezervasyon Tarihi'),
            ('1', '14:00'),
            ('2', '15:00'),
            ('3', '16:00'),
    )
    reserve_date = models.CharField(
            verbose_name='Rezervasyon Tarihi',
            max_length=20,
            choices=date_choices,
    )
   
    reserve_time = models.CharField(
            verbose_name='Rezervasyon Tarihi',
            max_length=10,
            choices=time_choices,
    )
    reserve_num = models.CharField(
            verbose_name='Rezervasyon Yapan Kişi Sayısı',
            max_length=10,
            choices=num_choices,
    )
    name = models.CharField(verbose_name='Ad Soyad', max_length=100)
    email = models.EmailField(verbose_name='Eposta Adresi', max_length=254)
    tel = models.CharField(verbose_name='Telefon Numarası', max_length=20)
    comment = models.TextField(verbose_name='Açıklama sütunu')
    """
    def __str__(self):
        return str(self.reserve_date)
    """

# Create your models here.
