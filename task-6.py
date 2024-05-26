
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):

    item_list = [{'name': name, 'cost': info['cost'], 'calories': info['calories']}
                 for name, info in items.items()]
    sorted_items = sorted(item_list, key=lambda x: x['calories'] / x['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item in sorted_items:
        if total_cost + item['cost'] <= budget:
            selected_items.append(item['name'])
            total_cost += item['cost']
            total_calories += item['calories']
        else:
            break
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = [{'name': name, 'cost': info['cost'], 'calories': info['calories']}
                 for name, info in items.items()]
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if item_list[i - 1]['cost'] <= w:
                dp[i][w] = max(item_list[i - 1]['calories'] + dp[i - 1][w - item_list[i - 1]['cost']],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_list[i - 1]['name'])
            w -= item_list[i - 1]['cost']
    
    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return selected_items, total_cost, total_calories

budget = 100

selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f'Selected items (Greedy): {selected_items_greedy}, Total cost: {total_cost_greedy}, Total calories: {total_calories_greedy}')

selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print(f'Selected items (DP): {selected_items_dp}, Total cost: {total_cost_dp}, Total calories: {total_calories_dp}')
