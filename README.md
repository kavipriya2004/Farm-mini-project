# Farm Management
Farm management system using Django, Python, HTML, CSS, JS, and PostgreSQL. Efficiently tracks farmer and crop data, with a user-friendly interface. Open-source project for agriculture management.
<br>
<br>
## Getting Started<br>

 1)git clone "repository-link"<br>
 2)cd "repo-name"<br>
 3)python -m venv env<br>
 4)Activate the virtual environment<br>
 5)Create a "requirements.txt" file with the dependencies <br>
 6)pip install -r requirements.txt<br>
 7)python manage.py migrate<br>
 8)python manage.py createsuperuser<br>
 9)python manage.py runserver<br>
<br>
<br>
<br>
## Prerequisites
List the software and tools that need to be installed.

- Python 3.12.3
- Django
- Dependencies  
        asgiref==3.7.2 <br>
        distlib==0.3.8<br>
        Django==5.0<br>
        django-crispy-forms==2.1<br>
        djangorestframework==3.14.0<br>
        djangorestframework-simplejwt==5.3.1<br>
        filelock==3.13.1<br>
        mysql-connector-python==8.3.0<br>
        mysqlclient==2.2.1<br>
        npm==0.1.1<br>
        optional-django==0.1.0<br>
        pillow==10.3.0<br>
        platformdirs==4.1.0<br>
        psycopg2==2.9.9<br>
        psycopg2-binary==2.9.9<br>
        PyJWT==2.8.0<br>
        PyMySQL==1.1.0<br>
        pytz==2024.1<br>
        sqlparse==0.4.4<br>
        tzdata==2023.3<br>
        virtualenv==20.25.0<br>
        virtualenvwrapper-win==1.2.7<br>
<br>
<br>
<br>

## Usuage
After setting up the project and running the development server, you can access the web application by navigating to http://127.0.0.1:8000/ in your web browser.<br>
 1)Login: Use the superuser credentials created during setup to log in to the admin interface at http://127.0.0.1:8000/admin/.<br>
 2)Manage Farmers and Crops: Add, update, and delete farmer and crop records using the admin interface or the provided application forms.
<br>
<br>
<br>

## Contributing
If you want to contribute to this project, please follow these steps:<br>
1)Fork the repository<br>
2)Clone your forked repository<br>
3)Create a new branch           <br>

            -git checkout -b "feature-branch"<br>
4)Make your changes and commit them<br>

            -git commit -m 'Add some feature'<br>
5)Push to the branch<br>

            -git push origin "feature-branch"<br>
6)Create a new Pull Request<br>
<br>
<br>
<br>
## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.   <br>  
    Make sure to include a `LICENSE` file in your repository with the full text of the Apache License 2.0. You can create this file by going to your repository on GitHub, clicking on "Add file" -> "Create new file", naming it `LICENSE`, and then pasting the content of the Apache License 2.0 into it.
<br>
<br>
<br>
## Installation
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


