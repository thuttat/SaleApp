from eapp.models import Category, Product

def load_categories():
    return Category.query.all()

def load_products(cate_id=None,kw=None,page=1):
    query = Product.query

    return query