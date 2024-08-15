from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from medbooks.models.medicalBook import MedBook
from django.db import transaction
import random
import string
from django.utils import timezone


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.ReadOnlyField()
    passport_data = serializers.CharField(write_only=True)
    snils = serializers.CharField(write_only=True)
    oms = serializers.CharField(write_only=True)
    birthday = serializers.CharField(write_only=True)
    sex = serializers.CharField(write_only=True)
    middle_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
            'middle_name',
            'sex',
            'birthday',
            'snils',
            'oms',
            'passport_data',
            'password'
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже зарегистрирован.'
            )
        return email

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = User.objects.create_user(**validated_data)
                # Создаем медицинскую книжку при создании пользователя
                MedBook.objects.create(
                    card_number=generate_medbook_number(),
                    status=True,
                    date_created=timezone.now(),
                    account_id=user.id
                )
        except Exception as e:
            # Обработка ошибки в транзакции, выбрасываем ParseError
            raise ParseError(f"Ошибка при создании пользователя и медицинской книжки: {e}")

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля'
            )
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'sex',
            'birthday',
            'snils',
            'oms',
            'passport_data',
            'email',
            'phone_number',
            'date_joined'
        )


class MeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'sex',
            'birthday',
            'snils',
            'oms',
            'passport_data',
            'email',
            'phone_number',
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

#Функция для генерации


def generate_medbook_number():
    letters_part = ''.join(random.choices(string.ascii_uppercase, k=5))
    digits_part = ''.join(random.choices(string.digits, k=5))
    return f"{letters_part}{digits_part}"
