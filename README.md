# My-Phone
________
My-Phone is a full-stack Django website built using Python, JavaScript, HTML and CSS. This web application is a full B2C e-commerce website for a fictional online mobile phone website. 

## Aim
________
My-Phone specialises in selling and delivering the latest technology phones at the best price in market. The site provides users with different functionalities that eases the process of purchasing a product. Users of the site can browse all products, filter products by different categories and also search for specific products by keyword search. From the list of products, users can select them to display each product in detail, giving users the option to add the product to their basket or return to the product list page to browse other phones. Registered users can add the product to their wishlist or a leave a review for other users to view. Authenticated users can also checkout securely inputting their personal & payment details to purchase the product and also store these details on their profile for easier future purchases. On the other hand, this website also provides the store owner with functionalities such as product management (add, edit & delete products) without accessing the admin interface and blog post management (add, edit & delete blogs).

This website application includes CRUD functionality, user authentication (using Django's allauth library), email validation and database interaction.

[My-Phone live link](https://my-phone2234.herokuapp.com/)


## Table of Contents:
_______
- User Stories
- Agile Planning Environment
- Exiting features
  -	All Pages
    - Navigation
    - Footer
  -	Home Page
  -	Products`
  -	Products Details
  -	Add to bag notification
  -	Bag Page
  -	Checkout
  -	Order Confirmation Page
  -	User Profile
  -	Wishlist
  -	Admin
    - Add Product
    - Edit Product
    - Delete Product
- Future feature
- Database schema
- Marketing
  -	Search Engine Optimization
  -	Web Marketing
  -	Google Metrics
  -	Business Model
  -	Social Media Platform
  -	Email Subscription Service
  -	Confirmation Email
- Color Scheme
- Typography
- Favicon
- Wireframes
  - Desktop wireframe
  - Mobile wireframe
- Technologies used
- Testing
  - Manual and automated testing
  -	Python testing
  -	Manual User Story Testing
  -	Fixed Bugs and Errors
- Deployment
  -	Github
  -	Django and Heroku
  -	Allauth
- Forking
- Cloning
- AWS Setup
- Stripe Payments
- Credits


## User Stories
___
#### EPIC: Viewing and Navigation (Products)

#### EPIC: Registration and Verification

#### EPIC: Sorting and Searching

#### EPIC: Purchasing and Checkout

#### EPIC: Admin and Store Management

#### EPIC: Product and Cocktail Reviews

#### EPIC: Wishlist Functionality

## Agile Planning Environment
___
The story point allocation above is based upon a 100-point iteration and uses the Fibonacci Sequence. Using the MoSCoW method each user story was then been labelled as being either 'Must Have', 'Should Have', 'Could Have' or 'Wont Have', based upon its importance to the project whilst following the 60:20:20 MoSCoW format. Note that the 'Wont Have' User Story below was excluded from the 60:20:20 MoSCoW allocation.

pic

## Exiting features
__________

### All Pages

  #### Navigation

  The main navigation bar is located at the top of the webpage and has different functionalities. It contains the main company title to the left, a product search bar in the center and the Wishlist, bag & user profile icons to the right. When clicked on, the user profile icon branches into more links. These include authentication links (register, login & logout), my profile, my Wishlist and product management (if admin is logged in). Below the product search bar, there are individual navigation links that allow the user to browse through the products via different filters. On smaller viewports, a hamburger menu is present to keep the look of the navbar refined and clean.

  #### Footer

  The footer of the page provides users with informational resources with copyright of the website on the left-hand side, and social media icons in the middle and contact details on the right-hand side of the footer.

### Home Page

The main image on the site was carefully selected, with the aim to entice customers to explore the site further, thus improving the sites google metrics. The bold and contrasting colors within this image were then selected using Chrome DevTools and applied within the rest of the site.
The Home Page of the website is segregated into different sections. This includes a CTA (Call to Action) that allows the users to easily access the list of phone products to browse through. A main banner of a product that represents the company and its market which is present to be appealing to user. About section- it introduces users to the website. Finally, a MailChimp powered email newsletter form that allows users to input their email address to subscribe to My Phone, followed by footer.


### Products

The products list page displays the summary of each product in a card container, an image, product name, category, price and rating. Each product card can be clicked on to view the product in detail on another page. Products can also be filtered via different categories; by rating and by price (ascending & descending).

### Product Details

The product detail page displays full information of the product including product title, price, category, rating, and product information. Users can add the product to their Wishlist and add the specified quantity of the product to their basket for checkout. Registered users can leave a review below products to share their opinions with other users.
Users will also see similar products options.


### Add to bag Information

One of the main features of My Phone is that distinguishes it as an e-commerce store is the add to basket feature. Users can add a specified quantity of products to their basket for purchase. A success message is displayed on the screen when products are added.

### Bag Page

Once the user is happy with their selection, they can advance to the shopping basket page to confirm the product selections, quantity and prices. Users can also add or remove products whilst on this page to update the quantity before checkout.

### Checkout

When the user is ready to proceed to the checkout page after selecting their choice of products. Here, the user is required to fill out personal information; First name, surname, email address, phone number, street address, town/city, county, postal code, and country. The user is also required to fill out payment information which in this project is powered by Stripe, long card number. expiry date and CVC. As Stripe is not fully activated in this project, only test payment details can be used to process payments. Users also have the option to save their personal information to their profile so future checkouts are easier instead of having to fill out the form repeatedly. Finally, before proceeding with the payment, the order summary is displayed next to the order form so that it is clear to the user the selection of products they are ordering.

### Order Confirmation page

After users have placed their order, an order confirmation page is displayed with the summary of the order placed including product details, personal information, order number and the email that is used to send the order confirmation to.

### User Profile

Registered users have an option to view their profile that lists their saved personal information which can be used for future checkouts and also a history of the orders they have placed with their respective order numbers. These order numbers can be hovered over and clicked on so that users can view the full order details.

### Wishlist

Registered users have an option to view their Wishlist and the products that have been added to it. The Wishlist feature is convenient as it does not expire, even after the user signs out. So, if the user wants to wait a longer period to purchase a product, they can keep it stored in their Wishlist. Users also have an option to remove any product from their Wishlist if no longer required.

### Admin

The products feature of the site all follow CRUD functionality allowing the admin user to create, read, update, and delete products and cocktails on the site. This functionality can all be done through the front end of the site, providing updated messages at each stage.

  #### Add Product

  Admins can add products on the site using the site admin button at the top of the page. Upon clicking this admin users are given a form containing vital product information as seen below.

  #### Edit Product

  Admin can edit products using the buttons on the product page and product detail pages. The form shown to admin already contains current information saving time when making alterations.

  #### Delete Product

  Admin can click on delete button to delete a product.

## Futute Feature
______

The following features would help improve the site further, given more time I would have liked to have included these elements in my current project:

-	The ability to recover a user's password if it has been stolen/forgotten/corrupted. This functionality is part of the allauth library which has already been installed in this project but only needs to be setup to make this functional
-	The ability for a user to login their account via social media sign in.
-	The functionality to add a product to the basket straight from a user's Wishlist.

## Database Schema
_______

Entity Relationship Databases (ERD) were created to help develop this project. 

pic

## Marketing
______

The site was optimized by careful selection of keywords. The following steps were taken to do this:

1.	The entire table consists of important relevant topics based upon my initial understanding of the business.
2.	Using these topics, a 'brain dump' of keywords was made orientated around common topics and themes within the business.
3.	Topics and keywords were then tried out on Google and the relevant suggestions it gave were added to the keyword list.
4.	Words crossed out in red were removed due to too having too much competition using **Wordtracker**.
5.	Words crossed out in blue were removed due to the lack of relevance and not being specific to the site.

    Words in Yellow denote the sites "Short Tail Keywords"
    Words in Green denote the sites Long Tail Keywords"

An example of how these words were used throughout the site can be seen below in the screenshot found on the website’s homepage:

PIC

### Search Engine Optimization

-	Words/phrases included within semantic HTML elements were optimized using the keywords above.
-	Careful consideration was given to the words chosen to avoid 'keyword stuffing'.
-	Keywords were used within links, urls and aria labels.
-	Social network links include rel="noopener" to not affect the assessment of the webpage.
-	Image description alt tags contain the keywords chosen above.
-	External reliable links were included within the site to improve SEO, these include:
    1.	Charities that the company supports.
    2.	Recommended mixer brands.
    3.	Useful tips/advice on drinking sensibly.

### Google Metrics

Google metrics were considered when developing the site, including:

Click Through Rate (CTR)
-	The title and Meta data of the website were optimized with both short and long tailed keywords.
Bounce Rate
-	The homepage of the site has been made engaging for the user.
Dwell Time
-	Content on the homepage is interesting and engaging to users.
Session Time
-	It is made easy for users to discover more content through 'recommended items" sections on the page.
Pages Per Session
-	Links were regularly included throughout the website to encourage users to navigate through the website more and engage with more of the content.


### Business Model

The business model used for the My Phone would be a B2C (Business to Customer), this is due to the business selling products directly to the customer through the platform. The target market for these products are users:
-	Looking to buy phone online

Customers who are buying products from My Phone should be able to:
- Easily view and purchase products
- Easily navigate and search for products they wish to buy
- Be able to subscribe for emails for new offers


### Social Media Platforms

As part of the Code Institute assessment criteria, a Facebook page was created to promote the company. Facebook is used by many around the globe and is a key marketing strategy to be successful e-commerce business. The Facebook page includes a CTA button which drives traffic away from social media and to the website. A screenshot of the Facebook webpage is shown below:

pic

### Email Subscription Service

Users are encouraged to signup for newsletters, discounts and information about the products sold at My Phone. The email subscription service is ran through Mailchimp, allowing shop owners to send marketing emails through the platform, increasing engagement within the site. Below is a screenshot of one of the subscription emails that was sent by My Phone's shop owner:

Pic

### Confirmation Email

When customers sucessfully purchase a product they are sent an automatic email containing all of their order confirmation details. An image of what this confirmation email looks like can be seen below:

pic

## Color Scheme
______

The colors within the site were carefully selected to mirror the product sold online at MyPhone. The dark contrasts against the white making elements of importance stand out on the page. These colors were initially selected from the sites main banner image using DEV tools, allowing for all colors within the page to complement each other nicely.


## Typography
_____

The aim of the font was to create a sophisticated feel within the site, complementing the imagery seen throughout. Moreover, text colours were either dark black or white depending on the background contrast ratio, to ensure information was accessible to users who may be visually impaired. The main font used on the site was 'Mali' and this was selected using Google Fonts

## Favicon
______

## Wireframes
______
### Desktop Wireframes

### Mobile Wireframes

## Technologies used
_______

1. Coding Langauges

- [HTML](https://en.wikipedia.org/wiki/HTML)
  - HTML is the main language used across the site and completes the structure of the webpages.
 
- [CSS](https://en.wikipedia.org/wiki/CSS)
  - CSS is used throughout to create custom styling to elements across the site.

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - JavaScript is used within the checkout template to help with form submission and to verify the users age.
  - [jQuery](https://jquery.com/) is used within the following webpages:
    To update item quantity within the bag template and to update the form.
    To display success and fail messages within form submission.

- [Python](https://www.python.org/)
  - Python was used extensively on the site to handle back-end functionality.

2. Frameworks and Platforms

- [Django](https://www.djangoproject.com/)
  - The project was created using Django as a framework to help handle back-end functionality.

- [GitHub](https://github.com/)
  - GitHub was the hosting site for the project code.

- [Gitpod](https://www.gitpod.io/)
  - Gitpod has been used to commit and push code within the GitHub repository.

- [Google Fonts](https://fonts.google.com/)
  - Google Fonts was used to select the typography type for the website and imported within CSS.

- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap was used within the site to help format the layout of elements and improve the responsiveness of the site.

- [AWS S3 Buckets](https://aws.amazon.com/?nc2=h_lg)
  - AWS S3 Buckets provide storage for static and media files within the deployed Heroku site

- [Heroku](https://dashboard.heroku.com/apps)
  - Heroku was used as a platform to deploy the site.

- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Developer Tools were used to help debug errors within the code and to help style the site through the colour selector.

- [Font Awesome](https://fontawesome.com/)
  - Icons used across the site were imported from Font Awesome.

- [Am I Responsive](https://amiresponsive.co.uk/)
  - The site Mock Up image was generated using Am I Responsive.

## Testing
______
###	Manual and automated testing

### Python Testing

### Manual User Story Testing

### Fixed Bugs and Errors

## Deployment
_________

### GitHub
* Created a new GitHub repository page using the 'Code Institute Template'.
* Opened the new repository by clicking on the 'Gitpod' button.
* Installed the relevant apps and packages needed to deploy to HEROKU.

### Django and Heroku
Deployment of my project was scaffolded using the Code Institute's Django Blog Cheatsheet. Furthermore, the following steps were taken to deploy the project to Heroku from the GitHub repository:

1. Create the Heroku App:
Before creating the Heroku app make sure your project has the following files:

* requirements.txt to create this type the following within the terminal: pip3 freeze --local > requirements.txt.
* Procfile to create this type the following within the terminal: python run.py > Procfile.
- Select "Create new app" within Heroku.

2. Attach the Postgres database:
- Search "Postgres" within the Resources tab and select the Heroku Postgres option.

3. Create the settings.py file:
- In Heroku navigate to the Settings tab, click on Reveal Config Vars and copy the DATABASE_URL.
- Within the Gitpod workspace, create an env.py file within the main directory.
- Import the env.py file within the settings.py file.
- Create a SECRET_KEY value within the Reveal Config Vars in Heroku.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Run the following command in your terminal python3 manage.py migrate.
- Add the CLOUDINARY_URL to the Reveal Config Vars in Heroku and add this to your settings.py file.
- Add the following sections to your settings.py file:
* Cloudinary to the INSTALLED_APPS list
* STATICFILES_STORAGE
* STATICFILES_DIRS
* STATIC_ROOT
* MEDIA_URL
* DEFAULT_FILE_STORAGE
* TEMPLATES_DIR
* Update DIRS in TEMPLATES with TEMPLATES_DIR
* Update ALLOWED_HOSTS with ['app_name.heroku.com','localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
- Create three directories in the top level directory: media, storage and templates.
- Create a file named "Procfile" in the main directory and ass the following: [web: gunicorn project-name.wsgi].
- Login to Heroku within the terminal window using heroku login -i
- Run the following command in the terminal window: heroku git:remote -a your_app_name_here. By doing this you will link the app to your GidPod terminal.
- After linking the app you can deploy new versions to Heroku by running the command git push heroku main.

### Allauth

Within the Django Framework, Allauth a package that handles registration and login details was installed. More information on how this was installed can be found here: [Django Allauth Installation](https://django-allauth.readthedocs.io/en/latest/installation.html)


## Forking the Repository
________

* Log in to GitHub and locate the required GitHub repository.
* At the top of the Repository, above the "Settings" button, locate the button labelled "Fork".
* You should now have a copy of the original repository within your GitHub account.
* You can make changes to this new version whilst keeping the original version safe.

## Cloning
________

* Ensure that you are logged into GitHub and locate the required GitHub repository.
* Click the dropdown button labelled 'Code' above the file list.
* Copy the URL for the required repository.
* Open Git Bash on your device.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone in the CLI and then paste the URL you copied earlier.
* Press Enter to create your local clone.
* For more information on how to clone a repository read GitHub's [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) document.


## AWS Set Up
_______

The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fportal.aws.amazon.com%2Fbilling%2Fsignup%2Fresume&client_id=signup&code_challenge_method=SHA-256&code_challenge=L8fV-W3h8oZvJxvy_MiEZmEinjbZ5t7FIeyJlKqsSzw#/start/email).
2. Login to your account and within the search bar type in S3.
3. Within the S3 page click on the button that says Create Bucket.
4. Name the bucket and select the region which is closest to you.
5. Underneath Object Ownership select ACLs enabled.
6. Uncheck Block Public Access and acknowledge that the bucket will be made public, then click Create Bucket.
7. Inside the created bucket click on the Properties tab. Below Static Website Hosting click Edit and change the Static website hosting option to Enabled. Copy the default values for the index and error documents and click Save Changes.
8. Click on the Permissions tab, below Cross-origin Resource Sharing (CORS), click Edit and then paste in the following code:
  [
      {
          "AllowedHeaders": [
          "Authorization"
          ],
          "AllowedMethods": [
          "GET"
          ],
          "AllowedOrigins": [
          "*"
          ],
          "ExposeHeaders": []
      }
  ]
  
 9. Within the Bucket Policy section. Click Edit and then Policy Generator. Click the Select Type of Policy dropdown and select S3 Bucket Policy and within Principle allow all principals by typing *.
 10. Within the Actions dropdown menu select Get Object and in the previous tab copy the Bucket ARN number. Paste this within the policy generator within the field labelled Amazon Resource Name (ARN).
 11. Click Add statement > Generate Policy and copy the policy that's been generated and paste this into the Bucket Policy Editor.
 12. Before saving, add /* at the end of your Resource Key, this will allow access to all resources within the bucket.
 13. Once saved, scroll down to the Access Control List (ACL) and click Edit.
 14. Next to Everyone (public access), check the list checkbox and save your changes.
 
 ### IAM
 
 1. Search for IAM within the AWS navigation bar and select it.
 2. Click User Groups that can be seen in the side bar and then click Create group and name the group 'manage-your-project-name'.
 3. Click Policies and then Create policy.
 4. Navigate to the JSON tab and click Import Managed Policy, within here search S3 and select AmazonS3FullAccess followed by Import.
 5. Navigate back to the recently created S3 bucket and copy your ARN Number. Go back to This Policy and update the Resource Key to include your ARN Number, and another line with your ARN followed by a /*. Below is an example of what this should look like:
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

6. Ensure the policy has been given a name and a short description, then click Create Policy.
7. Click User groups, and then the group you created earlier. Under permissions click Add Permission and from the dropdown click Attach Policies.
8. Select Users from the sidebar and click Add User.
9. Provide a username and check Programmatic Access, then click 'Next: Permissions'.
10. Ensure your policy is selected and navigate through until you click Add User.
11. Download the CSV file, which contains the user's access key and secret access key.

### Connecting AWS to Django

1. Within your terminal install the following packages by typing
  pip3 install boto3
  pip3 install django-storages 
  
2. Freeze the requirements by typing
pip3 freeze > requirements.txt

3. Add storages to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code:
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

5. Add the following keys within Heroku: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. These can be found in your CSV file.
6. Add the key USE_AWS, and set the value to True within Heroku.
7. Remove the DISABLE_COLLECTSTAIC variable from Heroku.
8. Within your settings.py file inside the code just written add:
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
  
9. Inside the settings.py file inside the bucket config if statement add the following lines of code:
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

10. In the root directory of your project create a file called custom_storages.py. Import the following at the top of this file and add the classes below:
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

11. Navigate back to you AWS S3 Bucket and click on Create Folder name this folder media, within the media file click Upload > Add Files and select the images for your site.
12. Under Permissions select the option Grant public-read access and click Upload.


## Stripe Payments
______

To handle payments within the website ensure that you have set this up a guide on how this can be done can be found [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).


## Credits
______
..
