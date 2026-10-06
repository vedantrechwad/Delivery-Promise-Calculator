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