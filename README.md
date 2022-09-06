# My-Phone
My-Phone is a full-stack Django website built using Python, JavaScript, HTML and CSS. This web application is a full B2C e-commerce website for a fictional online mobile phone website. 

## Aim
My-Phone specialises in selling and delivering the latest technology phones at the best price in market. The site provides users with different functionalities that eases the process of purchasing a product. Users of the site can browse all products, filter products by different categories and also search for specific products by keyword search. From the list of products, users can select them to display each product in detail, giving users the option to add the product to their basket or return to the product list page to browse other phones. Registered users can add the product to their wishlist or a leave a review for other users to view. Authenticated users can also checkout securely inputting their personal & payment details to purchase the product and also store these details on their profile for easier future purchases. On the other hand, this website also provides the store owner with functionalities such as product management (add, edit & delete products) without accessing the admin interface and blog post management (add, edit & delete blogs).

This website application includes CRUD functionality, user authentication (using Django's allauth library), email validation and database interaction.

### Deployment

#### GitHub
* Created a new GitHub repository page using the 'Code Institute Template'.
* Opened the new repository by clicking on the 'Gitpod' button.
* Installed the relevant apps and packages needed to deploy to HEROKU.

#### Django and Heroku
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

#### Allauth

Within the Django Framework, Allauth a package that handles registration and login details was installed. More information on how this was installed can be found here: [Django Allauth Installation](https://django-allauth.readthedocs.io/en/latest/installation.html)


### Forking the Repository

* Log in to GitHub and locate the required GitHub repository.
* At the top of the Repository, above the "Settings" button, locate the button labelled "Fork".
* You should now have a copy of the original repository within your GitHub account.
* You can make changes to this new version whilst keeping the original version safe.

### Cloning the Repository

* Ensure that you are logged into GitHub and locate the required GitHub repository.
* Click the dropdown button labelled 'Code' above the file list.
* Copy the URL for the required repository.
* Open Git Bash on your device.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone in the CLI and then paste the URL you copied earlier.
* Press Enter to create your local clone.
* For more information on how to clone a repository read GitHub's [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) document.


### AWS S3 Bucket Set Up

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


### Stripe Payments

To handle payments within the website ensure that you have set this up a guide on how this can be done can be found [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).


### Credits
..
