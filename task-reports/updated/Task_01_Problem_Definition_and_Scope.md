# Delivery Promise Calculator — Task 1: Problem Definition and Scope
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Define the operational logistics problem of delivery date estimation, establish the project scope, identify target personas, specify constraints, and outline success metrics for a production-grade automated DevOps delivery platform.

---

### 2. Problem Statement
In modern e-commerce and logistics operations, customer trust and operational efficiency hinge on accurate delivery promises:
- **Naive Estimation Failures:** Legacy systems rely on static calculations (`order_date + N_days`) that disregard shipping speed tiers (Same-Day, Express, Standard, Economy), warehouse handling buffers, and non-operational weekend transit delays.
- **Logistics Opacity & SLA Breaches:** Customers lack granular milestone tracking, leading to high support ticket volume and missed SLA commitments.
- **Lack of Role Separation:** Warehouse handlers require rapid status progression tools (Pending -> Processing -> Shipped -> Delivered), while retail customers require self-service tracking and pre-dispatch cancellation.
- **Infrastructure & Deployment Fragility:** Manual deployments suffer from environment drift, untested releases, and deployment downtime without an automated CI/CD pipeline, containerization, and configuration management.

---

### 3. Target User Personas
1. **Administrators (Admin Director):** Full administrative oversight, delivery order booking, authorized status updates, data exports, and audit logging.
2. **Operations Staff (Operations Lead):** Warehouse processing, dispatch coordination, milestone status progression, and SLA compliance monitoring.
3. **Retail Customers (Customer):** Self-service parcel tracking via unique tracking numbers, delivery date estimation, and cancellation before dispatch.

---

### 4. System Scope & Core Capabilities
- **Multi-Role Authentication & Session Management:** Dedicated sign-in portal with demo personas and instant click-to-autofill credential support for seamless live evaluation.
- **Smart Delivery Promise SLA Engine:** Dynamic delivery date calculation taking into account **Shipping Speed Tiers** (`SAME_DAY`, `EXPRESS`, `STANDARD`, `ECONOMY`) and business transit days.
- **Unique Parcel Tracking Codes:** Autonomous generation of standard tracking codes (e.g. `TRK-IN-9821`, `TRK-IN-4412`).
- **Interactive Delivery Management Hub (`/deliveries`):** Live delivery creation with realistic Indian consumer orders (Apple MacBook Pro to Pune, Sony Headphones to Noida, Samsung 65" TV to Bengaluru), dynamic search, and status filtering.
- **Real-Time Analytics Dashboard (`/dashboard`):** Real-time fulfillment SLA metrics, shipping tier volume breakdown, and status distribution.
- **Customer Self-Service Tracking Portal (`/track`):** Public milestone journey stepper from order receipt to doorstep delivery.
- **Automated DevOps Toolchain:** Git version control, Jenkins CI/CD declarative pipeline, automated Selenium UI testing, Docker containerization, and Puppet configuration management.

---

### 5. Technical Stack & Constraints
| Component | Technology | Specification / Version |
| :--- | :--- | :--- |
| Backend Framework | Spring Boot | 4.0.0-M3 / Java 21 (LTS) |
| Relational Database | SQLite | 3.45.1 (`delivery_promise.db`) via Hibernate 7 |
| Template Engine | Thymeleaf | Server-side rendered glassmorphism UI |
| Build Tool | Apache Maven | 3.9.16 via Maven Wrapper (`mvnw`) |
| CI/CD Automation | Jenkins | Declarative Pipeline (`Jenkinsfile`) |
| Automated UI Testing | Selenium WebDriver | 4.28.1 + JUnit 5 with Headless Chrome |
| Containerization | Docker | Eclipse Temurin 21 Alpine JRE Image |
| Configuration Mgmt | Puppet | Declarative manifest (`delivery_promise.pp`) |

---

### 6. Success Criteria
1. Delivery promise dates are dynamically calculated based on transit days and shipping tiers with 100% calculation accuracy.
2. End-to-end automated Selenium tests achieve 100% pass rate locally and in headless CI pipeline execution.
3. Multi-role authentication operates reliably with 13/13 passing automated unit tests.
4. Docker container build and deployment execute without human intervention via Jenkins Pipeline as Code.
5. Puppet configuration management reliably remediates unauthorized configuration drift.

---

### 7. Actual Project Screenshots & Technical Evidence

#### Figure 1. High-Level Logistics Platform & Delivery Promise Calculator (Live on localhost:8765)
![High-Level Logistics Platform](../screenshots/task03_app_homepage.png)
*Figure 1: The running Delivery Promise Calculator platform showing the automated logistics engine, real-time KPI metrics, interactive calculator simulator, and student project evaluation credentials.*

#### Figure 2. Project Baseline GitHub Repository & Scope Specification
![Project Baseline GitHub Repository](../screenshots/original/task01_p3_img1.png)
*Figure 2: GitHub repository initialization showing version-controlled project structure and initial problem definition scope.*\n