import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    unique_names = set(p.name for p in products)
    avg_price = sum(p.price for p in products) / len(products)
    avg_weight = sum(p.weight for p in products) / len(products)
    avg_flammability = sum(p.flammability for p in products) / len(products)

    return (len(unique_names), avg_price, avg_weight, avg_flammability)


if __name__ == "__main__":
    print(inventory_report(generate_products()))
