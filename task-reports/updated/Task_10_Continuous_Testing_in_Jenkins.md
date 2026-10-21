# Delivery Promise Calculator — Task 10: Continuous Testing in Jenkins
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
*Figure 2: Jenkins build console output showing continuous testing execution with zero test failures.*\n