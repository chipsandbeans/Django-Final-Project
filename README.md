# Munchy App

## Table of Contents
1. [User Experience Design](#user-experience-design)
2. [Features](#features)
3. [Agile](#agile)
4. [Testing](#testing)
5. [Installation](#installation)
6. [Technologies](#technologies)

## User Experience Design

### User Stories
1. **As a user**, I want to track my meals so that I can monitor my diet.
2. **As a user**, I want to create and update my meals so that I can easily manage my diet plan.
3. **As a user**, I want to delete a meal when I no longer need it.
4. **As a user**, I want to view my weight history and log my current weight to keep track of my progress.
5. **As a user**, I want to receive clear notifications when I successfully create, update, or delete meals and weights.
6. **As a user**, I want to be informed when I am not logged in and redirected to the login page.
7. **As a user**, I want to be redirected to the home page if I am already logged in.

### User Flow
1. **Sign Up / Log In**: Users can create an account or log in to access their meal and weight tracking dashboard.
2. **Meal Management**: Users can add, update, or delete their meals.
3. **Weight Tracking**: Users can log their weight and see a history of their logged weights.
4. **Notifications**: Users receive feedback messages on successful actions like adding meals, deleting weights, etc.
5. **Responsive Design**: The app works well on both mobile and desktop devices, with meal cards and weight entries adapting to screen sizes.

## Features

1. **Meal Tracking**:
   - Users can log their meals, including details about protein, carbs, and fats.
   - Users can update or delete meals they've created.
   - Responsive layout for mobile and desktop users.

2. **Weight Tracking**:
   - Users can log their weight entries and track progress over time.
   - Users can update or delete weight entries.

3. **User Authentication**:
   - Sign-up and login functionality for secure access to meal and weight tracking.
   - Users are redirected if they try to access restricted pages while not logged in.
   - Messages displayed on meal/weight updates, creations, deletions, and logout.

4. **Dynamic and Adaptable Interface**:
   - The website adapts to all screen sizes, ensuring a smooth experience across devices.
   - Background images adjust for different screen resolutions.

5. **User Feedback with Messages**:
   - Users receive messages confirming actions like meal updates, weight tracking entries, or logouts.

### Screenshots
![Home Page](images/homepage-screenshot.png)  
*Example of the home page showing meal entries.*

![Meal Creation](images/meal-creation-screenshot.png)  
*Screenshot of the meal creation form.*

![Weight Tracking](images/weight-tracking-screenshot.png)  
*Example of the weight tracking interface.*

## Agile

This project follows an Agile methodology, utilizing a project board to manage tasks, sprints, and milestones.

- **Project Board**:[ [Link to Project Board](#)](https://github.com/chipsandbeans/django-blog1/projects?query=is%3Aopen)
- Tasks and user stories are organized into sprints for efficient delivery.

## Testing

Testing was conducted throughout the development process to ensure that all features work as expected.

### Manual Testing
- **Meal Management**: Tested meal creation, updates, and deletion to ensure correct handling of user input and feedback messages.
- **Weight Management**: Ensured that weight entries can be added, updated, and deleted correctly.
- **User Authentication**: Verified that logged-in users are redirected to the correct pages and logged-out users are prompted with the login message.


### Screenshots of Tests


### Known Issues
- An error displays on some 

## Installation

To run the Munchy app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/munchy.git
   cd munchy
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Navigate to `http://localhost:8000` to access the app.

## Technologies

- **Django**: Python web framework used for backend development.
- **PostgreSQL**: Database used for storing user data, meals, and weight entries.
- **Bootstrap**: Front-end framework for responsive design.
- **JavaScript**: Used for dynamic and interactive components.
- **GIT**: Used git for version control using the gitpod terminal.
- **Heroku**: Used to deploy the live project.
- **Github**: The Project's code was stored in github.
- **PEP8**: Python code was validated using PEP8.
- **W3C HTML**: Validated HTML code using W3C'S HTML validator.
- **W3C HTML**: Validated CSS code using W3C'S CSS validator.
- **Chrome Devtools**: Used devtools on google chrome to test website responsiveness and to check for bugs.
