# ORM (object-relational mapping)-  технология программирования благодаря которой разработчики могут использовать язык програмированния для взоимодействия с реалиционной базой данных (PostgreSQL, MySQL, OracleDB).OSError
# Вместо того, чтобы писать сырые запросы на определённых SQL, вы будете писать код ООП на языке программирования. Это очень сильно ускоряет разработку приложения и бд, особенно на начальных.

from peewee import PostgresqlDatabase
db = PostgresqlDatabase(
    database = 'orm_db',
    user = 'user',
    password = '1',
    host = 'localhost',
    port = 5432
)

# db.connect()