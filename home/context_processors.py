from home.catalog import CATEGORIES


def categories(request):
    """Makes the category list available to every template (used by the navbar)."""
    return {"categories": CATEGORIES}
