def get_recipe_price(prices, optionals=[], **ingredients):
    sum = 0
    for ingredient, amount in ingredients.items():
        sum += prices[ingredient] * amount / 100

    return sum


print(get_recipe_price({'chocolate': 18, 'milk': 8},optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
