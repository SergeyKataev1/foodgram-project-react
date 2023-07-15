from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ExtendedUserViewSet, IngredientViewSet, RecipeViewSet,
                       TagViewSet)

router = DefaultRouter()

router.register(
    'users',
    ExtendedUserViewSet,
    basename='users'
)
router.register(
    'tags',
    TagViewSet,
    basename='tags'
)
router.register(
    'ingredients',
    IngredientViewSet,
    basename='ingredient'
)
router.register(
    'recipes',
    RecipeViewSet,
    basename='recipes'
)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
