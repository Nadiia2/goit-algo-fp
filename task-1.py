from pulp import *

lemonade = LpVariable("Lemonade_units", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_juice_units", lowBound=0, cat='Integer')

prob = LpProblem("Maximize_production", LpMaximize)

prob += lemonade + fruit_juice, "Total_production"

prob += 2 * lemonade + fruit_juice <= 100, "Water_constraint"
prob += lemonade <= 50, "Sugar_constraint"
prob += lemonade <= 30, "Lemon_juice_constraint"
prob += 2 * fruit_juice + lemonade <= 40, "Fruit_puree_constraint"

prob.solve()

print("Status:", LpStatus[prob.status])
print("Total production:", value(prob.objective))
print("Lemonade units:", value(lemonade))
print("Fruit juice units:", value(fruit_juice))
