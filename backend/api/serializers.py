from django.contrib.auth import get_user_model
from djoser.serializers import (UserCreateSerializer,
                                UserSerializer)
from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import (IntegerField,
                                        ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        ReadOnlyField,
                                        SerializerMethodField)
from rest_framework.validators import ValidationError

from recipes.models import (Favorite,
                            Ingredient,
                            Recipe,
                            RecipeIngredient,
                            ShoppingCart,
                            Tag)
from users.models import Subscribe

User = get_user_model()
