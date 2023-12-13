import sqlite3

class DatabaseManager:
    def __init__(self, db_name="clothing_production.db"):
        self._conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self):
        with self._conn:
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Themes (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    theme_id INTEGER,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (theme_id) REFERENCES Themes(id)
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Orders (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users(id),
                    FOREIGN KEY (product_id) REFERENCES Products(id)
                )
            ''')

    # Ваши методы для создания, изменения, удаления и фильтрации данных

    def close(self):
        self._conn.close()

from sqlite3 import DatabaseManager

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db_manager = DatabaseManager()
        db_manager.save_user(self.username, self.password)
        db_manager.close()

    staticmethod
    def login(username, password):
        db_manager = DatabaseManager()
        # Логика для проверки учетных данных пользователя
        db_manager.close()

from database_manager import DatabaseManager

class Theme:
    def __init__(self, name):
        self.name = name

    def save(self):
        db_manager = DatabaseManager()
        db_manager.save_theme(self.name)
        db_manager.close()

from database_manager import DatabaseManager

class Product:
    def __init__(self, theme_id, name, price, quantity):
        self.theme_id = theme_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def save(self):
        db_manager = DatabaseManager()
        db_manager.save_product(self.theme_id, self.name, self.price, self.quantity)
        db_manager.close()

    staticmethod
    def get_all():
        db_manager = DatabaseManager()
        products = db_manager.get_all_products()
        db_manager.close()
        return products

from database_manager import DatabaseManager

class Order:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def save(self):
        db_manager = DatabaseManager()
        db_manager.save_order(self.user_id, self.product_id, self.quantity)
        db_manager.reduce_product_quantity(self.product_id, self.quantity)
        db_manager.close()

    staticmethod
    def get_all():
        db_manager = DatabaseManager()
        orders = db_manager.get_all_orders()
        db_manager.close()
        return orders

from user import User
from theme import Theme
from product import Product
from order import Order

def register_user(username, password):
    user = User(username, password)
    user.save()
    print("Пользователь успешно зарегистрирован!")

def login_user(username, password):
    User.login(username, password)
    print("Вход выполнен успешно!")

def create_theme(name):
    theme = Theme(name)
    theme.save()
    print("Тема успешно создана!")

def add_product(theme_id, name, price, quantity):
    product = Product(theme_id, name, price, quantity)
    product.save()
    print("Товар успешно добавлен!")

def view_products():
    products = Product.get_all()
    for product in products:
        print(f"ID: {product[0]}, Тема: {product[1]}, Название: {product[2]}, Цена: {product[3]}, Количество: {product[4]}")

def place_order(user_id, product_id, quantity):
    order = Order(user_id, product_id, quantity)
    order.save()
    print("Заказ успешно размещен!")

def view_orders():
    orders = Order.get_all()
    for order in orders:
        print(f"ID: {order[0]}, Пользователь: {order[1]}, Товар: {order[2]}, Количество: {order[3]}")

register_user("john_doe", "password")
login_user("john_doe", "password")

create_theme("Шапки")
create_theme("Футболки")

add_product(1, "Шапка красная", 10.99, 50)
add_product(1, "Шапка синяя", 9.99, 30)
add_product(2, "Футболка черная", 19.99, 20)

view_products()

place_order(1, 1, 2)
place_order(1, 2, 1)
place_order(2, 3, 3)

view_orders()