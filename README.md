# VSA - Vocational Skills Academy Backend

Vocational Skills Academy (VSA) is a Django-based platform that powerups the Vocation skill Academy Platform to provide users with a wide range of courses, from beginner to advanced levels. The platform uses RESTAPI to allows users to enroll in courses after login in 

## Features

* User authentication and authorization
* Course enrollment
* Payment gateway integration (Azampay)
* Transaction history

## Mobile Money Integration

The application supports various mobile money payment providers:

- **Airtel**
- **Tigo**
- **Halopesa**
- **Mpesa**

Payment status updates are handled through **webhook callbacks**.

## Authentication

The application uses **JWT authentication**. Tokens are stored securely and refreshed automatically when needed.

## Contribution and Installation

1. Clone the repository
2. Create a virtual environment and install the required packages using `pip install -r requirements.txt`
3. Create a PostgreSQL database and configure the database settings in `settings.py`
4. Run the migrations using `python manage.py migrate`
5. Start the development server using `python manage.py runserver`

> [!TIP]
> WHy the hustle while you can view on live environment

## 🚀 Live Demo

**Back-end:** [Vocational Skill Academy](https://vs-backend-alpha.vercel.app/api/courses)

**Project Link:** [https://github.com/klaus-gudy/vs-backend](https://github.com/klaus-gudy/vs-backend)

> Check @klaus-gudy for help
