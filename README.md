

# E-commerce for Arts. Full-Stack Web Application with Django, HTML, CSS, JavaScript, and Integrated Payment System

## Project Overview

This project is a full-stack web application built using **Django**, **HTML**, **CSS**, and **JavaScript**. It integrates **SQLite** as the database for storing and managing application data. The frontend is designed to provide a responsive, user-friendly experience, while the backend leverages Django’s robust features for data management, server-side logic, and user authentication. Additionally, the application includes integrated payment functionality.

## Features

- **Django Framework**: 
  - Handles backend logic for user requests and responses.
  - Efficient data management using **SQLite** as the database.

- **Frontend Design**: 
  - Built with **HTML** and styled using **CSS** to create a responsive, user-friendly interface.
  - Dynamic elements and interactivity powered by **JavaScript**.

- **Data Management**:
  - Supports **CRUD (Create, Read, Update, Delete)** operations for managing application data.
  - Database interactions are handled using **Django models** and **SQLite**.

- **Custom Functionalities**:
  - Features tailored to the specific use case, such as **user authentication**, **data visualization**, or **interactive forms**.
  - Integrated **payment method** for processing transactions securely.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Installation and Setup

To set up and run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/techsamagan/E_commerce_gallery_store/
   ```

2. Navigate to the project directory:

   ```bash
   cd E_commerce_gallery_store
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at: 

   [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

- Explore the app's interface to access its features.
- Perform CRUD operations seamlessly with Django's backend integration.
- Utilize the integrated payment system for secure transactions.

## Future Improvements

- Add more interactivity using advanced **JavaScript** frameworks (e.g., React, Vue.js).
- Upgrade the database to a more scalable solution if needed (e.g., PostgreSQL, MySQL).
- Enhance the UI/UX for better accessibility and responsiveness.
