from backend.recipes.models import Tag
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Создаем tags'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#E26C2D', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#49B64E', 'slug': 'dinner'},
            {'name': 'Ужин', 'color': '#8775D2', 'slug': 'supper'}]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Tags загружены'))
