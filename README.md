# Lanex

A web application that enables users to connect with one another to exchange languages, helping to improve language knowledge and allow users to make their own language requests to help discover potential language buddies.
the way

## Setting up: Initial stage
In making this web application, several packages are required to be installed for it function correctly. Before beginning, make sure to clone the repository and access the proper directory.

```
$ git clone https://github.com/MoradEnCours/WAD2_Group_Project
$ cd lanex
```

### Setting up: Creating and activating the virtual environment
Assuming Anaconda is being used, enter the following into the command prompt:
```
$ conda create -n lanex python=3.8.0
$ conda activate lanex
```

### Setting up: Installing the necessary package dependencies
To make sure of using the right packages and versions required to run the web application, install them by entering the following into the command prompt:

```
(lanex)$ pip install -r requirements.txt
```

### Setting up: Making migrations and migrating
Make sure that the current directory is where file manage.py is located and enter the following in the command prompt:

```
(lanex)$ python manage.py makemigrations lanex
(lanex)$ python manage.py migrate
```

(Optional) For a sample population script to try out, it is recommended to run the population script by entering the following into the command prompt.

```
(lanex)$ python populate_lanex.py
```

## Running the web application
It's simple. Enter the following line into the command prompt:

```
(lanex)$ python manage.py runserver
```

After that, access the following link to begin browsing the web application: http://127.0.0.1:8000/

### Additional: Running tests
Tests are provided, and to run them simply enter the following into command prompt:

```
(lanex)$ python manage.py test lanex
```

## Primary tools made use of in developing the web application as well as resources and tutorials followed to help implement features
* [Django](https://github.com/django/django) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Pillow](https://github.com/python-pillow/Pillow) - A Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.
* [Django-Extensions](https://github.com/django-extensions/django-extensions) - A collection of custom extensions for the Django Framework. These include management commands, additional database fields, admin extensions and much more.
* [Django-Location-Field-Repo+Docs](https://github.com/caioariede/django-location-field ; https://django-location-field.readthedocs.io/en/latest/) - Provides model and form fields, and widgets that allow users to easily pick locations and store in the database.
* [OpenStreetMaps+Leaflet.js-library](https://wiki.openstreetmap.org/wiki/Leaflet) - Used in Django-location-field to assist with functionality of mapping a location when adding language requests.
* [Django-Registration-Repo+Docs+CodenongTutorial](https://github.com/ubernostrum/django-registration ; https://django-registration.readthedocs.io/ ; https://www.codenong.com/5658745/) - An extensible application providing user registration functionality for Django-powered Web sites
* [jQuery](https://github.com/jquery/jquery) - A lightweight, "write less, do more", JavaScript library.
* [Bootstrap](https://github.com/twbs/bootstrap) - the most popular CSS Framework for developing responsive and mobile-first websites.
* [Bootdey](https://www.bootdey.com/snippets/view/Social-post)
* [Bootstrap-examples](https://getbootstrap.com/docs/4.2/examples/dashboard/)
* [Bootsnipp](https://bootsnipp.com/snippets/7nk08) - An element gallery for web designers and web developers.
* [Tango-With-Django-Textbook](https://www.tangowithdjango.com/) - Recommended course textbook, including main 20 chapters and section for appendices.
* [Creating-Comments-System-Tutorial](https://djangocentral.com/creating-comments-system-with-django/) - Guide for building a basic commenting system for a Django 2.X app, which lets readers add comments on posts.
* [Query-Form-Processing-Tutorial](https://djangocentral.com/creating-comments-system-with-django/)  - Chapter 7 from the Django book providing useful demonstrations for form processing including query searching.
* [BIng-Search](https://docs.microsoft.com/en-gb/rest/api/cognitiveservices/bing-web-api-v7-reference) - Provides the ability to embed search results from the Bing search engine within an application

## Final words from the team:
Merci, enjoy, buenos días y sayanora!