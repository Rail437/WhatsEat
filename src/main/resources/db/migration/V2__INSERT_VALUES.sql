
insert into hibernate_sequence values ( 1 );
insert into hibernate_sequence values ( 1 );

insert into product_category_entity values(default, 'Молочное и яйца');
insert into product_category_entity values(default, 'Овощи и зелень');
insert into product_category_entity values(default, 'Фрукты и ягоды');
insert into product_category_entity values(default, 'Хлеб и выпечка');
insert into product_category_entity values(default, 'Сыр');
insert into product_category_entity values(default, 'Колбаса и сосиски');
insert into product_category_entity values(default, 'Мясо');
insert into product_category_entity values(default, 'Рыба и морепродукты');

insert into dish_category_entity values(default, 'Завтрак');
insert into dish_category_entity values(default, 'Обед');
insert into dish_category_entity values(default, 'Ужин');
insert into dish_category_entity values(default, 'Десерт');

insert into product_entity values(default, 'молоко', 1);
insert into product_entity values(default, 'яйцо куриное', 1);
insert into product_entity values(default, 'сливки', 1);
insert into product_entity values(default, 'творог', 1);
insert into product_entity values(default, 'помидор', 2);
insert into product_entity values(default, 'огурец', 2);
insert into product_entity values(default, 'брокколи', 2);
insert into product_entity values(default, 'картофель', 2);
insert into product_entity values(default, 'яблоко', 3);
insert into product_entity values(default, 'клубника', 3);
insert into product_entity values(default, 'банан', 3);
insert into product_entity values(default, 'белый хлеб', 4);
insert into product_entity values(default, 'мука пшеничная', 4);
insert into product_entity values(default, 'лаваш', 4);
insert into product_entity values(default, 'фета', 5);
insert into product_entity values(default, 'моцарелла', 5);
insert into product_entity values(default, 'рикотта', 5);
insert into product_entity values(default, 'пармезан', 5);
insert into product_entity values(default, 'сыр', 5);
insert into product_entity values(default, 'вареная колбаса', 6);
insert into product_entity values(default, 'копченая колбаса', 6);
insert into product_entity values(default, 'ветчина', 6);
insert into product_entity values(default, 'бекон', 6);
insert into product_entity values(default, 'индейка', 7);
insert into product_entity values(default, 'курица', 7);
insert into product_entity values(default, 'свинина', 7);
insert into product_entity values(default, 'говядина', 7);
insert into product_entity values(default, 'икра', 8);
insert into product_entity values(default, 'креветки', 8);
insert into product_entity values(default, 'лосось', 8);
insert into product_entity values(default, 'окунь', 8);

insert into dish_entity values(default, 'сырники', 'Творог переложите в небольшую стеклянную или пластиковую миску.
							   Добавьте щепотку соли, одно яйцо, 3 ст. л. сахара. Перемешайте их до получения однородной массы.
							   К полученной творожной смеси добавьте 3 ст. л. пшеничной муки. Смочите руки небольшим количеством подсолнечного масла и скатайте из творожной массы небольшие шарики.
							   Теперь запанируйте сырники в муке. Обжаривайте сырники 2-3 минуты с каждой строны.', 1, 1);

insert into dish_entity values(default, 'Яйца всмятку', 'Положите яйца в кастрюлю и залейте кипятком. Подержите 10 минут, затем слейте воду, снова залейте кипятком и достаньте через 2–3 минуты.', 1, 1);

insert into dish_entity values(default, 'Карамелизованный бекон', 'Бекон нарежьте полосками и выложите в огнеупорную форму. Посыпьте сахаром и перемешайте.
							   Поставьте в разогретую до 180 градусов духовку, пока бекон не станет темно-золотистого цвета, перевернув один раз, примерно на 16 минут.
							   Затем переложите на решетку и оставьте остывать. Подавайте комнатной температуры.', 1, 1);

insert into dish_entity values(default, 'Куриная грудка с картофелем', 'Хорошо перемешать куриное филе, лук и картофель с соевым соусом. Добавить оливковое масло, паприку и черный молотый перец. Обычно соевый соус достаточно соленый, поэтому следует посолить блюдо с учетом этого факта.
Оставить овощи с мясом мариноваться на 30 минут. Духовку разогреть до 180 градусов и запекать курицу с картофелем 30 минут, периодически перемешивая.', 2, 2);

insert into dish_entity values(default, 'Жареные креветки с чесноком и соевым соусом', 'Обжарить креветки на сливочном масле на большом огне.
							   Когда масло растает, добавить соевый соус. Продолжать готовить креветки на максимальном огне, это важно. Когда соус закипит, добавить соль, свежемолотый черный и красный перец, сушеный укроп. Затем добавить чеснок', 2, 3);


insert into dish_entity values(default, 'Смузи', 'Взбить банан и клубнику в блендере с добавлением молока до однородной констистенции.', 1, 4);
insert into dish_entity values(default, 'Ролл с индейкой', 'Лаваш смазать рикоттой, добавить нарезанные овощи, индейку,
							   поджаренную на гриле, сверху посыпат тертым сыром и завернуть лаваш', 2, 2);
insert into dish_entity values(default, 'Французские тосты', 'Взбить 2 яйца в миске со сливками и сахаром.
							   Окунуть в смесь тосты и общарить на сливочном масле до золотистой корочки. Подавать с клубникой и сахарной пудрой.', 1, 1);

insert into dish_entity values(default, 'Брускетта', 'Поджарить тосты, смазать их рикоттой, выложить сверху лосось, помидор и свежую зелень.', 1, 2);

insert into dish_entity values(default, 'Брокколи в сливочном соусе', 'Для соуса на сковороде растопите сливочное масло. Всыпьте муку и мускатный орех.
							   Добавьте сливки, перемешайте до однородности, добавьте к соусу брокколи. Готовить вместе 2-3 минуты.', 2, 2);
insert into dish_entity values(default, 'Запеченые яблоки', 'Вырежте сердцевину яблок, положите внутрь смеь рикотты и корицы, можно добавить орехи и сахар.
							   запекайте яблоки в духовке около 20 минут при температуре 180 градусов', 2, 4);
insert into dish_entity values(default, 'Омлет с сыром фета и помидорами', 'Взбейте 2 яйца с солью. Вылейте смесь на сковородку,
							   обжаривайте, помешивая, в течении 2 минут, добавьте помидоры и сыр фета. Подавать с зеленью.', 1, 1);
insert into dish_entity values(default, 'Лосось в лимонном соке с брокколи под сыром', 'Филе лосося нарезать небольшими кусочками, сбрызнуть лимонным соком, добавить перец, соль и отставить на полчаса. Через 30 минут филе залить водой (горячей) и варить на маленьком огне примерно 10 минут. Брокколи также отдельно от рыбы отварить.
							   Сливки взбить с молоком, яйцами и сыром, посолить, прибавить мускатный орех и перец. Форму для запекания промазать маслом, уложить слоями рыбу и брокколи, и залить взбитой смесью. Запекать рыбу под сыром в духовке около 20 минут (220 градусов).', 2, 3);

insert into recipes values(default, 2, 1, '1 шт');
insert into recipes values(default, 13, 1, '25 гр.');
insert into recipes values(default, 4, 1, '400 гр.');
insert into recipes values(default, 2, 2, '2 шт');
insert into recipes values(default, 23, 3, '100 гр.');
insert into recipes values(default, 25, 4, '500 гр.');
insert into recipes values(default, 8, 4, '600 гр.');
insert into recipes values(default, 29, 5, '500 гр.');
insert into recipes values(default, 11, 6, '1 шт.');
insert into recipes values(default, 10, 6, '500 гр.');
insert into recipes values(default, 14, 7, '1 лист');
insert into recipes values(default, 5, 7, '1 шт.');
insert into recipes values(default, 6, 7, '1 шт.');
insert into recipes values(default, 19, 7, '30 гр.');
insert into recipes values(default, 17, 7, '20 гр.');
insert into recipes values(default, 24, 7, '100 гр.');
insert into recipes values(default, 2, 8, '2 шт.');
insert into recipes values(default, 3, 8, '100 мл.');
insert into recipes values(default, 12, 8, '2 тоста');
insert into recipes values(default, 10, 8, '50 гр.');
insert into recipes values(default, 17, 9, '20 гр.');
insert into recipes values(default, 5, 9, '1 шт.');
insert into recipes values(default, 30, 9, '50 гр.');
insert into recipes values(default, 7, 10, '400 гр.');
insert into recipes values(default, 3, 10, '100 мл.');
insert into recipes values(default, 13, 10, '20 гр.');
insert into recipes values(default, 9, 11, '2 шт');
insert into recipes values(default, 17, 11, '50 гр.');
insert into recipes values(default, 2, 12, '2 шт');
insert into recipes values(default, 15, 12, '40 гр.');
insert into recipes values(default, 5, 12, '1 шт');
insert into recipes values(default, 30, 13, '500 гр.');
insert into recipes values(default, 7, 13, '500 гр.');
insert into recipes values(default, 3, 13, '100 мл.');
insert into recipes values(default, 19, 13, '125 гр.');
insert into recipes values(default, 1, 13, '200 мл.');
insert into recipes values(default, 2, 13, '4 шт');

