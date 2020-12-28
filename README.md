# Final Project
 
## Пиццерия 🍕
 
 - Все рецепты описаны классами
 
 - Есть два размера пиццы: is_large: L - True, XL - False
 
 - Метод dicts() выводит рецепт в виде словаря
 
 - Метод _eq_() сравнивает пиццы
 
 - Click содержит 2 команды: order, menu
 
 - flake8, black
 
 ## Menu 🥡
 
 Название пиццы: ингредиенты: граммы
 
 - Margherita 🧀 : tomato_sauce: 60, mozzarella: 150, tomatoes: 50
 
- Pepperoni 🍕 : tomato_sauce: 40, mozzarella: 150, pepperoni: 170

- Hawaiian 🍍 : tomato_sauce: 40, mozzarella: 150, chicken: 100, pineapples: 90

 
 ## Запуск программы
 
#### Вывести меню:
 
 python exam.py menu
 
#### Сделать заказ:
 
 python exam.py order pepperoni
 
#### Слелать заказ и выбрать способ доставки:
 
 Самовывоз:  python exam.py order pepperoni --pick 
 
 Курьер: python exam.py order pepperoni --delivery
 
#### Запустить тесты:
 
 python -m pytest test.py
 
 
 
