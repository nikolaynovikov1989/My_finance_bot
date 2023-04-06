create table budget(
    codename varchar(255) primary key,
    daily_limit integer
);

create table category(
    codename varchar(255) primary key,
    name varchar(255),
    is_base_expense boolean,
    aliases text
);

create table expense(
    id integer primary key,
    amount integer,
    created datetime,
    category_codename integer,
    raw_text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

insert into category(codename, name, is_base_expense, aliases)
VALUES
("coffee", "кофе", false, ""),
("dinner", "обед", true, "бизнес-ланч, перекус, обед"),
("eat", "еда", false, "магазин, продукты,"),
("restoran", "рестораны", false, "бар, кафе, ресторан, пицца, шашлык, роллы"),
("taxi", "такси", false, ""),
("public_transport", "транспорт", true, "электричка, метро, автобус"),
("bad_habits", "вредные-привычки", false, "алкоголь, вино, водка, пиво, сигареты, виски"),
("medicine", "медицина", false, "медицина, врачи, таблетки, лекарства, здоровье"),
("mortgage", "ипотека", true, "ипотека"),
("car", "машина", false, "автомобиль, машина, авто, тачка, автосервис"),
("clothes", "одежда", false, "обувь, кроссовки, куртка, шапка, ботинки"),
("internet", "cвязь", true, "интернет, телефон"),
("subscribes", "подписки", false, "приложения, сервер, vds, подписки"),
("family", "семья", false, "жена, жене, дети"),
("other", "остальное", true, "");

insert into budget(codename, daily_limit) values ('base', 500);
