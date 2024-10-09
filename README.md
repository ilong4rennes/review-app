# ReviewMaster

**ReviewMaster** is a Django-based web application similar to Yelp, allowing users to review businesses and share their ratings.

## Features

- Users can browse businesses and view details about each one.
- Users can submit reviews and rate businesses.
- Businesses and reviews are linked via a many-to-many relationship, allowing users to review multiple businesses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ilong4rennes/review-master.git
    cd review-master
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

6. Visit the app at `http://127.0.0.1:8000/`.

## Usage

- Visit `/businesses/` to view the list of businesses.
- Visit `/users/` to view the list of users.
- Add reviews to businesses and explore the business review system.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.


