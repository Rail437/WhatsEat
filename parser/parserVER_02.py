import psycopg2
# from psycopg2 import Error
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os


def get_image(image_url):
    dir = '../src/main/resources/static/sample/img/'
    path = os.path.dirname(dir)
    if not os.path.exists(path):
        os.makedirs(path)
    img_data = requests.get(image_url).content
    filename = os.path.basename(image_url)
    path = os.path.join(path, filename)
    with open(path, 'wb') as handler:
        handler.write(img_data)
    return path


def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('a', class_='tile is-child with-hover')
    recipes_urls = []
    for elem in items:
        link = elem['href']
        recipes_urls.append(link)
    # print(recipes_urls)
    return recipes_urls


def print_dict(d):
    for title, inner_d in d.items():
        print(title)
        k = 'Изображение'
        print(f'\t{k}')
        print(f'\t\t{inner_d[k]}')
        k = 'Путь к изображению'
        print(f'\t{k}')
        print(f'\t\t{inner_d[k]}')
        k = 'Список ингредиентов'
        print(f'\t{k}')
        for i in inner_d[k]:
            print(f'\t\t{i}')
        k = 'Способ приготовления'
        print(f'\t{k}')
        for i in inner_d[k]:
            print(f'\t\t{i}')
        print('\n')


def parse_recipes(urls):
    dct = {}
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='has-text-weight-bold breadcrumb-title').get_text(strip=True)
        # timer = soup.find('div', class_='has-text-centered').get_text(strip=True)
        # print(timer)
        image = soup.find('picture', class_='recipe-cover-img')
        image = image.find('img')['src']
        path = get_image(image)
        ingredients = soup.find('div', 'card-content recipe')
        final_list = ingredients.find('ul')
        final_list = final_list.findAll('li')
        lst = []
        for item in final_list:
            item = str(item)
            item = item[4:len(item) - 5]
            # item.capitalize()
            lst.append(item)

        value_dict = {}
        value_dict['Список ингредиентов'] = lst
        value_dict['Изображение'] = image
        value_dict['Путь к изображению'] = path

        text = soup.find('ol', class_='p-t-2')
        text_list = text.findAll('li')
        new_list = text_list[:-1]

        new_list2 = []
        for i in new_list:
            i = str(i)
            num, step = i.split('</span>')
            num = num[num.rfind('>') + 1:].strip()
            step = step.strip()
            new_list2.append(f'<li>{step}\n')
        value_dict['Способ приготовления'] = new_list2
        dct[title] = value_dict
    print_dict(dct)
    return dct


def db_fill(lst, name):
    dir = '../src/main/resources/db/migration/V3_INSERT_VALUES.sql'
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указан при установке PostgreSQL
                                      password="qwerty",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="whatseat")

        cursor = connection.cursor()


        cursor.execute(f"""SELECT id FROM dish_category_entity WHERE title = '{name}'""")
        if cursor.rowcount <= 0:
            cursor.execute(f"""INSERT INTO dish_category_entity (TITLE) VALUES ('{name}') RETURNING id""")
            with open(dir, "a") as f:
                f.write(f"""INSERT INTO dish_category_entity (TITLE) VALUES ('{name}')""")


        category_id = cursor.fetchone()[0]
        print('category_id =', category_id)

        for key, value in lst.items():
            dish_title = key
            print(dish_title)
            dish_ingredients = '\n'.join(value['Список ингредиентов'])
            dish_cooking_method = '\n'.join(value['Способ приготовления'])
            dish_img_link = value['Изображение']
            dish_img_path = value['Путь к изображению']
            insert_dish_query = f"""INSERT INTO dish_entity (TITLE, DESCRIPTION, ingredients_list, img_path, DISH_CAT_ID) VALUES ('{dish_title}', '{dish_cooking_method}', '{dish_ingredients}','{dish_img_path}', '{category_id}') RETURNING id"""
            with open(dir, "a") as f:
                f.write(f"""INSERT INTO dish_entity (TITLE, DESCRIPTION, ingredients_list, img_path, DISH_CAT_ID) VALUES ('{dish_title}', '{dish_cooking_method}', '{dish_ingredients}','{dish_img_path}', '{category_id}')""")
            print('insert_dish_query =', insert_dish_query)
            cursor.execute(insert_dish_query)

            dish_id = cursor.fetchone()[0]

            dish_ingredients = value['Список ингредиентов']
            for ing in dish_ingredients:
                print(ing)
                num = ing.count(':')
                if num == 1:
                    product, quantity = ing.split(':')
                    request = f"""select exists(select * from product_entity where TITLE = '{product}')"""
                    cursor.execute(request)
                    responce = cursor.fetchone()[0]
                    # print(f'ing = {repr(ing)}, product = {repr(product)}')
                    if responce == True:
                        request2 = f"""SELECT id from product_entity where title = '{product}'"""
                        cursor.execute(request2)
                        product_id = cursor.fetchone()[0]
                    else:
                        insert_product_query = f"""INSERT INTO product_entity (TITLE) VALUES ('{product}') RETURNING id"""
                        cursor.execute(insert_product_query)
                        with open(dir, "a") as f:
                            f.write(f"""INSERT INTO product_entity (TITLE) VALUES ('{product}')""")
                        product_id = cursor.fetchone()[0]
                else:
                    product = ing
                    request = f"""select exists(select * from product_entity where TITLE = '{product}')"""
                    cursor.execute(request)
                    responce = cursor.fetchone()[0]
                    # print(f'ing = {repr(ing)}, product = {repr(product)}')
                    if responce == True:
                        request2 = f"""SELECT id from product_entity where title = '{product}'"""
                        cursor.execute(request2)
                        product_id = cursor.fetchone()[0]
                    else:
                        insert_product_query = f"""INSERT INTO product_entity (TITLE) VALUES ('{product}') RETURNING id"""
                        cursor.execute(insert_product_query)
                        with open(dir, "a") as f:
                            f.write(f"""INSERT INTO product_entity (TITLE) VALUES ('{product}')""")
                        product_id = cursor.fetchone()[0]

                insert_recipes_query = f"""INSERT INTO recipes (QUANTITY, dish_id, product_id) VALUES ('{quantity}','{dish_id}','{product_id}') RETURNING id"""
                with open(dir, "a") as f:
                    f.write(f"""INSERT INTO recipes (QUANTITY, dish_id, product_id) VALUES ('{quantity}','{dish_id}','{product_id}')""")
                #                 print('insert_product_query =', insert_product_query)

                cursor.execute(insert_recipes_query)
        connection.commit()
        # print("1 запись успешно вставлена")
        # # Получить результат
        # cursor.execute("SELECT * dish_category_entity")
        # record = cursor.fetchall()
        # print("Результат", record)

    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


if __name__ == '__main__':
    chicken_url = 'https://worldrecipes.eu/ru/category/bliuda-iz-kuricy'
    dinner_url = 'https://worldrecipes.eu/ru/category/bliuda-na-uzhin'
    dessert_url = 'https://worldrecipes.eu/ru/category/deserty'
    meatdishes_url = 'https://worldrecipes.eu/ru/category/miasnyje-bliuda'

    chilen_list = parse_url(chicken_url)
    dinner_list = parse_url(dinner_url)
    dessert_list = parse_url(dessert_url)
    meatdishes_list = parse_url(meatdishes_url)

    dct_chilen_list = parse_recipes(chilen_list)
    dct_dinner_list = parse_recipes(dinner_list)
    dct_dessert_list = parse_recipes(dessert_list)
    dct_meatdishes_list = parse_recipes(meatdishes_list)

    db_fill(dct_chilen_list, 'Блюда из курицы')
    db_fill(dct_dinner_list, 'Блюда на ужин')
    db_fill(dct_dessert_list, 'Десерты')
    db_fill(dct_meatdishes_list, 'Мясные блюда')

    print('...finished')
