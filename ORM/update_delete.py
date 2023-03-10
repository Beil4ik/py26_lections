from models import Product, Category


# обновление данных
# query = Product.update(price=500).where(Product.title=='adidas')
# print(query)
# query.execute()
# query = Product.update(price = (Product.price + Product.price * 0.5))#увеличиваем всем товарыфм цены
# query.execute()

# query = Product.update(price=200000).where(Product.category_id==1 and Product.category_id==3)
# query.execute()


# Удаление данных
# Удаление через запрос
# query = Product.delete().where(Product.id == 15)
# query.execute()

# Удаление через объект
# product = Product.get(id=14)
# print(product, product.title)
# product.delete_instance()

query = Product.delete().where(Product.id >= 9)
print(query)
query.execute()