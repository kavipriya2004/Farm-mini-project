# Farm Management
Farm management system using Django, Python, HTML, CSS, JS, and PostgreSQL. Efficiently tracks farmer and crop data, with a user-friendly interface. Open-source project for agriculture management.

## Getting Started

 1)git clone "repository-link"

 2)cd "repo-name"

 3)python -m venv env

 4)Activate the virtual environment:

 5)Create a "requirements.txt" file with the dependencies 

 6)pip install -r requirements.txt

 7)python manage.py migrate

 8)python manage.py createsuperuser

 9)python manage.py runserver


### Prerequisites
List the software and tools that need to be installed.

- Python 3.12.3
- Django
- Dependencies  
        asgiref==3.7.2
        distlib==0.3.8
        Django==5.0
        django-crispy-forms==2.1
        djangorestframework==3.14.0
        djangorestframework-simplejwt==5.3.1
        filelock==3.13.1
        mysql-connector-python==8.3.0
        mysqlclient==2.2.1
        npm==0.1.1
        optional-django==0.1.0
        pillow==10.3.0
        platformdirs==4.1.0
        psycopg2==2.9.9
        psycopg2-binary==2.9.9
        PyJWT==2.8.0
        PyMySQL==1.1.0
        pytz==2024.1
        sqlparse==0.4.4
        tzdata==2023.3
        virtualenv==20.25.0
        virtualenvwrapper-win==1.2.7


#### Usuage
After setting up the project and running the development server, you can access the web application by navigating to http://127.0.0.1:8000/ in your web browser.

    1)Login: Use the superuser credentials created during setup to log in to the admin interface at http://127.0.0.1:8000/admin/.

    2)Manage Farmers and Crops: Add, update, and delete farmer and crop records using the admin interface or the provided application forms.

##### Contributing
If you want to contribute to this project, please follow these steps:
1)Fork the repository
2)Clone your forked repository
3)Create a new branch           
            -git checkout -b "feature-branch"
4)Make your changes and commit them
            -git commit -m 'Add some feature'
5)Push to the branch
            -git push origin "feature-branch"
6)Create a new Pull Request

###### License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.     
    Make sure to include a `LICENSE` file in your repository with the full text of the Apache License 2.0. You can create this file by going to your repository on GitHub, clicking on "Add file" -> "Create new file", naming it `LICENSE`, and then pasting the content of the Apache License 2.0 into it.

###### Installation
Steps to install the required dependencies and set up the project.

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate into the directory
cd farmer

# Install dependencies (if applicable)
pip install -r requirements.txt

# Run the project
python manage.py runserver


