from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.contrib.auth.password_validation import NumericPasswordValidator
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
import re
from difflib import SequenceMatcher


class MinimumLengthValidator(MinimumLengthValidator):#class override to change password error text
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Цей пароль занадто короткий. Він повинен містити не менше %(min_length)d символів.",
                    "Цей пароль занадто короткий. Він повинен містити не менше %(min_length)d символів.",
                    self.min_length
                ),
            code='password_too_short',
            params={'min_length': self.min_length},
        	)

    def get_help_text(self):
       return ngettext(
           "Ваш пароль повинен містити не менше %(min_length)d символів.",
           "Ваш пароль повинен містити не менше %(min_length)d символів.",
           self.min_length
       ) % {'min_length': self.min_length}

class CommonPasswordValidator(CommonPasswordValidator):#class override to change password error text
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                ("Цей пароль занадто поширений і ненадійний."),
                code='password_too_common',
            )
    def get_help_text(self):
        return ("Цей пароль занадто поширений і ненадійний.")


class NumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                ("Ваш пароль не може бути повністю цифровим"),
                code='password_entirely_numeric',
            )
    def get_help_text(self):
        return ("Ваш пароль не може бути повністю цифровим")


class UserAttributeSimilarityValidator(UserAttributeSimilarityValidator):#class override to change password error text
    def validate(self, password, user=None):
        if not user:
            return
        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        ("Ваш пароль не може бути схожим на %(verbose_name)s."),
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )
    def get_help_text(self):
        return ("Ваш пароль не може бути схожим на іншу особисту інформацію.")


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', error_messages ={'max_length':'Поле може містити не більше %(limit_value)d символів (зараз %(show_value)d)'})
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', error_messages ={'max_length':'Поле може містити не більше %(limit_value)d символів (зараз %(show_value)d)'})
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    error_messages = {'password_mismatch':"Введені паролі не співпадають", 'password_too_common':"dsfnsd"}#override error messages for the password mismatch

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        error_messages = {'username':{'unique':'Це імʼя зайняте, оберіть інше', 'max_length':'Поле може містити не більше %(limit_value)d символів (зараз %(show_value)d)'}, }#override error messages for the username unique