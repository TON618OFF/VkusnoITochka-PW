from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Фото блюда")
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
    
    def __str__(self):
        return self.name

class Promotion(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='promotions/', blank=True, null=True, verbose_name="Фото акции")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
    
    def __str__(self):
        return self.title

class Order(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    address = models.TextField(verbose_name="Адрес доставки")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self):
        return f"Заказ {self.id} от {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
    
    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"

class Review(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    customer_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    comment = models.TextField(verbose_name="Комментарий")
    rating = models.PositiveIntegerField(verbose_name="Оценка")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"Отзыв на {self.dish.name}"

class Contact(models.Model):
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
    def __str__(self):
        return self.address

class DeliveryInfo(models.Model):
    description = models.TextField(verbose_name="Информация о доставке")
    
    class Meta:
        verbose_name = "Информация о доставке"
        verbose_name_plural = "Информация о доставке"
    
    def __str__(self):
        return "Информация о доставке"
