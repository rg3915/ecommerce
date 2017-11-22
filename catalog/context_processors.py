from .models import Category


def categories(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return ctx
