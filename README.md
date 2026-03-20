# Expense Tracker API

Backend API + slick dashboard for personal expense tracking.

## Current Capabilities

- JWT auth (signup/login)
- CRUD expenses with filters
- Postgres via `DATABASE_URL`
- Docker + docker-compose (API + small Postgres)
- Seed script + smoke test
- Dashboard UI served by the same FastAPI app (`/dashboard`)

## Stack

- FastAPI + SQLAlchemy + Alembic
- PostgreSQL
- Docker


## Installation

1. Clone this repository on your local machine:

   ```bash
   git clone https://github.com/Tomu98/Expense-Tracker-API.git
   ```

2. Go to the project directory:

   ```bash
   cd Expense-Tracker-API
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv          # Create a virtual environment
   .venv\Scripts\activate        # Activate the environment in Windows
   source .expvenv/bin/activate  # Activate the environment in Linux/MacOS
   ```

4. Install the necessary dependencies for the project using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. This project uses environment variables to configure the connection to the database and a secret key for JWT authentication. You must create a file named `.env` in the root directory of the project with the following variables:

   ```bash
   DATABASE_URL=postgresql://<your_user>:<your_password>@localhost/<your_database>
   SECRET_KEY=<generated_unique_key>
   ```

   For the `SECRET_KEY`, you can generate a secure key by running the following command in your terminal:
   
   ```bash
   openssl rand -hex 32
   ```

   Copy the generated value and assign it to the `SECRET_KEY` variable in your `.env` file. If you plan to use a different database, such as SQLite or MySQL, simply update the `DATABASE_URL` with the connection string relevant to your chosen database.

   > Note: Make sure not to include the .env file in version control, as it contains sensitive information. The project is already configured with a .gitignore file to automatically exclude this file.

6. Start the API development server with the following command:

    ```bash
    uvicorn app.main:app --reload
    ```

### Docker (API + small Postgres)

```bash
cp .env.example .env
# edit SECRET_KEY

docker compose up --build
python scripts/seed.py
python scripts/smoke_test.py
```

API: http://localhost:8080
Docs: http://localhost:8080/docs
Dashboard: http://localhost:8080/dashboard/

<br>

By following these steps, you'll be able to install and run the Expense Tracker API in your local environment.
Adjust the `.env` file if you need to change the database or authentication settings.

<br>

## Fly.io Deployment

```bash
flyctl auth login
flyctl launch --no-deploy
flyctl postgres create --name expense-tracker-db --region otp
flyctl postgres attach --app expense-tracker expense-tracker-db
flyctl secrets set SECRET_KEY=$(openssl rand -hex 32)
flyctl deploy
```

Dashboard: https://expense-tracker.fly.dev/dashboard/
Docs: https://expense-tracker.fly.dev/docs

## Running Tests

This project uses pytest to perform automated tests to ensure the reliability and functionality of key features.
To run the tests, use the following command:
```bash
pytest
```

<br>

## How to use it

Once the application is running, you can access Swagger's interactive API documentation at 
`http://localhost:8080/docs`, where you can visualize and test the available API endpoints.

### Main Endpoints

**Authentication:**
- **POST** `/signup` - User registration.
- **POST** `/login` - User login (form data: `username`, `password`).

After login, use the JWT:

```
Authorization: Bearer <access_token>
```

**Expenses:**
- **GET** `/expenses` - Retrieve a list of expenses.
- **POST** `/expenses` - Create a new expense.
- **PUT** `/expenses/{id}` - Update an expense by ID.
- **DELETE** `/expenses/{id}` - Delete an expense by ID.

**User Account:**
- **PUT** `/user` - Update the username.
- **DELETE** `/user` - Delete the user account.

<br>

## Feedback & Contributions

I want to clarify that this is my first API project (of the many I want to do), and I welcome any feedback or contributions. If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

<br>

### **Thanks for checking out the project 🤍**



