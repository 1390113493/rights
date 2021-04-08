from django.db import models

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=50, verbose_name='键')
    value = models.CharField(max_length=5000, verbose_name='值')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '系统字段'
        verbose_name_plural = verbose_name