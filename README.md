## TITLE 
# Matuzo-Awards:gift_heart:

## AUTHOR
By **wilson owino** :100:

## DESCRIPTION
An App that mimics the infamous awwwards for project posting, reviews and ratings.|You can see other peoples project and rate them as well as posting yours


## BEHAVIOUR DRIVEN DEVELOPMENT(BDD)

| Behaviour | Input                     | Output                    |
| --------- | ------------------------- | ------------------------- |
| Register first | Input details to be validated | view the page upon registration |
| Update profile | in put profile pic to profile |  submit and view |
| post a project | post a pic and add description | 
| Rate and Review | Rate and review a projct out of ten |  scores are tabulated |
| Log Out |   | Proceedings Terminated |


# DISPLAY

## sign up :book:
![screenshot](/static/photos/registration.png)
## Landing Page 
### Various Projects That have been posted seen here:
![screenshot](/static/photos/land.png)
## Rate 
### Rate a projrct that you clicked on
![screenshot](/static/photos/rate.png)

## Upload 
### Upload your project for  other users
![screenshot](/static/photos/upload.png)





## SETUP
### Requirements
* Django 1.11
* Python 3.5 and above 
### Installation
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* Access the live site using the local host provided

### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)
#### Clone the Repo and rename it to suit your needs.
```bash
git clone the link
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste the following filling where appropriate:
```
SECRET_KEY='your_Secret_key'
DEBUG=True
DB_USER='your_database_username'
DB_PASSWORD='your_database_password'
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## LIVE SITE
## KNOWN BUGS
None

## TECHNOLOGIES
* Python3.6
* Django
* Javascript
* Css
* Scss

## LICENSE
[MIT](https://github.com/Willyowi/matuzo awards/blob/master/LICENSE)