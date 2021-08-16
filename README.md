[![homepage][1]][2]

[1]:  static/images/siterender.png
[2]:  Irishcraft.webaddress "Redirect to homepage"



**IrishCraft Website**
==================
Table of contents:
-----------------


 - [Description](#description)
 - [User Experience](#user-experience)
     - User Stories
     - Strategy
     - Scope
     - Structure
     - Skeleton
     - Surface
 - [Technologies](#technologies)
 - [Testing](#testing)
     - Acceptance Criteria
     - Browser Compatibility
     - OS Compatibility
     - Devices Compatibility
     - W3 HTML Validation
     - W3 CSS Validation 
     - CSS Lint Validation 
     - JSHint Validation
     - Python PEP8 Validation
     - Lightspeed Performance Test
     - Regression Testing
     - User Testing
     - Bugs
 - [Deployment](#deployment)
 - [Credits](#credits)
     - Code Used
     - Content
     - Acknowledgements


Description
-----------

Irish Craft is an e-commerce website built using Python and Django. 
The live site can be viewed [here](https://irishcraft.webaddress/).

User Experience
--------------------

----------

**USER STORIES**

----------

| User Stories | As A/An                             | I want to be able to                                                           | So that I can                                                                 |   |   |   |
|--------------|-------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---|---|---|
|              ||****** **View Products**  ******                     |                                                                                |                                                                               |   |   |   |
| 1            | Casual Shopper                      | View all products                                                              | products can be selected from list to purchase                                |   |   |   |
| 2            | Casual Shopper                      | Select and view individual products details                                    | View larger image of product, description, price, sizes and a purchase option |   |   |   |
| 3            | Casual Shopper                      | View list of items in basket and totals                                        | See my item count, price and subtotal/total                                   |   |   |   |
| 4            | Casual Shopper                      | View a list of products by category                                            | See a range of items in the category I am interested in.                      |   |   |   |
|              ||****** **Search and Sort Products** ******            |                                                                                |                                                                               |   |   |   |
| 5            | Casual Shopper                      | Search for products by name or description                                     | Narrow down the list of items that I have to view                             |   |   |   |
| 6            | Casual Shopper                      | See the number of results in a search that I have performed                    | Easily see how many products are available.                                   |   |   |   |
| 7            | Casual Shopper                      | Sort the products based on price                                               | Better identify items that I would like to buy                                |   |   |   |
|              ||**** **Registration & Account management** ****|                                                                                |                                                                               |   |   |   |
| 8            | Return Shopper                      | Set up an account with the store                                               | Create an account to store my details such as purchase history and address.   |   |   |   |
| 9            | Return Shopper                      | Login and logout functionality                                                 | Gain access to my account                                                     |   |   |   |
| 10           | Return Shopper                      | Recover account if password forgotten                                          | Gain access to my account                                                     |   |   |   |
| 11           | Return Shopper                      | Receive an confirmation email on registration                                  | Verify my account has been created                                            |   |   |   |
| 12           ||****** **Checkout and Payment** ******                |                                                                                |                                                                               |   |   |   |
| 13           | Return Shopper                      | Select a quantity of items and sizes if available                              | Add the items to my basket                                                    |   |   |   |
| 14           | Return Shopper                      | Remove items from my basket                                                    | Ensure I am paying for only the products I want                               |   |   |   |
| 15           | Return Shopper                      | Edit items in my basket                                                        | Ensure I am paying the correct quantity or size of product.                   |   |   |   |
| 16           | Return Shopper                      | View a full list of all products in my basket with prices and subtotal/total.  | Ensure that I have everything in my basket that I wanted.                     |   |   |   |
| 17           | Return Shopper                      | Enter my address and payment details for purchase                              | Pay for the items and have them delivered to the correct address              |   |   |   |
| 18           | Return Shopper                      | Get a confirmation email of my purchase                                        | Be reassured that my purchase has gone through and is correct                 |   |   |   |
| 19           | Return Shopper                      | Pay for my items in a manner that is secure and familiar                       | Be sure that my card details and payment are handled securely.                |   |   |   |
| 20           | Return Shopper                      | Review a product that I have bought                                            | Let other people know what I think of the product                             |   |   |   |
| 21           | Return Shopper                      | Add items to a Wishlist                                                        | Save items that I would like to buy at a future date.                         |   |   |   |
|              ||****** **Site Administration** ******                 |                                                                                |                                                                               |   |   |   |
| 22           | Site Owner                          | Add and remove products from the site                                          | Ensure my site is up to date.                                                 |   |   |   |
| 23           | Site Owner                          | Edit product details                                                           | Have the ability to change product details, price, availability and images.   |   |   |   |
|              |                                     |                                                                                |                                                                               |   |   |   |
|              |                                     |                                                                                |                                                                               |   |   |   |

A pdf of the User Stories spreadsheet can ben view [here](/static/readme_files/user_stories_irish_craft.numbers)

The mockup for this site was done on Balsamiq Wireframes 
and can be viewed below 



- [Desktop Homepage](static/readme_files/wireframes/index_page.png).  
- [Catagory Page](static/readme_files/wireframes/category_page.png).  
- [Login Page](static/readme_files/wireframes/login.png).  
- [Create Account Page](static/readme_files/wireframes/create_account.png).  
- [Basket Page](static/readme_files/wireframes/basket.png).
- [Account Page](static/readme_files/wireframes/account.png). 
- [Review Item Page](static/readme_files/wireframes/review_item.png).  
- [Wishlist Page](static/readme_files/wireframes/wishlist.png). 
- [View Item Page](static/readme_files/wireframes/view_itme.png). 
- [Admin Edit Item Page](static/readme_files/wireframes/admin_edit_item.png). 
- [Admin Add Item Page](static/readme_files/wireframes/admin_add_item.png). 
- [Checkout Page](static/readme_files/wireframes/checkout.png). 


The full selection of wireframes including mobile layout can be viewed in PDF form [here](static/readme_files/wireframes/irish_craft_wireframes.pdf)



----------

**STRATEGY**

--------

 - **Focus:**  
    The focus of this project will be the creation of a secure, navigable e-commerce site with ability to search and sort products. The site must make the shopping experience a positive one.

 - **Definition:**  
    Irish Craft is a solid, secure and friendly environment to search, save and purchase products.

 - **Value:**   
    The shopper will have a positive experience increasing the probablility of purchase and repeat business. 

----------

**SCOPE**

----------

**Features:** 


- **Navigation menu** – The navigation menu will offer users a number of site locations depending on their user access. 

- **Search Bar** – Search bar to query the database of products.

- **Account Page** – Displays shopper account details.

- **Review Page** - Give the shopper an opportunity to share their experience with the product/company.

- **Wishlist** - Allows the shopper to save their favourite items for return visits to the site.


**STRUCTURE**

----------

1. The shopper will first be presented with the main 'index' page where they will see a 

2. The Menu will display if not logged in "Home", "Login" and "SignUp" and if logged in will display "Add Location", "Profile" "Home and "Logout"


3. The Profile page will Be broken into three sections. A profile card with some stats about the users activity. A section for posts that the user has created and section with posts that the user has liked. 
    - As an external user I create a collection of my favourite camping locations.

4. The View location page will be a simple card displaying the Name, Description, Rating, Location and Picture of the campsite. This card will display a like button to logged in users and edit or delete to the user who created the post.

5. The Add Location page will have a simple form with fields for Name and Description, a star rating selection area, a map to search for the location and drop a pin, a button to upload a photo and a submit button. 
    - As a site owner I want create a knowledge bank of good camping locations


----------

**SURFACE**

----------


**Colours:** 

- 

**Typography:** 

- 

**Effects:**

 -  

**Imagery:** 

 - 

**Deviations from design:**

- 


Technologies
----------------

 - [**HTML5**](https://en.wikipedia.org/wiki/HTML5) –  to create the websites main structures
 - [**CSS3**](https://en.wikipedia.org/wiki/CSS) – to style the components created with HTML and
   create the desired effects described in the ‘Surface’ section.
 - [**Python**](https://www.python.org/download/releases/3.0/)
 - [**Materialize**](https://materializecss.com/) – to create responsive elements on the page.
 - [**FontAwesome**](https://fontawesome.com/)  - icons used throughout the site.
 - [**Google Fonts**](https://fonts.google.com/) – Imported fonts.
 - [**GitPod**](https://gitpod.io/) – IDE used for working on my code
 - [**GitHub**](https://github.com/) – Used for hosting the files used for the website.
 - [**Git**](https://git-scm.com/) – Version control used to track changes, commit and push code to
   Github.
 - [**Javascript**](https://www.javascript.com/)
 - [**Flask**](https://flask.palletsprojects.com/en/2.0.x/)
 - [**Lightspeed**](https://developers.google.com/speed/pagespeed/insights/) - Website performance testing utility
 - [**DevTools**](https://developers.google.com/web/tools/chrome-devtools) - I used Chrome DevTools throughout the development of the site to modify elements on the screen live, testing screen responsiveness and debugging code.
 - [**W3 HTML Validation**](https://validator.w3.org/) - Online HTML validation tool. 
 - [**W3 CSS Validation**](https://jigsaw.w3.org/css-validator/) - Online CSS validation tool.
 - **Gitpod extensions:**
     - Auto Close Tag
     - Bracket Pair Colorizer
     - Code Spellchecker
     - Prettier - Code Formatter
     - Indent-Rainbow
 - [**Techsini**](http://techsini.com/multi-mockup/index.php) - I used this website to create a multi mockup of the live website display at the head of my Readme file. 
 - [**Brackets**](http://brackets.io/) - Local IDE.
 - [**Autoprefixer**](https://autoprefixer.github.io/) - Parses CSS and adds vendor prefixes.
 - [**Google mobile-friendly Test**](https://search.google.com/test/mobile-friendly?id=PM7sy6dG9tEXLsvHooNW6Q) - Tests for mobile compatibility. 
 - [**Xcode simulator**](https://developer.apple.com/documentation/xcode) - suite of tools used for build or testing apps for Apple platform.
 - [**BeautifyTools Javascript Validator**](https://beautifytools.com/javascript-validator.php) - Online Javascript validation tool. 
 - [**JSHint Validation**](https://jshint.com/) - Online Javascript validation tool. 
 - [**JSON Valdiation**](https://jsonlint.com/) - Debug JSON object structure used in MongoDB and Javascript
 - [**Django**](https://www.djangoproject.com/) - High-level Python Web framework
 - [**Cloudinary**](https://cloudinary.com/) - Cloud storage for website media files


Testing
-------

----
**Acceptance Criteria:**

1. All links on the website must connect to the correct location.
2. All images and elements on website must load correctly.
3. All fallback fonts must work visually should the first choice fonts be unavailable.
4. All elements on the website must be responsive, resizing for different screen sizes and maintaining their integrity with no overlapping.
5. All external links direct to the correct website.
6. The website loads correctly and functions on Chrome, Internet Explorer, Safari and Firefox browsers.
7. The website performs as required as outlined in User Stories for external users and the site owner.

All testing is documented and can be viewed in the following formats. [Mac Numbers](atesting/irishcrafttesting.numbers), [Excel](testing/irishcrafttesting.xlsx) and [PDF](testing/irishcrafttesting.pdf).

----
**Browser Compatibility**


| Screen Size/Browser  | Chrome  | Internet Explorer  | Safari  |  Firefox |
|---|---|---|---|---|
|  Mobile |✅   | ✅  | ✅| ✅ |
|  Desktop | ✅  | ✅  | ✅  | ✅  | 
|  Tablet | ✅  | ✅  | ✅  |  ✅ | 


**OS Compatibility** 


The OS used during testing were: 
The OS used during testing were: 
- Mac OS 11.0.1 
- Windows 10
- Android (OxygenOS Version 9.0.6)
- iOS 14.4.1
- Xcode Simulator - iPhone 12 Pro Max, iPad Pro 12.9inch
- Chrome OS (release 89.0.4389.95)

Further testing yet to be carried out on Linux and Unix.

----
**Device Compatibility** 


The devices used during testing were: 
- MacBook Air 13inch 2017
- Acer Chromebook cb3-431
- OnePlus 3T 
- OnePlus 5T
- Pixel 4a
- iPhone X 
- iPhone SE 
- HP Elitebook G5 
- iPad 10.2
- Dell OptiPlex 7480 
- Samsung Galaxy s20


----
**W3 HTML Validation** 

HTML Validation with [https://validator.w3.org/](https://validator.w3.org/).




----
**W3C CSS Validation** 


CSS validation with [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)



----
**CSS Lint Validation**


CSS also validated via http://csslint.net/


----
**BeautifyTools Javascript Validation** 

https://beautifytools.com/javascript-validator.php


----
**Lightspeed Performance Test** 

The performance of the site on Lighthouse can be viewed [here](testing/lightspeedtest.pdf)

----
**Regression Testing**

Any new features and bug fixes were submitted to regression testing of all functional and non functional aspects of the project to ensure that previously developed and tested software still performed following changes.

----
**User Testing**




----
**Bugs**

+ **Bug001:** "django.db.utils.OperationalError: no such column:" Error after altering model item 'image' to change its definition to cloudinary parameters. 
**Fix:** The field had to be deleted entirely then running 'python3 manage.py makemigrations' and 'python3 manage.py migrate'. I then put in the altered field and ran migrations again to update the table. 

+ **Bug:**    
**Fix:** 

+ **Bug:**    
**Fix:** 

+ **Bug:**    
**Fix:** 

+ **Bug:**    
**Fix:** 




Deployment
----------

**Local Deployment**



**Remote**

1. Open repository in gitpod
2. Create a file got .env inside the directory irishcraft at the same level as settings.py
3. Add .env to .gitignore
4. Generate a random key, I used https://randomkeygen.com/ but you can just google any random key generator. 
5. Inside the .env file add the following....
    SECRET_KEY=insert-your-random-key-here. eg. SECRET_KEY=12345678abcdefg


6. Set up a cloudinary account and follow directions in the following link https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/\



Credits
-------

**Code used**

Generate random selection from Products database
https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys#:~:text=to%20show%0Anum_entities%20%3D-,Entity.objects,-.all().count()%0Arand_entities


Setting active item in carousel loop - 
https://stackoverflow.com/questions/52870493/carousel-set-first-loop-image-as-active-item/52870679

Snackbar script used to create toast messages alerts
https://www.cssscript.com/snackbar-toast-notification/


**Content**

No image placeholder -  https://sirv.com/help/articles/customized-error-images/


**Acknowledgements**
