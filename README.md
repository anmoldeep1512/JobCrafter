# JobCrafter

JobCrafter is a dynamic Web Application developed using Flask for backend, HTML and Bootstrap for frontend. This is a job creation platform where users can populate and submit form data which is processed, stored into the database and an email confirmation will be sent to the user notifying the successful submission.

## Installation 

For installation, you need python and pip as prerequisite.

1. Clone the repository:
```
git clone https://github.com/prbhv123/JobCrafter.git
cd JobCrafter
```
2. Create a virtual environment and install the dependencies from `requirements.txt`:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. Run the Application:
```
python3 app.py
```
## Features

- **Front-end Implementation** : Implemented using HTML and Bootstrap.
- **Back-end Implementation** : Developed using Python and Flask.
- **Form Data Handling** : Backend is capable of handling form data both via GET and POST requests. 
- **Data Storage** :  The application is integrated with SQLAlchemy for storing submitted data into database.
- **Email Confirmation** : On successful form submission, backend sends email confirmation to the recipient.
- **Front-end Alert** : On successful form submission, an alert is displayed on frontend.
