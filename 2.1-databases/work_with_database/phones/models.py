from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField(max_length=250, verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-слаг')

    def __str__(self):
        return self.name