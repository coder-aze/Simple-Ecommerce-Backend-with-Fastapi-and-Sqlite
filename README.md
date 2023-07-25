# Simple E-commerce Backend with FastAPI

This is a simple e-commerce backend built using FastAPI, a modern, fast, web framework for building APIs with Python. The purpose of this project is to provide a basic structure for an e-commerce application, allowing developers to add and modify features as needed. Please note that the payment system is not implemented in this version, and anyone interested can add it or make any other modifications to suit their requirements.

## Endpoints
![screencapture-127-0-0-1-8080-docs-2023-07-25-13_05_06](https://github.com/coder-aze/Simple-Ecommerce-Backend-with-Fastapi-and-Sqlite/assets/32417925/9aa377c9-cb8e-477c-8b02-880c584fffa5)
### Login Page

- **POST** `/user/login`
  - Endpoint to handle user login.

- **POST** `/user/registration`
  - Endpoint to handle user registration.

### Get Users Page

- **GET** `/user/users`
  - Endpoint to retrieve all users.

### Business Page

- **POST** `/business/add`
  - Endpoint to add a new business to the database.

- **GET** `/business/get`
  - Endpoint to retrieve all businesses.

- **DELETE** `/business/delete`
  - Endpoint to delete a business.

### Product Page

- **POST** `/products/add`
  - Endpoint to add a new product to the database.

- **GET** `/products/get`
  - Endpoint to retrieve all products.

- **DELETE** `/products/delete`
  - Endpoint to delete a product.

- **PUT** `/products/update`
  - Endpoint to update a product.

## Usage

To run the FastAPI application, make sure you have Python installed, and then follow these steps:

1. Clone the repository from GitHub.
2. Create a virtual environment using `virtualenv`. If you don't have `virtualenv` installed, you can install it using `pip`:
   ```
   pip install virtualenv
   ```
   Then, create the virtual environment:
   ```
   virtualenv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Your virtual environment is now active. You'll see `(venv)` at the beginning of your command prompt, indicating that you're inside the virtual environment.

5. Install the required dependencies inside the virtual environment:
   ```
   pip install -r requirements.txt
   ```

6. Run the FastAPI application using Uvicorn:
   ```
   uvicorn main:app --reload
   ```
7. The application will start, and you can access the API endpoints at `http://localhost:8000`.

Feel free to customize and extend this project according to your specific requirements. Happy coding!
