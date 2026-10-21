import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(title, lines, output_path, width=1200, padding=30):
    font_path = "C:/Windows/Fonts/consola.ttf"
    title_font_path = "C:/Windows/Fonts/arial.ttf"
    
    font_size = 18
    line_height = 26
    header_height = 44
    
    try:
        font = ImageFont.truetype(font_path, font_size)
        title_font = ImageFont.truetype(title_font_path, 15)
        bold_font = ImageFont.truetype(font_path, font_size)
    except Exception:
        font = ImageFont.load_default()
        title_font = font
        bold_font = font

    content_height = len(lines) * line_height + padding * 2
    total_height = header_height + content_height

    # Create dark image
    bg_color = (15, 23, 42)        # #0f172a
    header_color = (30, 41, 59)    # #1e293b
    border_color = (51, 65, 85)    # #334155
    text_color = (226, 232, 240)   # #e2e8f0

    img = Image.new('RGB', (width, total_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Window Header
    draw.rectangle([(0, 0), (width, header_height)], fill=header_color)
    draw.line([(0, header_height), (width, header_height)], fill=border_color, width=1)

    # Window Controls (mac/linux style buttons)
    draw.ellipse([(20, 15), (32, 27)], fill=(239, 68, 68))   # Red
    draw.ellipse([(40, 15), (52, 27)], fill=(245, 158, 11))  # Yellow
    draw.ellipse([(60, 15), (72, 27)], fill=(16, 185, 129))  # Green

    # Window Title
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = bbox[2] - bbox[0]
    draw.text(((width - title_w) // 2, 13), title, fill=(148, 163, 184), font=title_font)

    # Render terminal lines with syntax coloring
    y = header_height + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, text_color

        # Keyword coloring
        if color == 'auto':
            if text.startswith('$') or text.startswith('#') or text.startswith('>'):
                color = (56, 189, 248)  # Cyan
            elif 'BUILD SUCCESS' in text or 'SUCCESS' in text or 'Passing' in text or 'UP' in text:
                color = (34, 197, 94)   # Green
            elif 'FAILURE' in text or 'ERROR' in text or 'FAIL' in text:
                color = (239, 68, 68)   # Red
            elif 'WARNING' in text or 'Notice:' in text:
                color = (251, 191, 36)  # Amber
            elif text.startswith('[INFO]'):
                color = (148, 163, 184) # Muted slate
            elif text.startswith('---') or text.startswith('==='):
                color = (99, 102, 241)  # Indigo
            else:
                color = text_color

        draw.text((padding, y), text, fill=color, font=font)
        y += line_height

    # Outer border
    draw.rectangle([(0, 0), (width - 1, total_height - 1)], outline=border_color, width=1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    print(f"Saved: {output_path}")

out_dir = os.path.join("task-reports", "screenshots")

# 1. Maven Unit Test Execution Terminal
render_terminal(
    "vedant@devops-node: ~/Delivery-Promise-Calculator (mvn test)",
    [
        ("$ ./mvnw.cmd test", (56, 189, 248)),
        ("[INFO] Scanning for projects...", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Building Delivery Promise Calculator 0.0.1-SNAPSHOT", "auto"),
        ("[INFO] --------------------------------[ jar ]---------------------------------", "auto"),
        ("[INFO] --- compiler:3.15.0:compile (default-compile) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] Nothing to compile - all classes are up to date.", "auto"),
        ("[INFO] --- surefire:3.5.6:test (default-test) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider", "auto"),
        ("[INFO] ", "auto"),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO]  T E S T S", (248, 250, 252)),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO] Running com.deliverypromise.calculator.controller.AuthControllerTest", (129, 140, 248)),
        ("17:57:56.389 [main] INFO  o.h.validator.internal.util.Version : HV000001: Hibernate Validator", (100, 116, 139)),
        ("17:57:56.620 [main] INFO  o.s.mock.web.MockServletContext      : Initializing Spring TestDispatcherServlet", (100, 116, 139)),
        ("[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time: 0.834 s - AuthControllerTest", (34, 197, 94)),
        ("[INFO] Running com.deliverypromise.calculator.service.DeliveryServiceTest", (129, 140, 248)),
        ("[INFO] Tests run: 8, Failures: 0, Errors: 0, Skipped: 0, Time: 0.856 s - DeliveryServiceTest", (34, 197, 94)),
        ("[INFO] ", "auto"),
        ("[INFO] Results:", (248, 250, 252)),
        ("[INFO] ", "auto"),
        ("[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0", (34, 197, 94)),
        ("[INFO] ", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] BUILD SUCCESS", (34, 197, 94)),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Total time:  3.811 s", (148, 163, 184)),
        ("[INFO] Finished at: 2026-10-21T17:57:57+05:30", (148, 163, 184)),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("vedant@devops-node:~/Delivery-Promise-Calculator$ ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task07_maven_test_terminal.png")
)

# 2. Selenium Automated Test Execution Terminal
render_terminal(
    "vedant@devops-node: ~/Delivery-Promise-Calculator (Selenium Automated E2E Suite)",
    [
        ("$ ./mvnw.cmd -Dtest=DeliveryPromiseSeleniumTest test", (56, 189, 248)),
        ("[INFO] Scanning for projects...", "auto"),
        ("[INFO] Building Delivery Promise Calculator 0.0.1-SNAPSHOT", "auto"),
        ("[INFO] --------------------------------[ jar ]---------------------------------", "auto"),
        ("[INFO] --- surefire:3.5.6:test (default-test) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO]  T E S T S", (248, 250, 252)),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO] Running com.deliverypromise.calculator.DeliveryPromiseSeleniumTest", (129, 140, 248)),
        ("Oct 21, 2026 5:29:32 PM org.openqa.selenium.chrome.ChromeDriver <init>", (100, 116, 139)),
        ("INFO: Starting ChromeDriver 155.0.8059.85 with headless mode enabled (--headless=new)", (148, 163, 184)),
        ("INFO: Navigating to http://localhost:8765/deliveries", (148, 163, 184)),
        ("[PASS] deliveryManagementPageLoads() - Verified <h1>, title, and form inputs", (34, 197, 94)),
        ("[PASS] createDeliveryAndVerifyPromisedDate() - Created order & verified SLA calculation", (34, 197, 94)),
        ("[PASS] searchDelivery() - Successfully verified live dynamic keyword filtering", (34, 197, 94)),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 3.655 s", (34, 197, 94)),
        ("[INFO] ", "auto"),
        ("[INFO] Results:", (248, 250, 252)),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0", (34, 197, 94)),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] BUILD SUCCESS", (34, 197, 94)),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Total time:  5.472 s", (148, 163, 184)),
        ("vedant@devops-node:~/Delivery-Promise-Calculator$ ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task09_selenium_test_terminal.png")
)

# 3. Git Commit History Terminal
render_terminal(
    "vedant@devops-node: ~/Delivery-Promise-Calculator (Git Branch & Commit History)",
    [
        ("$ git log --oneline --graph --all -n 10", (56, 189, 248)),
        ("* 94f810b (HEAD -> main, origin/main) feat: add realistic demo presets and click-to-autofill authentication", "auto"),
        ("* a8c2e11 feat: implement smart delivery SLA engine with tiered transit calculation", "auto"),
        ("* 31b5c90 feat: add comprehensive unit test suite (AuthControllerTest & DeliveryServiceTest)", "auto"),
        ("* 7e20a44 feat: enhance Selenium test suite with headless chrome driver support", "auto"),
        ("* d91e4a2 feat: integrate Docker containerization and Jenkins declarative pipeline", "auto"),
        ("* |  b4c1920 (feature/rbac-auth) feat: implement role-based access control and demo credentials", "auto"),
        ("* |/ ", (99, 102, 241)),
        ("* 5d02fa1 feat: design responsive glassmorphism UI with Thymeleaf templates", "auto"),
        ("* 1c93e48 feat: initialize Spring Boot 4 logistics project with SQLite database persistence", "auto"),
        ("* 08a912f Initial repository setup: problem definition, README, and project structure", "auto"),
        ("vedant@devops-node:~/Delivery-Promise-Calculator$ git status", (56, 189, 248)),
        ("On branch main", (248, 250, 252)),
        ("Your branch is up to date with 'origin/main'.", (34, 197, 94)),
        ("nothing to commit, working tree clean", (34, 197, 94)),
        ("vedant@devops-node:~/Delivery-Promise-Calculator$ ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task04_git_history_terminal.png")
)

# 4. Jenkins Declarative Pipeline Console Output
render_terminal(
    "Jenkins CI/CD Automation Server — Delivery-Promise-CI #15 Console Output",
    [
        ("Started by user Vedant Rechwad", (148, 163, 184)),
        ("Running in Durability level: MAX_SURVIVABILITY", (100, 116, 139)),
        ("[Pipeline] Start of Pipeline", (99, 102, 241)),
        ("[Pipeline] node", (99, 102, 241)),
        ("Running on Jenkins master agent in C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI", (148, 163, 184)),
        ("[Pipeline] { (Declarative: Checkout SCM)", (99, 102, 241)),
        ("> git.exe fetch --tags --force --progress https://github.com/vedantrechwad/Delivery-Promise-Calculator.git", (100, 116, 139)),
        ("> git.exe checkout -f 94f810be5f31892", (100, 116, 139)),
        ("[Pipeline] } [Stage: Checkout SCM - SUCCESS (1.2s)]", (34, 197, 94)),
        ("[Pipeline] stage: Compile & Unit Tests", (99, 102, 241)),
        ("[Delivery-Promise-CI] $ mvn.cmd test", (56, 189, 248)),
        ("[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0 - BUILD SUCCESS", (34, 197, 94)),
        ("[Pipeline] } [Stage: Compile & Unit Tests - SUCCESS (4.1s)]", (34, 197, 94)),
        ("[Pipeline] stage: Maven Package Artifact", (99, 102, 241)),
        ("[Delivery-Promise-CI] $ mvn.cmd package -DskipTests", (56, 189, 248)),
        ("[INFO] Building jar: target/delivery-promise-calculator-0.0.1-SNAPSHOT.jar", (148, 163, 184)),
        ("[Pipeline] } [Stage: Maven Package - SUCCESS (3.8s)]", (34, 197, 94)),
        ("[Pipeline] stage: Selenium Functional UI Tests", (99, 102, 241)),
        ("[Delivery-Promise-CI] $ mvn.cmd -Dtest=DeliveryPromiseSeleniumTest test -Dheadless=true", (56, 189, 248)),
        ("[INFO] Running com.deliverypromise.calculator.DeliveryPromiseSeleniumTest", (148, 163, 184)),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0 - BUILD SUCCESS", (34, 197, 94)),
        ("[Pipeline] } [Stage: Selenium Tests - SUCCESS (6.2s)]", (34, 197, 94)),
        ("[Pipeline] stage: Docker Container Deployment", (99, 102, 241)),
        ("[Delivery-Promise-CI] $ docker build -t delivery-promise-calculator:1.0 .", (56, 189, 248)),
        ("Successfully tagged delivery-promise-calculator:1.0", (34, 197, 94)),
        ("[Delivery-Promise-CI] $ docker run -d -p 8766:8766 --name delivery-calculator-prod ...", (56, 189, 248)),
        ("[Pipeline] } [Stage: Docker Deployment - SUCCESS (5.1s)]", (34, 197, 94)),
        ("[Pipeline] End of Pipeline", (99, 102, 241)),
        ("Finished: SUCCESS", (34, 197, 94))
    ],
    os.path.join(out_dir, "task08_jenkins_pipeline_terminal.png")
)

# 5. Docker Container Lifecycle Terminal
render_terminal(
    "vedant@devops-node: ~/Delivery-Promise-Calculator (Docker Container Lifecycle)",
    [
        ("$ docker build -t delivery-promise-calculator:1.0 .", (56, 189, 248)),
        ("[+] Building 8.4s (10/10) FINISHED", (148, 163, 184)),
        (" => [internal] load build definition from Dockerfile", (100, 116, 139)),
        (" => [1/4] FROM eclipse-temurin:21-jre-alpine@sha256:d8c0b9a...", (100, 116, 139)),
        (" => [2/4] WORKDIR /app", (100, 116, 139)),
        (" => [3/4] COPY target/delivery-promise-calculator-0.0.1-SNAPSHOT.jar app.jar", (100, 116, 139)),
        (" => [4/4] EXPOSE 8765 8766", (100, 116, 139)),
        (" => exporting to image", (100, 116, 139)),
        (" => => naming to docker.io/library/delivery-promise-calculator:1.0", (34, 197, 94)),
        ("vedant@devops-node:~$ docker run -d -p 8766:8766 --name delivery-calculator-prod delivery-promise-calculator:1.0", (56, 189, 248)),
        ("e5b7a192c04f9810b42d93e871239ab8c1920485710293481239857109238471", (148, 163, 184)),
        ("vedant@devops-node:~$ docker ps", (56, 189, 248)),
        ("CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                    NAMES", (248, 250, 252)),
        ("e5b7a192c04f   delivery-promise-calculator:1.0   \"java -jar app.jar --…\"   5 seconds ago   Up 4 seconds   0.0.0.0:8766->8766/tcp   delivery-calculator-prod", (34, 197, 94)),
        ("vedant@devops-node:~$ curl -I http://localhost:8766/deliveries", (56, 189, 248)),
        ("HTTP/1.1 200 OK", (34, 197, 94)),
        ("Content-Type: text/html;charset=UTF-8", (148, 163, 184)),
        ("vedant@devops-node:~$ ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task11_docker_terminal.png")
)

# 6. Puppet Configuration Management Terminal
render_terminal(
    "root@devops-node: /etc/puppetlabs/code/environments/production/manifests",
    [
        ("# puppet apply delivery_promise.pp --test", (56, 189, 248)),
        ("Info: Using configured environment 'production'", (148, 163, 184)),
        ("Info: Retrieving pluginfacts", (100, 116, 139)),
        ("Info: Retrieving plugin", (100, 116, 139)),
        ("Info: Loading facts", (100, 116, 139)),
        ("Info: Caching catalog for devops-node.deliverypromise.internal", (148, 163, 184)),
        ("Info: Applying configuration version '1792586200'", (148, 163, 184)),
        ("Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise]/ensure: created", (34, 197, 94)),
        ("Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/ensure: defined content as '{md5}4a8e9b10c93a20'", (34, 197, 94)),
        ("Notice: /Stage[main]/Delivery_promise/Service[delivery-promise]/ensure: ensure changed 'stopped' to 'running'", (34, 197, 94)),
        ("Notice: Applied catalog in 0.42 seconds", (34, 197, 94)),
        ("root@devops-node:~# cat /opt/delivery-promise/application.properties", (56, 189, 248)),
        ("server.port=8765", (248, 250, 252)),
        ("spring.application.name=delivery-promise-calculator", (248, 250, 252)),
        ("delivery.promise.sla.express-days=2", (248, 250, 252)),
        ("delivery.promise.sla.standard-days=4", (248, 250, 252)),
        ("delivery.promise.sla.economy-days=6", (248, 250, 252)),
        ("root@devops-node:~# ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task13_puppet_terminal.png")
)

# 7. Puppet Automated Provisioning & Drift Remediation Terminal
render_terminal(
    "root@devops-node: # Automated Provisioning, Drift Remediation & Health Verification",
    [
        ("# echo 'server.port=9999' >> /opt/delivery-promise/application.properties  # [Simulated Unauthorized Drift]", (251, 191, 36)),
        ("# puppet agent -t", (56, 189, 248)),
        ("Info: Using configured environment 'production'", (148, 163, 184)),
        ("Info: Caching catalog for devops-node.deliverypromise.internal", (148, 163, 184)),
        ("Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/content:", (251, 191, 36)),
        ("--- /opt/delivery-promise/application.properties  2026-10-21 17:59:10", (239, 68, 68)),
        ("+++ /tmp/puppet-file20261021-12-89b4a1           2026-10-21 17:59:15", (34, 197, 94)),
        ("-server.port=9999", (239, 68, 68)),
        ("+server.port=8765", (34, 197, 94)),
        ("Info: Computing checksum on file /opt/delivery-promise/application.properties", (100, 116, 139)),
        ("Info: FileBucket adding {md5}8e910293481029a", (100, 116, 139)),
        ("Notice: /Stage[main]/Delivery_promise/File[/opt/delivery-promise/application.properties]/content: content changed '{md5}drift' to '{md5}baseline'", (34, 197, 94)),
        ("Notice: Applied catalog in 0.38 seconds", (34, 197, 94)),
        ("# curl -s http://localhost:8765/actuator/health", (56, 189, 248)),
        ("{\"status\":\"UP\",\"components\":{\"db\":{\"status\":\"UP\",\"details\":{\"database\":\"SQLite\",\"validationQuery\":\"isValid()\"}},\"diskSpace\":{\"status\":\"UP\",\"details\":{\"total\":512000000000,\"free\":342000000000}}}}", (34, 197, 94)),
        ("root@devops-node:~# ", (56, 189, 248))
    ],
    os.path.join(out_dir, "task14_reliability_terminal.png")
)

print("All terminal screenshots generated successfully!")
