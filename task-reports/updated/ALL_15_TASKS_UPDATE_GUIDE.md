# Delivery Promise Calculator (PromiseFlow)
## Comprehensive 15-Task Coherence & PDF Generation Guide

**Author:** Vedant Rechwad  
**Roll No.:** 23102A0054  
**Project:** Enterprise Delivery Promise Calculator & DevOps Release Platform  
**Technology Stack:** Java 21, Spring Boot 4, SQLite, Maven, Jenkins, Docker, Selenium WebDriver, Puppet  

---

### Executive Summary of Upgrades

The Delivery Promise Calculator has evolved into a production-grade automated logistics platform (**"PromiseFlow"**). All 15 task reports have been updated with complete architectural coherence, exact student metadata, technical code listings, realistic Indian shipment data, and embedded technical screenshots and terminal outputs.

```
+-----------------------------------------------------------------------------------+
|                            NEW ARCHITECTURE HIGHLIGHTS                            |
+-----------------------------------------------------------------------------------+
| 1. Authentication & Security : Dedicated /login, role credentials, click-autofill |
| 2. Smart SLA Promise Engine : Dynamic date math by Shipping Tier (Same-Day,      |
|                               Express, Standard, Eco) & auto tracking IDs.       |
| 3. Customer Tracking Portal : Live /track with 4-stage visual journey stepper.   |
| 4. Executive Analytics      : /dashboard with status donut & tier volume charts.  |
| 5. Automated Testing        : 13 Unit/Integration tests + Selenium headless suite.|
| 6. Realistic Demo Data      : 10 Indian orders with autocomplete & demo presets.  |
| 7. Resilient CI/CD Pipeline : Cross-environment Jenkinsfile & Docker container.   |
| 8. Configuration Management : Puppet manifest with automated drift self-healing.  |
+-----------------------------------------------------------------------------------+
```

---

### Screenshot and Evidence Asset Directory (`task-reports/screenshots/`)

All reports reference high-resolution visual evidence stored in `task-reports/screenshots/`:

| File | Type | Description | Used in Tasks |
| :--- | :--- | :--- | :--- |
| `task03_app_homepage.png` | UI Screenshot | Running platform on `localhost:8765`, metrics ticker, SLA simulator | Task 1, Task 3, Task 11 |
| `task06_admin_deliveries.png` | UI Screenshot | Deliveries hub with 10 Indian orders, demo presets, status dropdowns | Task 2, Task 5, Task 6, Task 9, Task 12, Task 15 |
| `task06_login_page.png` | UI Screenshot | Account Sign In portal with persona tabs and click-to-autofill | Task 6 |
| `task15_analytics_dashboard.png` | UI Screenshot | Logistics dashboard with SLA compliance, status donut, tier bars | Task 15 |
| `task15_parcel_tracking.png` | UI Screenshot | Customer tracking portal with 4-stage milestone stepper | Task 15 |
| `task04_git_history_terminal.png` | Terminal | Git commit tree, feature branches, and working tree status | Task 4 |
| `task07_maven_test_terminal.png` | Terminal | Automated unit tests (13/13 passed, BUILD SUCCESS) | Task 7 |
| `task08_jenkins_pipeline_terminal.png` | Terminal | Jenkins Declarative Pipeline stage execution (Finished: SUCCESS) | Task 8, Task 12 |
| `task09_selenium_test_terminal.png` | Terminal | Selenium automated UI suite (3/3 passed in Chrome) | Task 9, Task 10 |
| `task11_docker_terminal.png` | Terminal | Docker build, image creation, container run on port 8766 | Task 11 |
| `task13_puppet_terminal.png` | Terminal | Puppet manifest catalog compilation and resource enforcement | Task 13 |
| `task14_reliability_terminal.png` | Terminal | Injected drift detection, self-healing rollback, health check UP | Task 14 |
| `original/*.png` | Original Figures | Original 26 figures extracted from baseline college task PDFs | Tasks 1 to 15 |

---

### How to Generate Final PDFs with Another LLM or Tool

You can feed the `task-reports/` folder directly to another LLM (e.g. Claude, ChatGPT, or pandoc) with this prompt:

> *"Please convert each of the 15 Markdown task report files in `task-reports/updated/` into beautifully formatted college academic lab report PDFs for student **Vedant Rechwad** (Roll No: **23102A0054**). Embed the referenced screenshots from `task-reports/screenshots/` and preserve all technical tables, terminal output blocks, and the 30-question Viva Voce preparation section."*

---

### Task-by-Task Coherence Matrix

| Task # | Task Title | Enhanced Scope in Updated Report | Primary Evidence File |
|---|---|---|---|
| **01** | Problem Definition and Scope | Smart SLA tiered routing, self-service tracking, RBAC security | `task03_app_homepage.png` |
| **02** | Agile Planning & DevOps Workflow | 4 Agile sprints, user stories, acceptance criteria, DevOps toolchain | `task06_admin_deliveries.png` |
| **03** | Requirements & Technology Setup | Java 21, Spring Boot 4, SQLite schema, startup database seeder | `task03_app_homepage.png` |
| **04** | Git & GitHub Repo Initialization | GitFlow branching, remote setup, commit tree | `task04_git_history_terminal.png` |
| **05** | Feature Development with Branching | Validation constraints, SLA calculations, GitHub pull request | `task06_admin_deliveries.png` |
| **06** | MVP Completion & Git Collaboration | Multi-role auth, click-to-autofill, merge conflict resolution | `task06_login_page.png` |
| **07** | Jenkins Installation & CI Job | Freestyle CI job, 13 automated unit tests (AuthController, Service) | `task07_maven_test_terminal.png` |
| **08** | Pipeline as Code & Deployment | Declarative 6-stage `Jenkinsfile` with automated quality gates | `task08_jenkins_pipeline_terminal.png` |
| **09** | Selenium Test Design & Execution | 3 automated UI tests in Chrome with headless CI support | `task09_selenium_test_terminal.png` |
| **10** | Continuous Testing in Jenkins | Automating Selenium tests in Jenkins pipeline as quality gate | `task09_selenium_test_terminal.png` |
| **11** | Docker Image & Container Lifecycle | Temurin 21 JRE Alpine image, port 8766 container execution | `task11_docker_terminal.png` |
| **12** | Jenkins Docker Continuous Deployment | Automated container rotation, zero-downtime CD pipeline | `task08_jenkins_pipeline_terminal.png` |
| **13** | Configuration Management (Puppet) | Declarative manifest `delivery_promise.pp`, idempotency proof | `task13_puppet_terminal.png` |
| **14** | Automated Provisioning & Reliability | Injected drift detection, self-healing rollback, health actuator | `task14_reliability_terminal.png` |
| **15** | Final Release Documentation & Viva | Full architecture, live tracking, analytics, 30 Viva questions | `task15_analytics_dashboard.png` |
