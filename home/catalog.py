"""Shop catalogue: every category and product shown on the site.

Prices are in INR. Edit this file to add, remove or re-price items.
- "image" is a file name inside the static/ folder (leave it out to show the category icon instead)
- "from_price": True shows the price as "From ₹..." (for services with variable cost)
"""

CATEGORIES = [
    {
        "slug": "scoops-cones",
        "name": "Scoops & Cones",
        "icon": "fas fa-ice-cream",
        "tagline": "Freshly scooped, served in crunchy waffle cones.",
        "products": [
            {"name": "Gelato Scoop", "image": "websites.jpg", "price": 99, "size": "1 scoop",
             "desc": "Pick any flavour from our gelato counter, served in a cup or cone."},
            {"name": "Choco-Dip Twin Cones", "image": "two.jpg", "price": 129, "size": "2 cones",
             "desc": "Two vanilla cones drizzled with rich chocolate sauce."},
            {"name": "Waffle Cone Trio", "image": "1_ice-cream-websites.jpg", "price": 149, "size": "3 cones",
             "desc": "Vanilla, chocolate and strawberry, each in its own crunchy waffle cone."},
        ],
    },
    {
        "slug": "sundaes-cups",
        "name": "Sundaes & Cups",
        "icon": "fas fa-glass-whiskey",
        "tagline": "Loaded cups and sundaes with all the toppings.",
        "products": [
            {"name": "Softy with Toppings", "image": "12_.jpg", "price": 89, "size": "1 cup",
             "desc": "Smooth soft-serve topped with choco balls and fruit bites."},
            {"name": "Coffee & Caramel Bowl", "image": "4_ice-cream-websites.jpg", "price": 159, "size": "2 scoops",
             "desc": "Coffee-bean and salted-caramel scoops served in a bowl."},
            {"name": "Classic Sundae", "image": "ice-cream--61447025.jpg", "price": 169, "size": "1 glass",
             "desc": "Vanilla scoops with whipped cream, choco pearls and a crispy wafer roll."},
            {"name": "Cookies & Caramel Cup", "image": "15_ice-cream-websites-800x631.jpg", "price": 179, "size": "1 cup",
             "desc": "Creamy caramel ice cream loaded with crunchy cookie pieces."},
        ],
    },
    {
        "slug": "family-packs",
        "name": "Family Packs",
        "icon": "fas fa-box-open",
        "tagline": "Big packs made for sharing with the whole family.",
        "products": [
            {"name": "Classic Vanilla", "image": "download (2).jpg", "price": 199, "size": "1 litre",
             "desc": "Smooth, creamy vanilla that goes with every dessert."},
            {"name": "Fresh Strawberry", "image": "download (6).jpg", "price": 229, "size": "1 litre",
             "desc": "Made with real strawberry pulp for a fruity, pink treat."},
            {"name": "Rich Chocolate", "image": "download (4).jpg", "price": 249, "size": "1 litre",
             "desc": "Deep, dark chocolate ice cream for the whole family."},
            {"name": "Tutti Frutti", "image": "images (1).jpg", "price": 259, "size": "1 litre",
             "desc": "Colourful candied fruit bits in a creamy base."},
            {"name": "Roasted Almond", "image": "images.jpg", "price": 299, "size": "1 litre",
             "desc": "Vanilla base packed with crunchy roasted almonds."},
            {"name": "Choco-Vanilla Combo", "image": "download (3).jpg", "price": 429, "size": "2 x 1 litre",
             "desc": "One chocolate and one vanilla pack, best value for parties."},
        ],
    },
    {
        "slug": "parties-events",
        "name": "Parties & Events",
        "icon": "fas fa-birthday-cake",
        "tagline": "Let us bring the ice cream to your celebration.",
        "products": [
            {"name": "Custom Ice Cream Cake", "price": 899, "from_price": True, "size": "1 kg",
             "icon": "fas fa-birthday-cake",
             "desc": "Choose your flavours and message. Order 24 hours in advance."},
            {"name": "Ice Cream Making Class", "image": "unnamed.jpg", "price": 999, "size": "per person",
             "desc": "A 2-hour hands-on class: learn to churn your own ice cream at our parlour."},
            {"name": "Birthday Party Pack", "price": 1999, "from_price": True, "size": "serves 20",
             "icon": "fas fa-gift",
             "desc": "Assorted cups, cones and toppings delivered for kids' parties."},
            {"name": "Live Ice Cream Counter", "price": 7999, "from_price": True, "size": "up to 100 guests",
             "icon": "fas fa-store",
             "desc": "Our staff serve fresh scoops and sundaes at weddings and corporate events."},
        ],
    },
]


def all_products():
    """Every product, each tagged with its category."""
    for category in CATEGORIES:
        for product in category["products"]:
            yield {**product, "category": category}


def get_category(slug):
    return next((c for c in CATEGORIES if c["slug"] == slug), None)


def search(query):
    query = query.lower()
    return [p for p in all_products()
            if query in p["name"].lower() or query in p["desc"].lower()
            or query in p["category"]["name"].lower()]
