import graphene
from graphene_django.types import DjangoObjectType
from .models import Beverages, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "description")

class BeverageType(DjangoObjectType):
    class Meta:
        model = Beverages
        fields = ("id", "name", "description", "category")
        
class Query(graphene.ObjectType):
    all_beverages = graphene.List(BeverageType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String())
    
    def resolve_all_beverages(root, info):
        return Beverages.objects.select_related("category").all()
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
    