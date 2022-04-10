from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.IntegerField(blank=False, default=0)
    update_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            obj = Profile.objects.create(user=instance)
            obj.save()


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Size(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
        ordering = ['title']


class Merch(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    price = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'
        ordering = ['title']


class MerchSizeNum(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE, related_name='merch_size_num', null=True)
    count = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return f'{self.merch.__str__()} {self.size.__str__()}'

    class Meta:
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остаток'
        ordering = ['id']


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    size_count = models.IntegerField()
    basket_coast = models.IntegerField()
    spent_score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.__str__()} {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['created_at']



