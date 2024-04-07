Design a system which can serve:
1. Customer can see all available bases with price
2. Customer ca see all avalaible toppings with price
3. customer can place pizza order with custom base & topping


Solution :

# Entities :
1. Pizza :
    - id
    - base
    - List[toppings]
    - price

2. Base
    - name
    - price

3. Topping
    - id
    - ingredient
    - qty
    - price

4. Ingredient
    - name
    - pricePerUnit

5. PizzaOrder :
    - id
    - pizza
    - qty
    - taxPrice

# Services

1. Base Service
    - get_all_bases()
    - get_base_by_name(name)
    - add_base(name, price)

2. Ingredient service
    - get_all_ingredients()
    - add_ingredient(name, price_perUnit)
    - get_ingredient_by_name(name)

3. Toppping Service
    - get_all_toppings()
    - add_topping(ingredient, qty)

4. Pizza Service
    - add_pizza(base, List[toppings])

5. Pizza Order serivce
    - add_order(pizza, qty)
    - get_order_price()