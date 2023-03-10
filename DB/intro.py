# PostgreSQL - система управления базами данныхс(СУБД/ DBMS)
#  это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри БД(CRUD).

# Posgres - сама база данных, она реалиционная, то есть данные храняться в виде таблиц  и таблицы имеют  связи между собой (relations)&
# SQL(Structured Query Language) - декларативный язык структурированных запросов, он применяетться для создания  и управления данными
#===================================================
# типы полей в postgres
# 1. Numeric types:
# a. smallint (2 bytes) -> -32767 to 32767
# b. integer (4 bytes) -> -2147000 t 2147000
# c. bigint(8 bytes) -> ....
# d. serial (4 bytes) -> auto-increment(integer, 1-214700)
# c. real(4 bytes) - число с плавающей точкой, вещественное число
# f. double precision (8 bytes) - real но только с двойной точностью
# 2. Character types:
# a. varchar(кол-во 255)- можем указатть макс кол-во символов в ручную. Если мы указали макс кол-во символов в 50, а заполнили только 10, то остальные 40 не заполняться
# b. char(255) - еслт если не заполним все символы то остальные заполняться пробелами
# с. text - неограниченное кол-во символов
# 3. Boolean types:
# #boolean(1 bytes) -> True/False
# 4. date - календарная дата (год.месяц.день)
# 5. location (point) - координаты
#---------------------------------------------------
# Связи между таблицами(relations):
    # 1. Один к одному(One-to-one) - человек паспорт
    # 2. Один ко многим() - человек и банковские карты


# constraints(Ограничения):
#         1.CHECK <column> > 5
#         2. UNIQUE - только уникальные значения
#         3. NOT NULL - обязательно к заполнению
#         4. PRIMARY KEY (для установки идентификатора данных в таблице)
#         5. FOREIGN KEY (для установки связи между таблицами)
#         6. DEFAULT <value>- добавляет дефолтное значение
#         Добавление к таблице кторая уже есть
#         ALTER TABLE cities ALTER COLUMN location SET NOT NULL;
#         ALTER TABLE products ADD CONSTRAINT <name_of_constr> UNIQUE (name);
#         ALTER TABLE cities ALTER COLUMN location SET NOT NULL;
#-----------------------------------------------------
# ubuntu: sudo -u postgres psql
# mac: psql postgres
# psql -> для входа через своего юзера
# \q -> выход из СУБД
# \du -> список свех юзеров
# \l -> список всех баз данных
# \c <dbname> -> команда для подключения к бд
#     \dt -> список таблиц в бд
#     \d <table> -> подробная информация про таблицу
# ИМПОР данных при помощи файла 
# psql -U <username> -d <database> -f <path_to_file>
# CREATE DATABASE <dbname>; -> команда для создания бд 
# CREATE TABLE <tablename> (
#     <name_of_column><type>
#     <name_of_column><type>
# ); команда для создания таблицы
# пример:
# СREATE TABLE weather (
#     city varchar(80)
#     temp_lo int,
#     temp_hi int,
#     prcp real,
#     date date
# );
# DROP DATABASE <name_of_db>; - удаление бд
# DROP TABLE <name_of_table>; - удаление таблицы
# DROP ... -> удаление
# CREATE USER <username> WITH PASSWORD '<password>'; -> команда для создания юзера
# ALTER USER <username> WITH SUPERUSER; команда для изменения статуса юзера на суперюзера
# SELECT <column> FROM <table>; команда для получения данных
# WHERE: используеться для фильтрации по полям. будут выводиться только те данные которые соответствуют условию WHERE
#Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему-либо'
# SELECT * FROM products WHERE meat = 'Becon'
# SELECT * FROM products WHERE meat in ('Becon'
# AND:  оператор и, для множесва уловий 
# Операторы сравнения: >, <, >=, <=, =, <>
# BETWEEN: Условие между 
# SELECT * FROM products WHERE id BETWEEN 3 and 8;
# SELECT * FROM produts WHERE id <= 8 and >= 3;
# ORDER BY : сортировка по входящим данным по  убыванию или возрастанию
            #ASC(по возрастанию) и DESC(по убывванию)
# SELECT <row> FROM <table> ORDER BY <row> [ASC/DESC]
# LIMIT:  позволяет нам вернуть данные в ограниченном колличечтве 
# SELECT <row> FROM <table> LIMIT 1;
# LIKE: выводит результат который соответствует введенному шабллону. Зависит от регистра
# ILIKE: не зависит от регистра
# Cинтаксис: SELECT * FROM products WHERE name LIKE 'S%';
# DISTINCT: Позволяет нам убрать  дубликаты и возвращает тоько уникальные значения 
# SELECT DISTINCT name FROM product
# SELECT first_name  ' '  last_name FROM customer;

# INSERT INTO <tablename> (<columns>) VALUES
#     # (datas_to_comuns); - команда для заполнения данных в таблицу
    
#     INSERT INTO cities (name, location)
#     VALUES ('Bishkek', '(42.52, 74.59)')

# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>; - команда для обнавления данных 
# Указываем после WHERE то какой объект обновить

# DELETE FROM <tablename> WHERE <column> = <data>; - команда для удаления
# СREATE USER <username> WITH PASSWORD '<password>'; - команда для создания юзера```

# GROUP BY разделяет данные, которые мы получаем в SELECT, при этом группируя их по определённому призраку и теперь для каждой группы можно использовать агрегатную функцию

# HAVING: он работает также, как и WHERE, только с операторам GROUP BY

'-------------------------------------------------------------------------'

# JOIN - оператор, который позволяет в запросах селект брать данные из нескольких страниц

# INNER JOIN() - достаются только те записи, у которых есть связь\

# FULL JOIN - достаются все записи с обеих страниц

# LEFT JOIN - достаёт все записи с левой страницы, а с правой только те записи, у которых есть связь с левой таблицей

# RIGHT JOIN - достаёт все записи с правой страницы, а с левой только те записи, у которых есть связь с правой таблицей

# * где "левая" таблица это та таблица, которая записана до join, а "правая" таблица это таблица, которая записана после join