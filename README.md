# Welcome to Covax
## Spreading vaccination resources, spreading happiness, fighting COVID-19
Covax gathers information to teach people where they can get vaccinated if they are eligible. It will crowdsource ongoing experiences of vaccinations, vaccination appointments, and resources to set appointments while sharing information on groups that have been allotted vaccinations at particular locations. 

Users will share experiences so that others may learn where appointments can be made, if vaccines are available, if they are no longer available, and to whom they are made available. 

Users will use the application to report on their experiences with a given resource to determine if appointments can be made in real time.

Our efforts will help our community find vaccination resources in a time of uncertainty while expediting vaccination efforts for the institutions that distribute them.

### Running Covax Locally

To get this up and running, clone the repository and navigate in your terminal to the repository directory. Add a secret key (random string of characters) to the local_template.env file and run `source local_template.env` in your terminal. Run `pip install -r requirements.txt`. Run `python manage.py migrate` and finally, run `python manage.py runserver` to start up your development server.

### Creating Dummy Data

To add data to this project, first create users. You will have to make a superuser by running `python manage.py createsuperuser` and following the prompt in your terminal. After that, go to `http://localhost:8000` to sign in and create other users.

Once you have created other users you must create locations first, then votes, then appointments. Create them using the following

* `python manage.py populate_data --locations=5` to create 5 new location objects in the database
* `python manage.py populate_data --votes=5` to create 5 new vote objects in the database
* `python manage.py populate_data --appointments=5` to create 5 new appointment objects in the database
