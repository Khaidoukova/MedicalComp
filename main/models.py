from django.db import models
from django.urls import reverse

from users.models import User


class TestCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class LabTest(models.Model):
    name = models.CharField(max_length=100, verbose_name='название анализа')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, verbose_name='категория', null=True, blank=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    price = models.IntegerField(verbose_name='цена', null=True, blank=True)
    time = models.IntegerField(verbose_name='срок выполнения', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('main:labtest_detail',
                       args=self.pk)


class Doctor(models.Model):
    PRIMARY_VISIT = 'первичный прием'
    SECONDARY_VISIT = 'повторный прием'

    VISITS = (
        (PRIMARY_VISIT, 'первичный прием'),
        (SECONDARY_VISIT, 'повторный прием')

    )
    specialization = models.CharField(max_length=100, verbose_name='специализация')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, verbose_name='категория', null=True,
                                 blank=True)
    price = models.IntegerField(verbose_name='цена', null=True, blank=True)
    visit = models.CharField(max_length=20, choices=VISITS, default=PRIMARY_VISIT, verbose_name='прием')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ('specialization',)

    def __str__(self):
        return f'{self.specialization}'

    def get_absolute_url(self):
        return reverse('main:doctor_detail',
                       args=self.pk)



