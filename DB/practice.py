'практика для блога'

# create table blogger (
# id serial primary key,
# name varchar(50));

# create table post (
# id serial primary key,
# owner_id int references blogger(id),
# body text,
# created_at date);

# заполнение данных
# insert into blogger(name) values ('John'), ('Sultan'), ('Jamie');

# insert into post (owner_id, body, created_at) values (1, 'My first blog. Hello world!', '2023.02.24'), (1, 'Today is good day!', '2023.02.01'), (1, 'today is my bad day', '2022.03.05');

# insert into post (owner_id, body, created_at) values (3, 'Lanister is the best', '2023.02.01'), (3, 'I will be bakc', '2022.03.05');

# insert into post (owner_id, body, created_at) values (2, 'I\m good man', '2022.03.05');

# shoop
# CREATE TABLE customer (
# id serial primary key,
# name varchar(50));

# CREATE TABLE product (
# id serial primary key,
# title varchar(50),
# price decimal);

# CREATE TABLE card (
# id serial primary key,
# customer_id int references customer(id),
# product_id int references product(id));

'запонение таблиц'
# INSERT INTO customer (name) values ('Sultan'), ('John'), ('Jamie');

# INSERT INTO product(title, price) values ('KKS', 340),
# ('Iphone 14', 70000),
# ('potato', 200),
# ('anas', 400),
# ('ice_cream', 120);

# INSERT INTO cart(customer_id, product_id) values (1, 1), (1, 1), (1, 1), (1,3), (1, 3), (2, 2), (2, 2), (3, 4), (3, 5);

# АГРЕГАТНЫЕ ФУНКЦИИ
# SUM - функция, которая считывающая сумму всех записей в сгруппированном поле
# пример из shop
# SELECT c.name, SUM(p.price) AS total_price
# FROM product AS p JOIN cart ON p.id = cart.product_id
# JOIN customer AS c ON c.id = cart.customer_id
# GROUP BY c.name;

# ARRAY_AGG - объединяет записи сгруппированного поля в массив

# SELECT b.name, ARRAY_AGG(post.body) FROM blogger AS b
# JOIN post ON

'-------------------------------------------------------------------------'
# Shakespeare

'1. Вытащить все произведения в которых sourse = Moby и кол-во параграфов меньше 100'
# SELECT title, source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100;

'2. Найти кол-во глав в каждом произведении'
# SELECT count(*), work.title FROM chapter
# JOIN work ON work.workid = chapter.workid
# GROUP BY work.title ORDER BY COUNT(*);

'3. Найти сколько произведений относятся к каждому жанру'
# SELECT COUNT(*), genretype FROM work
# GROUP BY genretype ORDER BY count;

'4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений'
# SELECT title, totalparagraphs FROM work;

'5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания'
# SELECT ch.charname, MAX(ch.speechcount)
# FROM character_work AS ch_w
# JOIN character AS ch ON ch_w.charid = ch.charid
# JOIN work ON ch_w.work = work.workid
# WHERE ch.speechcount > 200 ORDER BY work.year;

'6. Вытащить героя, который чаще всех появляется в произведениях'