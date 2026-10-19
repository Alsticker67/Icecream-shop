# Ice Creams $hop

An ice cream shop website built with Django and Bootstrap 4.

## Features

- **Home page**: hero banner, featured products, browse-by-category tiles and a "why choose us" section
- **Menu & services** in four categories: Scoops & Cones, Sundaes & Cups, Family Packs, and Parties & Events
- **Search** across every product from the navbar
- **Contact form**: messages are saved to the database and can be viewed in the Django admin
- **Responsive layout** for desktop, tablet and phone
- All prices are in Indian Rupees (₹)

## Getting started

Requires Python 3.10 or newer.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000> in your browser.

To use the admin panel at `/admin/`, first create an admin account:

```bash
python manage.py createsuperuser
```

## Editing products

Every category and product lives in [`home/catalog.py`](home/catalog.py). Add, remove or re-price items
there and the menu, navbar dropdown and home page all update automatically. Product images go in the
`static/` folder.

## Running the tests

```bash
python manage.py test home
```

## Project structure

```
Hello/              Django project settings and root URLs
home/
  catalog.py        Product categories and prices
  views.py          Page views
  models.py         Contact form model
  tests.py          Automated tests
templates/
  css.html          Base layout (navbar, footer, shared styles)
  index.html        Home page
  services.html     Menu / category pages
  about.html, contact.html, login.html, 404.html
static/             Images
```

## Deploying

The default settings are for local development. Before deploying, set these environment variables:

| Variable | Example |
|---|---|
| `DJANGO_SECRET_KEY` | a long random string |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | `yourdomain.com,www.yourdomain.com` |
