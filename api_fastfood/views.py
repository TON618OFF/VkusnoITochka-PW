from django.shortcuts import render
from .serializers import *
from .permission import *
from rest_framework import viewsets
from fastfood.models import *
from rest_framework import mixins
from rest_framework.renderers import AdminRenderer

# Create your views here.
class CategoryViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)
        return queryset


class DishViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = DishSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Dish.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        category = self.request.query_params.get('category', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)
        elif category is not None:
            queryset = queryset.filter(category__icontains=description)
        return queryset


    #renderer_classes = [AdminRenderer]

class PromotionViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = PromotionSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Promotion.objects.all()
        title = self.request.query_params.get('title', None)
        description = self.request.query_params.get('description', None)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)
        return queryset



class ContactViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = ContactSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Contact.objects.all()
        address = self.request.query_params.get('address', None)
        phone = self.request.query_params.get('phone', None)
        email = self.request.query_params.get('email', None)

        if address is not None:
            queryset = queryset.filter(address__icontains=address)
        elif phone is not None:
            queryset = queryset.filter(phone__icontains=phone)
        elif email is not None:
            queryset = queryset.filter(email__icontains=email)
        return queryset

class UserProfileViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = UserProfileSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        user = self.request.query_params.get('user', None)
        last_name = self.request.query_params.get('last_name', None)
        first_name = self.request.query_paramsn.get('first_name', None)
        patronymic = self.request.query_params.get('patronymic', None)
        phone = self.request.query_params.get('phone', None)
        address = self.request.query_params.get('address', None)

        if user is not None:
            queryset = queryset.filter(user__icontains=user)
        elif last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        elif first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        elif patronymic is not None:
            queryset = queryset.filter(patronymic__icontains=patronymic)
        elif phone is not None:
            queryset = queryset.filter(phone__icontains=phone)
        elif address is not None:
            queryset = queryset.filter(address__icontains=address)
        return queryset

class OrderViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user', None)
        last_name = self.request.query_params.get('last_name', None)
        first_name = self.request.query_params.get('first_name', None)
        patronymic = self.request.query_params.get('patronymic', None)
        phone = self.request.query_params.get('phone', None)
        address = self.request.query_params.get('address', None)
        total_price = self.request.query_params.get('total_price', None)
        delivery_type = self.request.query_params.get('delivery_type', None)

        if user is not None:
            queryset = queryset.filter(user__icontains=user)
        elif last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        elif first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        elif patronymic is not None:
            queryset = queryset.filter(patronymic__icontains=patronymic)
        elif phone is not None:
            queryset = queryset.filter(phone__icontains=phone)
        elif address is not None:
            queryset = queryset.filter(address__icontains=address)
        elif total_price is not None:
            queryset = queryset.filter(total_price__icontains=total_price)
        elif delivery_type is not None:
            queryset = queryset.filter(delivery_type__icontains=delivery_type)
        return queryset

class OrderItemViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

class DeliveryViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = DeliverySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Delivery.objects.all()
        status = self.request.query_params.get('status', None)

        if status is not None:
            queryset = queryset.filter(status__icontains=status)
        return queryset