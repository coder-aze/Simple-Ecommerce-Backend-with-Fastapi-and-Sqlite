# Simple E-commerce Backend with FastAPI

This is a straightforward and efficient e-commerce backend developed using FastAPI, a cutting-edge web framework renowned for its speed and exceptional performance with Python. The main objective of this project is to provide a basic structure for an e-commerce application, allowing developers to quickly set up and customize essential functionalities to match their specific needs.

FastAPI's exceptional performance ensures that the backend runs smoothly and efficiently, making it ideal for handling e-commerce processes without any performance bottlenecks. Additionally, this backend features a secure authentication system powered by JSON Web Tokens (JWT), ensuring that user data remains protected throughout the application.

Please note that while this version does not include a payment system, interested users can effortlessly integrate their preferred payment solutions or tailor the backend to suit their individual requirements.

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

6. To add authentication to your FastAPI application, you can use a secret key for securing your API endpoints. Here's how you can do it:
   ```
   SECRET_KEY="YOUR_SECRET_KEY"
   ```

  Replace `YOUR_SECRET_KEY` from example.env file with a strong, unique secret key. This key will be used to sign and verify authentication tokens.

7. Run the FastAPI application using Uvicorn:
   ```
   uvicorn main:app --reload
   ```
8. The application will start, and you can access the API endpoints at `http://localhost:8000`.

Feel free to customize and extend this project according to your specific requirements. Happy coding!
