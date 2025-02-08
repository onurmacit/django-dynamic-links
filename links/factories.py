import factory
from .models import Item

class ItemFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Item instances.
    """
    class Meta:
        model = Item  

    title = factory.Faker("sentence")  
    description = factory.Faker("text")  