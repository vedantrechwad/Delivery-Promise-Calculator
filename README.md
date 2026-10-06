# Puppet-Provisioned Delivery Promise Calculator

A DevOps-oriented Spring Boot application for managing delivery records and calculating promised delivery dates.

## Technology Stack

- Java 21
- Spring Boot
- Maven
- SQLite
- Spring Data JPA / Hibernate
- Thymeleaf
- Git / GitHub
- Jenkins
- Selenium
- Docker
- Puppet

## Features

- Create delivery records
- Calculate promised delivery date
- View delivery records
- Search by customer or product
- Update delivery status
- View delivery summary
- SQLite database persistence

## Project Structure

src/
├── main/
│   ├── java/com/deliverypromise/calculator/
│   │   ├── controller/
│   │   ├── model/
│   │   ├── repository/
│   │   └── service/
│   └── resources/
│       ├── templates/
│       └── application.properties

## Running the Application

```bash
mvn clean package
mvn spring-boot:run

## Task 6: MVP Completion and Git Collaboration

### MVP Features

The Delivery Promise Calculator MVP includes the following features:

- Create delivery records
- View delivery records
- Search deliveries by customer or product
- Calculate promised delivery date
- Update delivery status
- Delivery dashboard with summary statistics
- Input validation for delivery records
- Role-based delivery status workflow

### Role-Based Workflow

The application supports three roles:

- **ADMIN** – Can view deliveries and update delivery status
- **OPERATIONS** – Can view deliveries and update delivery status
- **CUSTOMER** – Can view and search deliveries but cannot update delivery status

The role is maintained using the application session.

### Dashboard

A dashboard is available at:

`http://localhost:8765/dashboard`

The dashboard displays:

- Total deliveries
- Pending deliveries
- Delivered deliveries

### Git Collaboration

The Task 6 feature is developed using a separate feature branch:

`feature/mvp-dashboard`

The feature will be tested locally, committed, pushed to GitHub, and merged into the `main` branch through a Pull Request.

## Collaboration Demo

MVP dashboard and role-based workflow implemented and tested locally.

## Collaboration Demo

Task 6 collaboration changes were developed using Git feature branches.
