# Email Spam Classification Flask App

This repository contains a simple Flask application for classifying emails as spam or not spam. The classification is based on a pre-trained model using a Count Vectorizer (`cv.pkl`) and a classifier (`clf.pkl`). The application takes the email body as input through a text area, and the result of the classification is displayed.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the user interface.
- `models/cv.pkl`: Pickle file containing the trained Count Vectorizer.
- `models/clf.pkl`: Pickle file containing the trained classifier.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/2002nishthajain/Email-spam-classification
    ```

2. Install the required dependencies. It is recommended to create a virtual environment for this:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your web browser and go to http://127.0.0.1:8080/ to access the application.

5. Enter the email body in the provided text area and click the "Classify" button to get the spam or not spam classification.

## Deployment and Testing

The application is deployed on Render. ThunderClient was used for testing the application by sending JSON format data. The deployed application can be tested using the ThunderClient collection provided in the `tests` directory.

## Note

This repository is created for practice purposes. 
