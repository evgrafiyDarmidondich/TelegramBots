from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from lessBot.database.models import Product

# функция добавления товара в бд
async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        image=data['image'],
    )
    session.add(obj)
    await session.commit()

# Фукция вывода всех товаров
async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()

# Функция вывода одного выбраного товара
async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar()

# Функция изменения одного товара
async def orm_update_product(session: AsyncSession, product_id: int, data):
    query = update(Product).where(Product.id == product_id).values(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        image=data['image'],
    )
    await session.execute(query)
    await session.commit()

# Функция удаления выбраного товара
async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()


