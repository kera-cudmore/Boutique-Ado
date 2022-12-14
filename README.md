# Boutique Ado

![Boutique Ado Banner](https://user-images.githubusercontent.com/92253071/196004237-151b3755-3e6b-4436-b5ee-e6a0c75ffce1.png)

Boutique Ado is a full stack e-commerce site utilising Django, stripe payments and AWS.

Link to deployed site: [Boutique Ado](https://kera-cudmore-boutique-ado.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/kera-cudmore/Boutique-Ado?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/kera-cudmore/boutique-ado?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/kera-cudmore/boutique-ado?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kera-cudmore/boutique-ado?color=yellow&style=for-the-badge)

---

## CONTENTS

* [User Experience](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
* [Features](#features)
  * [General Features of Each Page](#general-features-of-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Databases Used](#databases-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
  * [Stripe](#stripe)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)

---

Responsive site image to go here.

---

## User Experience

### Project Goals

### User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| 1 | Shopper | View a list of products| Select something to purchase |
| 2 | Shopper | View a specific category of products | Quickly find products I'm interested in without having to search through all products. |
| 3 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes. |
| 4 | Shopper| Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase. |
| 5 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much. |
| **REGISTRATION & USER ACCOUNTS** |
| 6 | Site User | Easily register for an account| Have a personal account and be able to view my profile |
| 7 | Site User | Easily log in or out | Access my personal account information |
| 8 | Site User | Easily recover my password in case I forget it | Recover access to my account |
| 9 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 10 | Site User | Have a personalised user profile | View my personal order history and order confirmations, and save my payment information |
| **SORTING & SEARCHING** |
| 11 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products |
| 12 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 13 | Shopper | Sort multiple categories of products simutaneously | Find the best-priced or best-rated products across broad categories, such as clothing or homeware |
| 14 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| 15 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |
| 16 | Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 17 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| 18 | Shopper | Adjust the quantity of individual items in my bag| Easily make changes to my purchase before checkout |
| 19 | Shopper | Easily eneter my payment information | Check out quickly and with no hassles |
| 20 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 21 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 22 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **ADMIN & STORE MANAGEMENT** |
| 23 | Store Owner | Add a product| Add new items to my store |
| 24 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 25 | Store Owner | Delete a product | Remove items that are no longer for sale |

---

## Design

### Colour Scheme

### Typography

The font Lato has been used throughout the site. This was imported into the CSS file from Google Fonts.

![Lato Font Examples](documentation/lato-font.png)

### Imagery

### Wireframes

### Database Schema

---

## Features

### General Features of Each Page

### Future Implementations

### Accessibility

---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python 3

### Databases Used

sqlite3 - for the development database.
ElephantSQL - For the deployed sites database.

### Frameworks Used

[Django](https://www.djangoproject.com/) - Version 3.2.16 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version 4.6 - A framework for building responsive, mobile-first sites.

### Libraries & Packages Used

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 0.41.0 - Used for authentication, registration & account management.

[dj_database_url](https://pypi.org/project/dj-database-url/0.5.0/) - Version 0.5.0 - Allows us to utilise the DATABASE_URL environment variable.

[Stripe](https://pypi.org/project/stripe/) - Version 5.0.0 - To allow us to utilise the Stripe API for payments.

[gunicorn](https://pypi.org/project/gunicorn/) - Version 20.1.0

[psycopg2](https://pypi.org/project/psycopg2/) - Version 2.9.5 - A postgres database adaptor.

[pillow](https://pypi.org/project/Pillow/) - Version 9.3.0 - A python imaging library.
asgiref==3.5.2

[django-countries](https://pypi.org/project/django-countries/7.2.1/) - Version 7.2.1

[django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Version 1.14.0

oauthlib==3.2.1

pytz==2022.4

requests-oauthlib==1.3.1

sqlparse==0.4.3

### Programs Used

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Shields.io](https://shields.io/) - To add badges to the projects documentation.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

### Stripe

Stripe - setting up stripe elements to accept payment [docs](https://stripe.com/docs/js)

---

## Deployment & Local Development

### Deployment

The site is deployed using heroku. To deploy using heroku:

1.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [Boutique Ado](https://github.com/kera-cudmore/Boutique-Ado).

3. Click on the fork button in the top right of the page.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for the project.

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

---

## Credits

### Code Used

This project was created as part of a series of lessons with the Code Institute as part of their Level 5 Diploma in Web Application Development.

### Content

The content required for the site was provided as part of the lesson materials by the Code Institute.

### Media

A link to download the product images was provided by the Code Institute, who sourced the material from [kaggle](https://www.kaggle.com/).
