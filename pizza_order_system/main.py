from services.pizza_base_service import PizzaBaseService
from services.ingredient_service import IngredientService
from services.topping_service import ToppingService
from services.pizza_service import PizzaService
from services.pizza_order_service import PizzaOrderService

def initialization():
    pizza_base_service = PizzaBaseService()
    pizza_base1 = pizza_base_service.add_base("Plain", 100.0)
    pizza_base2 = pizza_base_service.add_base("Thin_Crust", 80.0)

    ingredient_service = IngredientService()
    i1 = ingredient_service.add_ingredient("Onion", 5.0)
    i2 = ingredient_service.add_ingredient("Tomato", 5.0)
    i3 = ingredient_service.add_ingredient("Corn", 2.5)

    topping_service = ToppingService()
    t1 = topping_service.add_topping(i1, 2)
    t2 = topping_service.add_topping(i2, 2)
    t3 = topping_service.add_topping(i3, 3)

    pizza_service = PizzaService()
    pizza = pizza_service.add_pizza(pizza_base1, [t1])
    
    return pizza


if __name__ == "__main__":
    
    pizza = initialization()

    pizza_order_service = PizzaOrderService()
    pizza_order = pizza_order_service.add_order(pizza, 2)

    print(pizza_order_service.get_order_price(pizza_order.get_id()))