# Software Architecture: DFIR Case Management System

## Design Pattern: MVC (Model-View-Controller)
This application strictly follows the MVC design pattern to separate concerns, making the codebase maintainable and scalable.

* **Model (Data):** Handled by `Flask-SQLAlchemy`. Models represent our database tables (Cases, Evidence, Users).
* **View (UI):** Handled by `Jinja2` templates and Bootstrap. This is the HTML the user interacts with.
* **Controller (Logic):** Handled by Flask route functions. The controller takes the user's request, queries the Model, and passes the data to the View.

## Request Lifecycle
When a user interacts with the app, the data flows in a specific, predictable loop:

1. **Browser** sends an HTTP request (e.g., clicking "View Case").
2. **Flask** matches the URL to a specific route function (Controller).
3. **Route** queries the SQLite/PostgreSQL Database via the SQLAlchemy ORM (Model).
4. **Route** passes the retrieved data into a Jinja HTML Template (View).
5. **Server** sends the rendered HTML back to the Browser.

## Application Structure (Flask Blueprints)
To prevent `app.py` from becoming a massive, unmaintainable file with 50+ routes, this project utilizes **Flask Blueprints**. We divide the application into distinct feature modules:
* `/auth` (Login, Logout, Session management)
* `/cases` (Case creation, listing, updating)
* `/evidence` (Evidence ingestion, hashing, chain-of-custody logging)
* `/reports` (PDF/HTML generation)

## Authentication & Session Flow
1. User submits login form.
2. Server verifies the password hash using `werkzeug.security`.
3. Upon success, `Flask-Login` issues a secure, HTTP-only session cookie.
4. Future requests include this cookie to identify the user.
5. The `@role_required` decorator checks the user's role against the requested route (e.g., blocking an Analyst from viewing Admin logs).