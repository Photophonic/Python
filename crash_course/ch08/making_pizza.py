import pizza as p
from pizza import make_pizza as mp
from pizza import make_pizza
import pizza

# import NAME allows python to call a separate function and used it in this file
# using the imported function is similar to pl/sql, file.function_name
pizza.make_pizza('Medium', 'Cheese', 'Honey Wheat Crust', 'Sausage')

# this makes every funciton of the imported module available.

# to import a specific funtion in a module, use from x import x.function_name
make_pizza('Large', 'Cheese', 'pineapple', 'ham', 'sauce')

# imported funcitons can have an alias...
mp('small', 'honey wheat', 'chicken', 'mushrooms')

# or whole modules can have an alias
p.make_pizza('Medium', 'Cheese', 'Honey Wheat Crust', 'Sausage')
