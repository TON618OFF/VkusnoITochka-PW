from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='dishes/', verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
    
    def __str__(self):
        return self.name

class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(upload_to='promotions/', verbose_name="Изображение", blank=True, null=True)
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
    def __str__(self):
        return self.address

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес", blank=True)
    
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Order(models.Model):
    DELIVERY_TYPES = (
        ('pickup', 'Самовывоз'),
        ('courier', 'Курьером'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес доставки")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPES, verbose_name="Тип доставки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self):
        return f"Заказ {self.id} от {self.last_name} {self.first_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
    
    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    status = models.CharField(max_length=100, verbose_name="Статус", default="В обработке")
    courier_info = models.TextField(verbose_name="Информация о курьере", blank=True)
    estimated_time = models.DateTimeField(verbose_name="Ориентировочное время доставки", null=True, blank=True)
    
    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"
    
    def __str__(self):
        return f"Доставка для заказа {self.order.id}"