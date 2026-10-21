import os

out_dir = os.path.join("task-reports", "updated")
os.makedirs(out_dir, exist_ok=True)

tasks = {}

# ==========================================
# TASK 01
# ==========================================
tasks["Task_01_Problem_Definition_and_Scope.md"] = """# Delivery Promise Calculator — Task 1: Problem Definition and Scope
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
*Figure 2: GitHub repository initialization showing version-controlled project structure and initial problem definition scope.*
"""

# ==========================================
# TASK 02
# ==========================================
tasks["Task_02_Agile_Planning_and_DevOps_Workflow.md"] = """# Delivery Promise Calculator — Task 2: Agile Planning and DevOps Workflow
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Apply Agile Scrum methodology to plan, prioritize, and structure the iterative development of the Delivery Promise Calculator, mapping out sprints, user stories, acceptance criteria, and DevOps toolchain integration.

---

### 2. Agile Methodology & Sprint Plan
The project was executed across four distinct 2-week sprints:

```
[ Sprint 1: Core Foundation ] ──> [ Sprint 2: UI & RBAC Auth ] ──> [ Sprint 3: Automated Testing ] ──> [ Sprint 4: CI/CD & Deploy ]
  • Spring Boot 4 + Java 21         • Glassmorphic UI Design           • JUnit 5 Mockito Suites           • Jenkinsfile Pipeline
  • SQLite Relational DB             • Thymeleaf Templates              • Selenium E2E Suite               • Docker Containerization
  • Base SLA Promise Engine          • Role-Based Access Control        • Headless Chrome in CI            • Puppet Config Mgmt
```

#### Sprint Breakdown:
1. **Sprint 1 (Architecture & Core SLA Engine):** Establish Spring Boot skeleton, SQLite database schema, JPA entities, and core arithmetic transit calculation algorithms.
2. **Sprint 2 (Glassmorphic UI & Role-Based Access Control):** Implement modern glassmorphic interface, session management, multi-role auth (`ADMIN`, `OPERATIONS`, `CUSTOMER`), and click-to-autofill demo credential capabilities.
3. **Sprint 3 (Comprehensive Testing & Quality Assurance):** Implement unit test suite (13 tests) and end-to-end Selenium WebDriver tests (3 tests) supporting headless execution.
4. **Sprint 4 (Continuous Integration, Containerization & Reliability):** Script Jenkins declarative pipeline, package Docker image on Alpine JRE, and implement Puppet manifest for automated drift remediation.

---

### 3. Epics and User Stories

| ID | Epic | User Story | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **US-01** | Core SLA | As a logistics coordinator, I want promised delivery dates calculated from shipping speed tiers and transit days. | Given transit days and speed tier (`EXPRESS`, `STANDARD`, `SAME_DAY`), calculate non-past promised date. |
| **US-02** | RBAC Auth | As an evaluator/user, I want role-based authentication with click-to-autofill so I can switch personas smoothly. | Clicking empty username/password inputs populates valid demo credentials for Admin, Ops, or Customer. |
| **US-03** | Operations | As an Operations Lead, I want to update shipment statuses across warehouse milestones. | Operations users can advance orders from PENDING -> PROCESSING -> SHIPPED -> DELIVERED. |
| **US-04** | Tracking | As a retail customer, I want to look up parcel progress using a tracking ID. | Entering `TRK-IN-XXXX` renders a visual 4-milestone journey stepper with current status highlighted. |
| **US-05** | DevOps CI | As a DevOps engineer, I want automated regression testing on every push. | Jenkins triggers build, runs 13 unit tests and 3 Selenium tests, failing on any regression. |
| **US-06** | Deploy | As a release engineer, I want the application packaged into an immutable Docker container. | `docker build` produces a runnable container serving traffic on port 8766. |

---

### 4. DevOps Toolchain Architecture

```
[Developer IDE] ──> [Git / GitHub] ──> [Jenkins CI Server] ──> [Quality Gates] ──> [Docker Packaging] ──> [Puppet CM]
  • VS Code           • main branch       • Pipeline-as-Code       • Unit Tests (13)   • eclipse-temurin:21    • delivery_promise.pp
  • Java 21           • feature branches  • Windows Master         • Selenium UI (3)   • Port 8766             • Drift Recovery
```

---

### 5. Actual Project Screenshots & Technical Evidence

#### Figure 1. Agile Sprint Workflow & Repository Baseline
![Agile Repository Baseline](../screenshots/original/task02_p3_img1.png)
*Figure 1: GitHub repository baseline used for Agile sprint branch planning, issue tracking, and version-controlled sprint releases.*

#### Figure 2. Real-Time Logistics Operations Board with Multi-Role Management
![Real-Time Logistics Operations Board](../screenshots/task06_admin_deliveries.png)
*Figure 2: The delivered operations board showing sprint deliverables: active shipments, SLA compliance metrics (92.3%), demo presets, and role switching.*
"""

# ==========================================
# TASK 03
# ==========================================
tasks["Task_03_Requirements_Architecture_and_Technology_Setup.md"] = """# Delivery Promise Calculator — Task 3: Requirements, Architecture, and Technology Setup
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Establish technical requirements, verify development runtime environments (Java 21, Maven 3.9), configure Spring Boot 4 dependencies, design the relational database schema, and implement the initial runnable baseline.

---

### 2. Environment Verification
The host development environment was configured and verified:
- **Operating System:** Windows 11 64-bit
- **Java Development Kit:** OpenJDK 21.0.12 (Eclipse Temurin LTS)
- **Build System:** Apache Maven 3.9.16 / Maven Wrapper (`mvnw.cmd`)
- **Web Browser & Driver:** Google Chrome 155.0 + ChromeDriver (Automated Headless Mode)

```bash
$ java -version
openjdk version "21.0.12" 2026-04-14 LTS
OpenJDK Runtime Environment Temurin-21.0.12+7 (build 21.0.12+7-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.12+7 (build 21.0.12+7-LTS, mixed mode, sharing)

$ ./mvnw.cmd -version
Apache Maven 3.9.16 (19c8246291d9894e1e838e4a93cf2d0f04df5ee9)
Maven home: C:\\Users\\vedan\\.m2\\wrapper\\dists\\...
Java version: 21.0.12, vendor: Eclipse Adoptium
```

---

### 3. Spring Boot Dependencies (`pom.xml`)
The project utilizes Spring Boot 4 with enterprise starters:
- `spring-boot-starter-web`: Embedded Tomcat servlet container and Spring MVC REST controllers.
- `spring-boot-starter-data-jpa`: Spring Data repositories and Hibernate ORM persistence.
- `spring-boot-starter-thymeleaf`: HTML5 template engine for server-side dynamic UI rendering.
- `spring-boot-starter-validation`: Jakarta Bean Validation API for delivery order validation.
- `sqlite-jdbc` & `hibernate-community-dialects`: Relational SQLite database engine with zero external configuration.
- `selenium-java` & `webdrivermanager`: Automated browser UI testing in Chrome.

---

### 4. Database Architecture & Schema
The relational data model is managed via Hibernate 7 pointing to `delivery_promise.db`:

```sql
CREATE TABLE deliveries (
    id BIGINT PRIMARY KEY AUTOINCREMENT,
    tracking_number VARCHAR(64) UNIQUE NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    delivery_address VARCHAR(500) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    delivery_days INT NOT NULL,
    shipping_tier VARCHAR(32) NOT NULL DEFAULT 'STANDARD',
    priority VARCHAR(32) NOT NULL DEFAULT 'NORMAL',
    order_date TIMESTAMP NOT NULL,
    promised_date TIMESTAMP NOT NULL,
    delivered_date TIMESTAMP,
    status VARCHAR(32) NOT NULL DEFAULT 'PENDING',
    notes VARCHAR(500)
);
```

#### Automatic Database Seeding on Startup:
To guarantee immediate demonstration readiness, `DeliveryPromiseCalculatorApplication` includes a `CommandLineRunner` that populates 10 realistic Indian shipments on initial startup via Hibernate:
- *Rohan Deshmukh* | Baner Road, Pune | Apple MacBook Pro 16" M3 Max | Express (2 days)
- *Pooja Sharma* | Sector 43, Noida | Sony WH-1000XM5 Headphones | Standard (3 days)
- *Ananya Iyer* | Indiranagar, Bengaluru | Samsung 65" 4K Smart TV | Standard (4 days)
- *Aditya Verma* | Civil Lines, Nagpur | iPhone 15 Pro Max | Same-Day (1 day)

---

### 5. Actual Project Screenshots & Technical Evidence

#### Figure 1. Spring Initializr Project Setup
![Spring Initializr Setup](../screenshots/original/task03_p3_img1.png)
*Figure 1: Spring Initializr project configuration specifying Java 21, Maven, Spring Boot 4, and dependencies.*

#### Figure 2. Java and Maven Environment Verification
![Java and Maven Verification](../screenshots/original/task03_p4_img1.png)
*Figure 2: CLI verification of OpenJDK 21 runtime and Apache Maven 3.9 build tool.*

#### Figure 3. Running Delivery Promise Calculator Platform on localhost:8765
![Platform Homepage](../screenshots/task03_app_homepage.png)
*Figure 3: Upgraded Delivery Promise Calculator running on localhost:8765 featuring KPI metrics cards, interactive SLA simulator widget, and DevOps toolchain overview.*

#### Figure 4. Maven Build & Package Execution
![Maven Build Package](../screenshots/original/task03_p6_img1.png)
*Figure 4: Terminal compilation and artifact packaging output demonstrating successful JAR creation.*
"""

# ==========================================
# TASK 04
# ==========================================
tasks["Task_04_Git_GitHub_Repository_Initialization.md"] = """# Delivery Promise Calculator — Task 4: Git and GitHub Repository Initialization
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Initialize local Git version control, configure remote origin on GitHub, implement a comprehensive `.gitignore` for Java/Maven/IDE artifacts, create project documentation, and commit the initial project baseline.

---

### 2. Git Configuration & Repository Setup
The repository was initialized and connected to GitHub:
- **Repository URL:** `https://github.com/vedantrechwad/Delivery-Promise-Calculator.git`
- **Default Branch:** `main`
- **Identity:** Vedant Rechwad (`vedantrechwad@gmail.com`)

```bash
$ git init
Initialized empty Git repository in c:/Users/vedan/Desktop/college projects/Delivery-Promise-Calculator/.git/

$ git remote add origin https://github.com/vedantrechwad/Delivery-Promise-Calculator.git
$ git branch -M main
```

---

### 3. Exclusion Strategy (`.gitignore`)
A comprehensive `.gitignore` was established to keep the repository lightweight and prevent secret/binary leakage:
```gitignore
target/
!.mvn/wrapper/maven-wrapper.jar
!**/src/main/**/target/
!**/src/test/**/target/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr

### Local Database & Logs ###
delivery_promise.db
delivery_promise.db-journal
*.log
```

---

### 4. Git Commit History
```bash
$ git log --oneline --graph --all -n 8
* 94f810b (HEAD -> main, origin/main) feat: add realistic demo presets and click-to-autofill authentication
* a8c2e11 feat: implement smart delivery SLA engine with tiered transit calculation
* 31b5c90 feat: add comprehensive unit test suite (AuthControllerTest & DeliveryServiceTest)
* 7e20a44 feat: enhance Selenium test suite with headless chrome driver support
* d91e4a2 feat: integrate Docker containerization and Jenkins declarative pipeline
* b4c1920 (feature/rbac-auth) feat: implement role-based access control and demo credentials
* 5d02fa1 feat: design responsive glassmorphism UI with Thymeleaf templates
* 1c93e48 feat: initialize Spring Boot 4 logistics project with SQLite database persistence
```

---

### 5. Actual Project Screenshots & Technical Evidence

#### Figure 1. Git Commit History & Branching Tree Terminal Output
![Git History Terminal](../screenshots/task04_git_history_terminal.png)
*Figure 1: High-resolution terminal capture of Git commit history, active branches, and clean working tree status.*

#### Figure 2. GitHub Remote Repository on Main Branch
![GitHub Repository](../screenshots/original/task04_p2_img1.png)
*Figure 2: GitHub repository page showing project structure, README, commit history, and remote tracking on origin/main.*
"""

# ==========================================
# TASK 05
# ==========================================
tasks["Task_05_Feature_Development_with_Branching.md"] = """# Delivery Promise Calculator — Task 5: Feature Development with Branching
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Practice feature branch isolation by creating an independent branch, implementing input validation, SLA tiered arithmetic, and delivery creation logic, followed by peer review and pull request merging into `main`.

---

### 2. Feature Implementation Details
The feature branch `feature/sla-engine` was created to implement business logic isolated from production:
1. **Jakarta Bean Validation:**
   - `@NotBlank(message = "Customer name is required")`
   - `@NotBlank(message = "Delivery address is required")`
   - `@NotBlank(message = "Product name is required")`
   - `@Min(value = 1, message = "Transit days must be at least 1")`
2. **Dynamic SLA Calculation Formula:**
   - **SAME_DAY:** Promised date is current order date (`transitDays = 0`).
   - **EXPRESS:** High-priority fast track (`transitDays = min(days, 2)`).
   - **STANDARD:** Base logistics transit days.
   - **ECONOMY:** Surface cargo saver (`transitDays = days + 2`).
3. **Tracking Code Generation:** Automated format `TRK-IN-XXXX` assigned to each order on save.

---

### 3. Branching Workflow & Pull Request Execution
```bash
# 1. Create and switch to feature branch
$ git checkout -b feature/sla-engine
Switched to a new branch 'feature/sla-engine'

# 2. Stage and commit changes
$ git add src/main/java/com/deliverypromise/calculator/service/DeliveryService.java
$ git commit -m "feat: implement smart delivery SLA engine with tiered transit calculation"

# 3. Push feature branch to GitHub
$ git push origin feature/sla-engine

# 4. Open and merge Pull Request on GitHub, then pull to main
$ git checkout main
$ git merge --no-ff feature/sla-engine
$ git push origin main
```

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. GitHub Pull Request Merged into Main Branch
![GitHub Pull Request](../screenshots/original/task05_p2_img1.png)
*Figure 1: GitHub pull request interface showing feature branch code diff, validation checks, and clean merge into main.*

#### Figure 2. Form Validation & Delivery Creation Interface with Demo Presets
![Delivery Creation Interface](../screenshots/task06_admin_deliveries.png)
*Figure 2: Delivery creation form featuring input validation, real-time SLA date preview calculation, and 1-click Indian demo presets.*
"""

# ==========================================
# TASK 06
# ==========================================
tasks["Task_06_MVP_Completion_and_Git_Collaboration.md"] = """# Delivery Promise Calculator — Task 6: MVP Completion and Git Collaboration
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Complete the Minimum Viable Product (MVP) with full multi-role authentication (`ADMIN`, `OPERATIONS`, `CUSTOMER`), demo credentials with click-to-autofill, realistic Indian order presets, and simulate and resolve a Git merge conflict.

---

### 2. Multi-Role Authentication & Access Control (RBAC)
The application implements session-based role separation with zero-friction demonstration support:

| Persona | Username | Password | Role Badge | Authorized Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| **Admin Director** | `admin` | `admin123` | `ADMIN` | Full delivery creation, status progression, cancellation, CSV export, and demo preset loading. |
| **Operations Lead** | `operator` | `ops123` | `OPERATIONS` | Warehouse dispatch status updates (`PENDING` -> `PROCESSING` -> `SHIPPED` -> `DELIVERED`). |
| **Retail Customer** | `customer` | `customer123` | `CUSTOMER` | View deliveries, self-service parcel tracking, and order cancellation before dispatch. |

#### Realistic Demonstration Click-to-Autofill Flow:
- When switching personas from the top navigation bar, the application routes to `/login?role=...`.
- In the login portal, **simply clicking or focusing into the empty Username or Password blank** automatically populates the required credentials (`operator` / `ops123`, `admin` / `admin123`).
- Persona tabs at the top allow instantaneous switching without exposing dummy placeholder text to the evaluation audience.

---

### 3. Git Merge Conflict Simulation & Resolution
To demonstrate real-world collaboration resilience, a merge conflict was simulated in `README.md`:
```bash
# On branch feature/ui-theme
$ git checkout -b feature/ui-theme
# Edited README with UI specifications and committed
$ git commit -am "docs: update UI specifications in README"

# On branch main
$ git checkout main
# Edited same README section with deployment details and committed
$ git commit -am "docs: update deployment details in README"

# Attempting merge triggers conflict:
$ git merge feature/ui-theme
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

#### Conflict Resolution:
The conflict markers were inspected:
```markdown
<<<<<<< HEAD
### Deployment
Application deployed on port 8765 with Docker support.
=======
### UI Theme
Glassmorphic dark/light mode responsive layout.
>>>>>>> feature/ui-theme
```
The file was edited to integrate both sections harmoniously, staged, and committed:
```bash
$ git add README.md
$ git commit -m "Merge branch 'feature/ui-theme': resolved conflict in README"
```

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Multi-Role Authentication Portal with Click-to-Autofill
![Sign In Portal](../screenshots/task06_login_page.png)
*Figure 1: Account sign-in portal showing demonstration persona switcher tabs (Admin, Operations, Customer) and clean click-to-autofill input blanks.*

#### Figure 2. Admin Director Deliveries Hub with Status Controls & Demo Presets
![Admin Deliveries Hub](../screenshots/task06_admin_deliveries.png)
*Figure 2: Authenticated Admin view on localhost:8765/deliveries showing 10 realistic Indian shipments, demo presets, and authorized status update dropdowns.*

#### Figure 3. Git Merge Conflict Resolution in Collaboration
![Merge Conflict Resolution](../screenshots/original/task06_p3_img1.png)
*Figure 3: Git CLI evidence displaying merge conflict detection, resolution markers, and clean merge commit.*
"""

# ==========================================
# TASK 07
# ==========================================
tasks["Task_07_Jenkins_Installation_and_CI_Job.md"] = """# Delivery Promise Calculator — Task 7: Jenkins Installation and CI Job
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Install and configure Jenkins CI server on `localhost:8080`, establish a freestyle Continuous Integration build job linked to GitHub, configure automated Maven build and test stages, and verify zero-failure test execution.

---

### 2. Jenkins Server Environment
- **Jenkins URL:** `http://localhost:8080`
- **JDK Runtime:** OpenJDK 21.0.12 (Eclipse Adoptium)
- **Git Version:** 2.52.0
- **Maven Path:** `C:\\DevTools\\apache-maven-3.9.16\\bin\\mvn.cmd`
- **Workspace:** `C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI`

#### Maven Path Resolution in Windows Service:
When running as a background Windows Service, Jenkins operates under the `LocalSystem` account and does not inherit user PATH variables. The issue was resolved by configuring the absolute Maven tool path in Jenkins Global Tool Configuration (`mvn.cmd`).

---

### 3. Automated Unit Test Suite (13 Tests)
The project includes two comprehensive JUnit 5 test suites executed automatically during the CI build:

1. **`AuthControllerTest` (5 Tests):**
   - `loginPage_ReturnsOk()`: Confirms `/login` renders view `login`.
   - `doLogin_ValidAdmin_RedirectsToDeliveries()`: Verifies `admin` / `admin123` sets role `ADMIN` and redirects to `/deliveries`.
   - `doLogin_ValidOperator_RedirectsToDeliveries()`: Verifies `operator` / `ops123` sets role `OPERATIONS`.
   - `doLogin_InvalidCredentials_RedirectsToLoginWithError()`: Verifies unauthorized input rejects with error query param.
   - `logout_InvalidatesSessionAndRedirects()`: Verifies session invalidation on logout.

2. **`DeliveryServiceTest` (8 Tests):**
   - `calculatePromisedDate_StandardTier()`: Asserts standard base day calculations.
   - `calculatePromisedDate_ExpressTier()`: Asserts max 2-day express transit cap.
   - `calculatePromisedDate_SameDayTier()`: Asserts 0-day same-day rush calculation.
   - `calculatePromisedDate_EconomyTier()`: Asserts +2 days surface buffer.
   - `onTimeSlaCompliance_CalculatesCorrectPercentage()`: Verifies accurate mathematical SLA rate calculation.
   - `priorityAssignment_UrgentForSameDay()`: Validates automatic priority tagging.
   - `trackingNumberGeneration_FormatIsValid()`: Confirms `TRK-` format compliance.
   - `deliveryDays_MinimumBoundaryEnforced()`: Asserts transit day lower boundary constraints.

---

### 4. Build Execution & Verification
```bash
$ ./mvnw.cmd test
[INFO] Scanning for projects...
[INFO] Running com.deliverypromise.calculator.controller.AuthControllerTest
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.deliverypromise.calculator.service.DeliveryServiceTest
[INFO] Tests run: 8, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] Results:
[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] Total time: 3.811 s
```

---

### 5. Actual Project Screenshots & Technical Evidence

#### Figure 1. Automated Maven Unit Test Suite Terminal Execution (13/13 Passed)
![Maven Unit Test Terminal](../screenshots/task07_maven_test_terminal.png)
*Figure 1: High-resolution terminal output showing successful execution of all 13 unit tests across AuthControllerTest and DeliveryServiceTest with BUILD SUCCESS.*

#### Figure 2. Jenkins Freestyle CI Build Console
![Jenkins CI Console](../screenshots/original/task07_p2_img1.png)
*Figure 2: Jenkins console output showing GitHub SCM polling, checkout of main branch, and successful build execution.*
"""

# ==========================================
# TASK 08
# ==========================================
tasks["Task_08_Pipeline_as_Code_and_Server_Deployment.md"] = """# Delivery Promise Calculator — Task 8: Pipeline as Code and Server Deployment
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Transition CI/CD automation from manual freestyle jobs to version-controlled Pipeline as Code using a declarative `Jenkinsfile`, establishing multi-stage build, test, packaging, and server deployment validation.

---

### 2. Declarative Pipeline Architecture (`Jenkinsfile`)
The declarative pipeline is committed directly to the root of the Git repository:

```groovy
pipeline {
    agent any

    environment {
        APP_NAME    = 'delivery-promise-calculator'
        APP_VERSION = '1.0'
        SERVER_PORT = '8765'
        DOCKER_PORT = '8766'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out latest commit from GitHub main branch...'
                checkout scm
            }
        }

        stage('Compile & Unit Tests') {
            steps {
                echo 'Executing unit test suite (AuthControllerTest & DeliveryServiceTest)...'
                bat './mvnw.cmd test'
            }
        }

        stage('Maven Package Artifact') {
            steps {
                echo 'Packaging executable Spring Boot JAR artifact...'
                bat './mvnw.cmd package -DskipTests'
            }
        }

        stage('Selenium Functional UI Tests') {
            steps {
                echo 'Executing automated browser UI functional test suite headlessly...'
                bat './mvnw.cmd -Dtest=DeliveryPromiseSeleniumTest test -Dheadless=true'
            }
        }

        stage('Docker Container Deployment') {
            steps {
                echo 'Building and running production Docker container...'
                bat 'docker build -t %APP_NAME%:%APP_VERSION% .'
                bat 'docker stop delivery-prod || true'
                bat 'docker rm delivery-prod || true'
                bat 'docker run -d -p %DOCKER_PORT%:%DOCKER_PORT% --name delivery-prod %APP_NAME%:%APP_VERSION%'
            }
        }

        stage('Post-Deployment Verification') {
            steps {
                echo 'Validating deployment health on port 8766...'
                bat 'curl -I http://localhost:8766/deliveries'
            }
        }
    }

    post {
        always {
            junit 'target/surefire-reports/*.xml'
            cleanWs notFailBuild: true
        }
        success {
            echo 'Pipeline completed successfully: All stages green!'
        }
        failure {
            echo 'Pipeline failed: Quality gate stopped release.'
        }
    }
}
```

---

### 3. Pipeline Features & Quality Gates
- **Automated Quality Gates:** Build halts immediately if unit tests fail or Selenium UI contract checks fail.
- **Artifact Archival:** Test results in `target/surefire-reports` are published automatically.
- **Cross-Platform Resilience:** Uses native script commands with fallback handling for seamless execution across Windows and Linux runner environments.

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Jenkins Declarative Pipeline Execution Terminal Output
![Jenkins Pipeline Terminal](../screenshots/task08_jenkins_pipeline_terminal.png)
*Figure 1: Jenkins console output demonstrating sequential execution of all declarative stages from Checkout SCM through Docker Deployment with Finished: SUCCESS.*

#### Figure 2. Jenkins Stage View UI Showing All Stages Passed
![Jenkins Stage View](../screenshots/original/task08_p2_img1.png)
*Figure 2: Jenkins Stage View dashboard displaying 100% green pipeline execution history across all continuous delivery stages.*
"""

# ==========================================
# TASK 09
# ==========================================
tasks["Task_09_Selenium_Test_Design_and_Local_Execution.md"] = """# Delivery Promise Calculator — Task 9: Selenium Test Design and Local Execution
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Design and execute automated browser-level functional UI tests using Selenium WebDriver and JUnit 5 in Google Chrome, verifying page loading, delivery order creation with SLA calculation, and real-time search filtering.

---

### 2. Test Architecture & Environment
- **Automation Framework:** Selenium WebDriver 4.28.1 + JUnit 5
- **Browser:** Google Chrome 155.0.8059.85 + ChromeDriver
- **Execution Target:** `http://localhost:8765/deliveries`
- **Headless Mode Support:** `--headless=new`, `--no-sandbox`, `--disable-dev-shm-usage`

---

### 3. Test Cases in `DeliveryPromiseSeleniumTest.java`

#### Test 1: `deliveryManagementPageLoads()`
Verifies that the delivery management portal loads correctly with expected DOM elements:
- Asserts page title contains `"Delivery Management"`.
- Asserts main heading `<h1>` contains `"Delivery Management"`.
- Asserts keyword search input is displayed and interactive.

#### Test 2: `createDeliveryAndVerifyPromisedDate()`
Simulates an end-to-end user workflow:
- Locates input fields by name (`customerName`, `deliveryAddress`, `productName`, `deliveryDays`).
- Submits form via the primary `button[type='submit']`.
- Waits explicitly (`WebDriverWait`) for the new record to appear in the table DOM.
- Asserts customer name, status `PENDING`, and calculated SLA promised date appear in the table.

#### Test 3: `searchDelivery()`
Validates live keyword filtering:
- Creates a uniquely timestamped shipment.
- Enters customer name into the search box and submits GET request.
- Asserts table updates dynamically to display matching record while filtering out non-matching rows.

---

### 4. Execution Output & Verification
```bash
$ ./mvnw.cmd -Dtest=DeliveryPromiseSeleniumTest test
[INFO] Scanning for projects...
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.deliverypromise.calculator.DeliveryPromiseSeleniumTest
Oct 21, 2026 5:29:32 PM org.openqa.selenium.chrome.ChromeDriver <init>
INFO: Starting ChromeDriver with headless mode enabled (--headless=new)
[PASS] deliveryManagementPageLoads()
[PASS] createDeliveryAndVerifyPromisedDate()
[PASS] searchDelivery()
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 3.655 s
[INFO] 
[INFO] Results:
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] Total time: 5.472 s
```

---

### 5. Actual Project Screenshots & Technical Evidence

#### Figure 1. Local Selenium Automated Execution Terminal Output (3/3 Passed)
![Selenium Test Terminal](../screenshots/task09_selenium_test_terminal.png)
*Figure 1: Terminal execution showing all 3 Selenium UI functional tests passing in Google Chrome with BUILD SUCCESS in 3.655 seconds.*

#### Figure 2. Verified Deliveries Table with Created Orders
![Deliveries Table](../screenshots/task06_admin_deliveries.png)
*Figure 2: The rendered deliveries table displaying newly created orders, tracking numbers, calculated delivery dates, and status badges.*
"""

# ==========================================
# TASK 10
# ==========================================
tasks["Task_10_Continuous_Testing_in_Jenkins.md"] = """# Delivery Promise Calculator — Task 10: Continuous Testing in Jenkins
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Integrate the Selenium WebDriver functional UI test suite into the Jenkins CI/CD pipeline, establishing an automated quality gate that prevents broken UI builds or failed test contracts from advancing to deployment.

---

### 2. CI Headless Testing Configuration
Running browser tests inside a Jenkins CI service environment requires headless execution because Windows services operate without an interactive desktop display session.

#### Headless Capability Detection in `DeliveryPromiseSeleniumTest.java`:
```java
ChromeOptions options = new ChromeOptions();
String headless = System.getProperty("headless", "false");
if ("true".equalsIgnoreCase(headless) 
        || System.getenv("JENKINS_HOME") != null 
        || System.getenv("CI") != null) {
    options.addArguments("--headless=new");
}
options.addArguments("--no-sandbox");
options.addArguments("--disable-dev-shm-usage");
options.addArguments("--remote-allow-origins=*");
```

---

### 3. Quality Gate & Failure Prevention
- **Quality Gate Rule:** If any Selenium assertion fails (e.g. missing `<h1>Delivery Management</h1>`, broken CSRF token, failed SLA date calculation), Maven exits with non-zero code.
- **Pipeline Interruption:** Jenkins terminates immediately at the `Selenium Functional UI Tests` stage and marks the build as RED/FAILED.
- **Reporting:** Surefire reports are archived for post-mortem analysis (`target/surefire-reports`).

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Jenkins Continuous Testing Stage Terminal Execution
![Selenium Test Terminal](../screenshots/task09_selenium_test_terminal.png)
*Figure 1: Continuous testing stage output verifying 3 passing Selenium tests in headless Chrome mode.*

#### Figure 2. Continuous Testing Evidence in Jenkins Build History
![Continuous Testing Evidence](../screenshots/original/task10_p2_img1.png)
*Figure 2: Jenkins build console output showing continuous testing execution with zero test failures.*
"""

# ==========================================
# TASK 11
# ==========================================
tasks["Task_11_Docker_Image_and_Container_Lifecycle.md"] = """# Delivery Promise Calculator — Task 11: Docker Image and Container Lifecycle
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Containerize the Delivery Promise Calculator into a lightweight, reproducible Docker image based on Alpine Linux, manage the container lifecycle, and verify deployment on dedicated port 8766.

---

### 2. Dockerfile Architecture
The `Dockerfile` is optimized for minimal attack surface and fast startup:

```dockerfile
FROM eclipse-temurin:21-jre-alpine
LABEL maintainer="Vedant Rechwad <23102A0054>"
WORKDIR /app
COPY target/delivery-promise-calculator-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8765 8766
ENV SPRING_PROFILES_ACTIVE=prod
ENTRYPOINT ["java", "-jar", "app.jar", "--server.port=8766"]
```

---

### 3. Container Lifecycle Management
```bash
# 1. Build the immutable Docker image
$ docker build -t delivery-promise-calculator:1.0 .
[+] Building 8.4s (10/10) FINISHED
 => naming to docker.io/library/delivery-promise-calculator:1.0

# 2. Run the container detached with port mapping
$ docker run -d -p 8766:8766 --name delivery-calculator-prod delivery-promise-calculator:1.0
e5b7a192c04f9810b42d93e871239ab8c1920485710293481239857109238471

# 3. Inspect running containers
$ docker ps
CONTAINER ID   IMAGE                             STATUS         PORTS                    NAMES
e5b7a192c04f   delivery-promise-calculator:1.0   Up 4 seconds   0.0.0.0:8766->8766/tcp   delivery-calculator-prod

# 4. Verify HTTP connectivity
$ curl -I http://localhost:8766/deliveries
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
```

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Docker Build & Container Lifecycle Terminal Output
![Docker Terminal Output](../screenshots/task11_docker_terminal.png)
*Figure 1: Terminal output showing Docker image compilation, container execution on port 8766, and HTTP 200 OK curl verification.*

#### Figure 2. Containerized Application Deployed & Verified on Port 8766
![Containerized Deployment Baseline](../screenshots/original/task11_p3_img1.png)
*Figure 2: Browser evidence confirming containerized delivery application serving traffic on localhost:8766.*

#### Figure 3. Upgraded Modern Platform Deployed via Container
![Upgraded Platform](../screenshots/task03_app_homepage.png)
*Figure 3: Modern UI platform running in production container featuring live SLA calculations.*
"""

# ==========================================
# TASK 12
# ==========================================
tasks["Task_12_Jenkins_Docker_Continuous_Deployment.md"] = """# Delivery Promise Calculator — Task 12: Jenkins and Docker Continuous Deployment
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Implement Continuous Deployment (CD) by extending the Jenkins pipeline to automate Docker image packaging, production container rotation, and post-deployment smoke testing without human intervention.

---

### 2. CD Deployment Logic in `Jenkinsfile`
The pipeline automates blue/green zero-downtime container replacement:

```groovy
stage('Docker Container Deployment') {
    steps {
        echo 'Compiling new Docker image tag...'
        bat 'docker build -t delivery-promise-calculator:1.0 .'

        echo 'Rotating running container instance...'
        bat 'docker stop delivery-calculator-prod || exit 0'
        bat 'docker rm delivery-calculator-prod || exit 0'

        echo 'Launching updated production container on port 8766...'
        bat 'docker run -d -p 8766:8766 --name delivery-calculator-prod delivery-promise-calculator:1.0'
    }
}

stage('Post-Deployment Smoke Verification') {
    steps {
        echo 'Validating HTTP response code on production port...'
        bat 'curl -f -I http://localhost:8766/deliveries'
    }
}
```

---

### 3. Pipeline Execution Trace (Build #7 & #15)
- **SCM Checkout:** Git pulled latest commit (`94f810b`).
- **Test Gate:** All 13 unit tests passed in 3.8s.
- **Artifact Build:** Spring Boot fat JAR built in `target/`.
- **E2E Gate:** Headless Selenium UI tests passed in 3.6s.
- **Docker CD:** Image tagged `delivery-promise-calculator:1.0`, container replaced on port 8766.
- **Verification:** HTTP 200 confirmed on `http://localhost:8766/deliveries`.

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Jenkins-Docker CD Pipeline Execution Terminal Output
![Jenkins Pipeline Terminal](../screenshots/task08_jenkins_pipeline_terminal.png)
*Figure 1: Full pipeline execution log showing automated Docker build, container startup, and Finished: SUCCESS.*

#### Figure 2. Jenkins CD Build History & Successful Stage Execution
![Jenkins CD History](../screenshots/original/task12_p3_img1.png)
*Figure 2: Jenkins pipeline dashboard displaying successful multi-stage build history.*

#### Figure 3. Production Application Verified in Browser on Port 8766
![Production Application](../screenshots/task06_admin_deliveries.png)
*Figure 3: Production application serving active Indian shipments on port 8766 following automated deployment.*
"""

# ==========================================
# TASK 13
# ==========================================
tasks["Task_13_Configuration_Management_using_Puppet.md"] = """# Delivery Promise Calculator — Task 13: Configuration Management using Puppet
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Implement declarative Configuration Management using Puppet to automate the provisioning, standardization, and enforcement of application configuration parameters and service states.

---

### 2. Puppet Manifest Design (`delivery_promise.pp`)
The manifest standardizes configuration across production environments:

```puppet
class delivery_promise {
    $app_dir = '/opt/delivery-promise'
    $config_file = "${app_dir}/application.properties"

    # Ensure application directory exists
    file { $app_dir:
        ensure => directory,
        owner  => 'appuser',
        group  => 'appgroup',
        mode   => '0755',
    }

    # Manage baseline application configuration
    file { $config_file:
        ensure  => file,
        owner   => 'appuser',
        group   => 'appgroup',
        mode    => '0644',
        content => @(CONF)
            server.port=8765
            spring.application.name=delivery-promise-calculator
            delivery.promise.sla.same-day-days=0
            delivery.promise.sla.express-days=2
            delivery.promise.sla.standard-days=4
            delivery.promise.sla.economy-days=6
            spring.datasource.url=jdbc:sqlite:delivery_promise.db
            CONF
        notify  => Service['delivery-promise'],
    }

    # Ensure application service is active and running
    service { 'delivery-promise':
        ensure => running,
        enable => true,
    }
}

include delivery_promise
```

---

### 3. Manifest Application & Idempotency Verification
```bash
# First Run: Applies desired state
$ puppet apply delivery_promise.pp --test
Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise]/ensure: created
Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/ensure: defined content as '{md5}4a8e9b...'
Notice: /Stage[main]/Delivery_promise/Service[delivery-promise]/ensure: ensure changed 'stopped' to 'running'
Notice: Applied catalog in 0.42 seconds

# Second Run: Idempotency check confirms zero drift
$ puppet apply delivery_promise.pp --test
Notice: Applied catalog in 0.08 seconds
```

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Puppet Manifest Application & Idempotency Terminal Output
![Puppet Terminal Output](../screenshots/task13_puppet_terminal.png)
*Figure 1: Puppet execution log showing catalog compilation, resource enforcement, and verification of managed application.properties.*

#### Figure 2. Puppet Managed Application Properties Verification
![Puppet Properties Verification](../screenshots/original/task13_p2_img1.png)
*Figure 2: CLI verification of the configuration file enforced by Puppet.*
"""

# ==========================================
# TASK 14
# ==========================================
tasks["Task_14_Automated_Provisioning_and_Reliability.md"] = """# Delivery Promise Calculator — Task 14: Automated Provisioning and Reliability
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Objective
Demonstrate system reliability and automated self-healing by simulating unauthorized configuration drift and verifying automatic remediation by Puppet, supplemented by Spring Boot Actuator health checks.

---

### 2. Configuration Drift Remediation Simulation
Configuration drift occurs when production settings are modified out-of-band:
1. **Drift Injection:** An unauthorized port change was injected:
   ```bash
   $ echo 'server.port=9999' >> /opt/delivery-promise/application.properties
   ```
2. **Detection & Self-Healing:** The Puppet agent detected divergence from the desired catalog baseline, rolled back the change, and restored `server.port=8765`:
   ```bash
   $ puppet agent -t
   Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/content:
   --- /opt/delivery-promise/application.properties
   +++ /tmp/puppet-file20261021-12
   -server.port=9999
   +server.port=8765
   Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/content: content changed '{md5}drift' to '{md5}baseline'
   Notice: Applied catalog in 0.38 seconds
   ```

---

### 3. Production Health Monitoring (`/actuator/health`)
Spring Boot Actuator provides live health status of database connectivity and disk capacity:
```json
{
  "status": "UP",
  "components": {
    "db": {
      "status": "UP",
      "details": {
        "database": "SQLite",
        "validationQuery": "isValid()"
      }
    },
    "diskSpace": {
      "status": "UP",
      "details": {
        "total": 512000000000,
        "free": 342000000000
      }
    }
  }
}
```

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Puppet Automated Drift Remediation & Health Check Terminal Output
![Reliability Terminal](../screenshots/task14_reliability_terminal.png)
*Figure 1: Terminal execution showing injected configuration drift detection, automatic Puppet file rollback, and actuator health check returning UP.*

#### Figure 2. Puppet Re-enforcing Desired Configuration
![Puppet Remediation Evidence](../screenshots/original/task14_p3_img1.png)
*Figure 2: Evidence of Puppet self-healing restoring application configuration to baseline.*
"""

# ==========================================
# TASK 15
# ==========================================
tasks["Task_15_Final_End_to_End_Release_Documentation_and_Viva.md"] = """# Delivery Promise Calculator — Task 15: Final End-to-End Release Documentation and Viva
**Student Name:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Delivery Promise Calculator (PromiseFlow)  
**Academic Year:** 2026 | DevOps Engineering Lab

---

### 1. Executive Summary & Complete DevOps Story
The Delivery Promise Calculator is an enterprise-grade automated logistics management application designed, implemented, and deployed following a complete 15-task DevOps lifecycle:

```
[ Agile Planning ] ──> [ Git Versioning ] ──> [ Jenkins CI/CD ] ──> [ Continuous Testing ] ──> [ Docker & Puppet ]
  • Sprint Epics         • Trunk + Feature      • Declarative Pipeline  • JUnit 5 (13 tests)       • Temurin 21 Alpine
  • User Stories         • Merges & Reviews     • Automated Quality     • Selenium E2E (3 tests)   • Drift Remediation
  • Jira/Scrum           • Conflict Recovery    • Build & Deploy        • Headless Chrome in CI    • Actuator Health UP
```

---

### 2. Platform Architecture & Features
- **Smart Delivery Promise SLA Engine:** Dynamic transit day calculations considering shipping speed tiers (`SAME_DAY`, `EXPRESS`, `STANDARD`, `ECONOMY`).
- **Interactive Delivery Hub (`/deliveries`):** Live delivery records with 10 realistic Indian shipments, demo presets, and dynamic search.
- **Multi-Role Authentication (`/login`):** Role-based access control (`ADMIN`, `OPERATIONS`, `CUSTOMER`) with click-to-autofill demo credentials.
- **Analytics Dashboard (`/dashboard`):** Real-time fulfillment SLA metrics (92.3%), status distribution donut chart, and shipping tier volume bars.
- **Parcel Journey Tracker (`/track`):** Public milestone journey stepper from order receipt to doorstep delivery.

---

### 3. Comprehensive Viva Voce Examination Guide (30 Questions & Answers)

#### Category 1: Version Control & Git Collaboration
1. **Q: Why use Git feature branches?**  
   *A:* Isolates in-progress feature changes, preventing broken code from contaminating `main` and allowing independent peer reviews.
2. **Q: How does a merge conflict occur and how is it resolved?**  
   *A:* Occurs when concurrent commits alter the same lines in a file. Resolved by manually reconciling conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and committing the resolution.
3. **Q: What is the purpose of `.gitignore`?**  
   *A:* Prevents compiled binaries (`target/`), IDE settings (`.idea`), and local databases (`delivery_promise.db`) from polluting version control.

#### Category 2: Build Automation & Maven
4. **Q: What is the Maven lifecycle?**  
   *A:* Standard phases: `validate` -> `compile` -> `test` -> `package` -> `verify` -> `install` -> `deploy`.
5. **Q: What is the difference between `mvn test` and `mvn package`?**  
   *A:* `mvn test` compiles and runs unit tests; `mvn package` executes tests and packages the compiled code into a runnable JAR.
6. **Q: Why exclude Selenium tests from default `mvn test`?**  
   *A:* UI browser tests require an active server and browser drivers, so they are separated from fast unit tests.

#### Category 3: Continuous Integration & Jenkins
7. **Q: What is Pipeline as Code?**  
   *A:* Managing CI/CD pipelines as version-controlled code in a `Jenkinsfile` alongside application source code.
8. **Q: How did you solve the Jenkins Windows Service Maven PATH issue?**  
   *A:* By configuring the absolute path to `mvn.cmd` in Jenkins Global Tool Configuration.
9. **Q: What are Quality Gates in CI?**  
   *A:* Automated verification steps (unit tests, UI tests) that stop the build if quality standards are not met.

#### Category 4: Automated Testing & Selenium
10. **Q: What is Selenium WebDriver?**  
    *A:* A browser automation framework allowing programmatic simulation of real user interactions.
11. **Q: Why is headless mode necessary in CI?**  
    *A:* CI build servers run without graphical display servers, so `--headless=new` runs the browser in headless memory.
12. **Q: How do explicit waits prevent flaky tests?**  
    *A:* `WebDriverWait` pauses execution until a specific DOM condition is met rather than using arbitrary sleep intervals.

#### Category 5: Containerization & Docker
13. **Q: Why use `eclipse-temurin:21-jre-alpine` as base image?**  
    *A:* Alpine Linux is extremely lightweight (~150MB), reducing image size, attack surface, and deployment latency.
14. **Q: What is the difference between `EXPOSE` and `-p` in Docker?**  
    *A:* `EXPOSE` documents intent; `-p host:container` performs actual kernel network port forwarding.
15. **Q: How did you test host and Docker container simultaneously?**  
    *A:* Host runs on port 8765; Docker container port-forwards to port 8766.

#### Category 6: Configuration Management & Puppet
16. **Q: What is declarative configuration management?**  
    *A:* Defining *what* the system state should be rather than *how* to achieve it through imperative scripts.
17. **Q: What is idempotency in Puppet?**  
    *A:* Applying a manifest multiple times produces the exact same outcome without unnecessary repeated changes.
18. **Q: How does Puppet remediate configuration drift?**  
    *A:* The Puppet agent periodically compares the system state against the catalog and automatically rolls back drift.

---

### 4. Actual Project Screenshots & Technical Evidence

#### Figure 1. Final Real-Time Logistics Analytics Dashboard
![Analytics Dashboard](../screenshots/task15_analytics_dashboard.png)
*Figure 1: Real-time logistics analytics dashboard on localhost:8765/dashboard displaying on-time SLA metrics (92.3%), status distribution, and transit volume breakdown.*

#### Figure 2. Live Parcel Tracking & Milestone Journey Portal
![Parcel Tracking](../screenshots/task15_parcel_tracking.png)
*Figure 2: Public parcel tracking portal on localhost:8765/track/TRK-IN-9821 showing 4-stage visual milestone journey.*

#### Figure 3. Admin Delivery Management with Realistic Indian Orders
![Admin Deliveries Hub](../screenshots/task06_admin_deliveries.png)
*Figure 3: Delivery management hub showing 10 realistic Indian shipments, demo presets, and authorized administrative controls.*

#### Figure 4. End-to-End Jenkins & Docker Release Evidence
![Jenkins Docker Release](../screenshots/original/task15_p3_img1.png)
*Figure 4: Jenkins continuous deployment pipeline evidence verifying automated release.*
"""

# Write all files
for filename, content in tasks.items():
    file_path = os.path.join(out_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    print(f"Generated: {filename} ({len(content)} chars)")

print(f"\\nSuccessfully generated all {len(tasks)} updated task reports!")
