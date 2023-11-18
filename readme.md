# Instagram Clone README

## Description
This is a simple Instagram-like web application implemented using Python, HTML, CSS, and JavaScript. The backend utilizes the Flask framework, and SQLite is used as the database. The application includes features such as user authentication (login, signup, reset password), profile management (edit profile), post management (create post, edit post), and social interaction (like posts). Additionally, there is an intentionally non-functional "Forgot Password" feature for demonstration purposes.

## Installation
1. Make sure you have Python 3 installed on your system.
2. Clone the repository:

    ```bash
    git clone https://github.com/arv1903/instagram-clone.git
    ```

3. Navigate to the project directory:

    ```bash
    cd instagram-clone
    ```

4. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

5. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

6. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you are in the project directory and the virtual environment is activated.

2. Run the Flask application:

    ```bash
    python3 app.py
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/`.

4. Explore the Instagram clone and test the various features, such as login, signup, reset password, edit profile, create post, edit post, and like posts.

## Folder Structure
- `templates`: HTML templates for different pages.
- `static`: Contains static files like CSS and JavaScript.
- `app.py`: Main Flask application file.
- `models.py`: Database models for users and posts.
- `utils.py`: Utility functions.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite

## Known Issues
- The "Forgot Password" feature is intentionally non-functional for demonstration purposes.

## Contributing
Feel free to contribute by opening issues or submitting pull requests.