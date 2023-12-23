import datetime
from fastapi import FastAPI, HTTPException
import database as db
import models
from typing import List
import random
from random import randint



app = FastAPI()


@app.get("/")
def root():
    return {"Вы на главной странице"}


@app.get("/create_users/{count}")
async def create_note(count: int):

    list_surname = ['Мельникова', 'Иванова', 'Буракшаева', 'Фурсова', 'Сапсай', 'Богословский', 'Самбикина', 'Шпак', 'Пименов', 'Сигида']
    list_name = ['Елизавета', 'Иван', 'Артем', 'Юлия', 'Ангелина', 'Максим', 'Валерия', 'Елизавета', 'Анастасия', 'Мария']
    list_email = ['tradition@gmail.com', 'motheroperation@inbox.ru', 'minute@gmail.com', 'productoperation@inbox.ru', 'school@mail.ru', 'operation@inbox.ru', 'coach@gmail.com', 'copyschool@mail.ru', 'realityschool@gmail.com', 'recordschool@mail.ru']
    list_password = ['qAMpOmQbxi', 'k27BqmucT0', 'o2iR5QkDGv', 'h14lxn4tBW', '9zsveIxxlM', 'lc7xWttrDn', 'rIDhh29Emu', 'g4cMxOwMIb', 'sm5wMDKY0s', 'vnvL0lI2pY']
    
    for i in range(count):
        article = db.users.insert().values(name=random.choice(list_name), surname=random.choice(list_surname), email=random.choice(list_email),
                                         password=random.choice(list_password))
        await db.database.execute(article)
    return {'Сообщение': f'{count} Создано пользователей'}


@app.get("/create_products/{count}")
async def create_note(count: int):

    list_products = ['Брокколи', 'Морковь', 'Шпинат', 'Чеснок', 'Свекла', 'Спаржа', 'Сельдерей']
   

    for i in range(count):
        article = db.products.insert().values(title=random.choice(list_products), description=f'Овощь',
                                            price=randint(100, 500))
        await db.database.execute(article)
    return {'Сообщение': f'{count} Создано продуктов'}


@app.get("/create_orders/{count}")
async def create_note(count: int):
    for i in range(count):
        article = db.orders.insert().values(user_id=randint(1, 10), prod_id=randint(1, 10), status="Создан",
                                          date=datetime.datetime.now())
        await db.database.execute(article)
    return {'Сообщение': f'{count} Создано заказов'}




@app.get("/users/", response_model=List[models.UserRead])
async def read_users():
    article = db.users.select()
    return await db.database.fetch_all(article)


@app.get("/products/", response_model=List[models.ProductRead])
async def read_products():
    article = db.products.select()
    return await db.database.fetch_all(article)


@app.get("/orders/", response_model=List[models.OrderRead])
async def read_orders():
    article = db.orders.select()
    return await db.database.fetch_all(article)




@app.get("/users/{user_id}", response_model=models.UserRead)
async def read_user(user_id: int):
    article = db.users.select().where(db.users.c.id == user_id)
    user = await db.database.fetch_one(article)
    if user is None:
        raise HTTPException(status_code=404, detail="Отсутствует пользователь в списке")
    return user


@app.get("/products/{product_id}", response_model=models.ProductRead)
async def read_product(product_id: int):
    article = db.products.select().where(db.products.c.id == product_id)
    product = await db.database.fetch_one(article)
    if product is None:
        raise HTTPException(status_code=404, detail="Отсутствует продукт в списке")
    return product


@app.get("/orders/{order_id}", response_model=models.OrderRead)
async def read_order(order_id: int):
    article = db.orders.select().where(db.orders.c.id == order_id)
    order = await db.database.fetch_one(article)
    if order is None:
        raise HTTPException(status_code=404, detail="Отсутствует заказ в списке")
    return order



@app.put("/users/{user_id}", response_model=models.UserRead)
async def update_user(user_id: int, new_user: models.UserCreate):
    article = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(article)
    return {**new_user.dict(), "id": user_id}


@app.put("/products/{product_id}", response_model=models.ProductRead)
async def update_product(product_id: int, new_product: models.ProductCreate):
    article = db.products.update().where(db.products.c.id == product_id).values(**new_product.dict())
    await db.database.execute(article)
    return {**new_product.dict(), "id": product_id}


@app.put("/orders/{order_id}", response_model=models.OrderRead)
async def update_order(order_id: int, new_order: models.OrderCreate):
    article = db.orders.update().where(db.orders.c.id == order_id).values(**new_order.dict())
    await db.database.execute(article)
    return {**new_order.dict(), "id": order_id}



@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    article = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(article)
    return {'Сообщение': 'Пользователь удалён'}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    article = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(article)
    return {'Сообщение': 'Продукт удалён'}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    article = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(article)
    return {'Сообщение': 'Заказ удалён'}


# Для запуска используем команду: uvicorn main:app --reload