from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=200,
                            unique=True)
    color = models.CharField(verbose_name='Цвет',
                             max_length=7,
                             unique=True,
                             validators=[
                                 RegexValidator(
                                     regex=('^#([A-Fa-f0-9]{6}|'
                                            '[A-Fa-f0-9]{3})$'),
                                     message='Ошибка в HEX коде цвета',
                                 )
                             ])
    slug = models.SlugField(max_length=200,
                            unique=True,
                            validators=[
                                RegexValidator(
                                    regex='^[-a-zA-Z0-9_]+$',
                                    message='Ошибка в вводе slug поля',
                                )
                            ])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=200,
                            unique=True)
    measurement_unit = models.CharField(verbose_name='Единица измерения',
                                        max_length=200)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredients_unique'
            )
        ]

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='recipes')
    name = models.CharField(verbose_name='Название',
                            max_length=200)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='recipe/')
    text = models.CharField(verbose_name='Текст',
                            max_length=1024)
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredient')
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги')
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredienttorecipe')
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[
        MinValueValidator(1, message='Мин. количество ингредиента < 1')])

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='ingredienttorecipe_unique'
            )
        ]

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount} '
        )


class FavoriteAndShoppingCart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное в корзине'
        verbose_name_plural = 'Избранное в корзине'
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='%(app_label)s_%(class)s_unique',
            )
        ]


class Favorite(FavoriteAndShoppingCart):

    def __str__(self):
        return f'{self.user} добавил "{self.recipe.ingredients}" в Избранное'

    class Meta(FavoriteAndShoppingCart.Meta):
        default_related_name = 'favorite'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(FavoriteAndShoppingCart):

    class Meta(FavoriteAndShoppingCart.Meta):
        default_related_name = 'shoppingcart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
