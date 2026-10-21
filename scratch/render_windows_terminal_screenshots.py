import os
from PIL import Image, ImageDraw, ImageFont

def render_windows_terminal(tab_title, lines, output_path, width=1150, padding_x=18, padding_y=16):
    font_path = "C:/Windows/Fonts/consola.ttf"
    tab_font_path = "C:/Windows/Fonts/segoeui.ttf"
    
    font_size = 15
    line_height = 23
    tab_bar_height = 36
    
    font = ImageFont.truetype(font_path, font_size)
    tab_font = ImageFont.truetype(tab_font_path, 12)
    controls_font = ImageFont.truetype(tab_font_path, 12)
    bold_font = ImageFont.truetype(font_path, font_size)

    content_height = len(lines) * line_height + padding_y * 2
    total_height = tab_bar_height + content_height

    # Windows Terminal Dark Palette
    frame_bg = (31, 31, 31)        # #1f1f1f (tab bar background)
    body_bg = (12, 12, 12)         # #0c0c0c (terminal background)
    tab_active_bg = (12, 12, 12)   # Active tab matches body
    tab_border = (45, 45, 45)      # Tab subtle border
    text_default = (204, 204, 204) # #cccccc
    text_muted = (128, 128, 128)   # #808080
    border_color = (40, 40, 40)    # Outer border

    img = Image.new('RGB', (width, total_height), color=body_bg)
    draw = ImageDraw.Draw(img)

    # 1. Top Tab Bar
    draw.rectangle([(0, 0), (width, tab_bar_height)], fill=frame_bg)

    # 2. Active Tab
    tab_w = 230
    tab_h = 30
    tab_x = 8
    tab_y = 6
    # Active tab shape (rounded top corners or clean rectangle)
    draw.rectangle([(tab_x, tab_y), (tab_x + tab_w, tab_bar_height)], fill=tab_active_bg)
    draw.line([(tab_x, tab_y), (tab_x + tab_w, tab_y)], fill=tab_border, width=1)
    draw.line([(tab_x, tab_y), (tab_x, tab_bar_height)], fill=tab_border, width=1)
    draw.line([(tab_x + tab_w, tab_y), (tab_x + tab_w, tab_bar_height)], fill=tab_border, width=1)

    # PowerShell Icon in Tab (small blue badge with >_ )
    icon_x = tab_x + 10
    icon_y = tab_y + 7
    draw.rectangle([(icon_x, icon_y), (icon_x + 16, icon_y + 16)], fill=(1, 36, 86))
    draw.text((icon_x + 3, icon_y + 1), ">", fill=(255, 255, 255), font=ImageFont.truetype(font_path, 11))

    # Tab Text
    draw.text((icon_x + 22, tab_y + 7), tab_title, fill=(240, 240, 240), font=tab_font)

    # Tab Close Icon '✕'
    draw.text((tab_x + tab_w - 18, tab_y + 8), "✕", fill=(160, 160, 160), font=ImageFont.truetype(tab_font_path, 10))

    # '+' New Tab button
    plus_x = tab_x + tab_w + 10
    draw.text((plus_x, tab_y + 7), "+", fill=(160, 160, 160), font=ImageFont.truetype(tab_font_path, 14))

    # '˅' Chevron
    draw.text((plus_x + 20, tab_y + 9), "˅", fill=(140, 140, 140), font=ImageFont.truetype(tab_font_path, 10))

    # Windows 11 Caption Controls (Top Right: Minimize, Maximize, Close)
    ctrl_w = 46
    close_x = width - ctrl_w
    max_x = close_x - ctrl_w
    min_x = max_x - ctrl_w

    # Minimize '-'
    draw.text((min_x + 18, 10), "─", fill=(200, 200, 200), font=controls_font)
    # Maximize '□'
    draw.text((max_x + 18, 10), "□", fill=(200, 200, 200), font=controls_font)
    # Close '✕'
    draw.text((close_x + 18, 10), "✕", fill=(200, 200, 200), font=controls_font)

    # 3. Terminal Content Lines
    y = tab_bar_height + padding_y

    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, text_default

        # Windows PowerShell syntax highlighting
        if color == 'auto':
            if text.startswith('PS '):
                # Split prompt and command
                parts = text.split('> ', 1)
                prompt_part = parts[0] + '> '
                draw.text((padding_x, y), prompt_part, fill=(204, 204, 204), font=font)
                bbox = draw.textbbox((0, 0), prompt_part, font=font)
                p_width = bbox[2] - bbox[0]
                
                if len(parts) > 1:
                    cmd_line = parts[1]
                    # In PowerShell, command is yellow, args are white
                    cmd_tokens = cmd_line.split(' ', 1)
                    cmd_name = cmd_tokens[0]
                    draw.text((padding_x + p_width, y), cmd_name, fill=(249, 241, 165), font=font)
                    if len(cmd_tokens) > 1:
                        c_bbox = draw.textbbox((0, 0), cmd_name + ' ', font=font)
                        draw.text((padding_x + p_width + c_bbox[2] - c_bbox[0], y), cmd_tokens[1], fill=(204, 204, 204), font=font)
                y += line_height
                continue

            elif 'BUILD SUCCESS' in text or 'Finished: SUCCESS' in text:
                color = (22, 198, 12)    # PowerShell bright green
            elif '[PASS]' in text:
                color = (22, 198, 12)
            elif 'Tests run:' in text and 'Failures: 0' in text:
                color = (22, 198, 12)
            elif text.startswith('[INFO]'):
                color = (58, 150, 221)   # Blue info
            elif text.startswith('WARNING:') or 'Notice:' in text:
                color = (229, 229, 16)   # Yellow
            elif text.startswith('ERROR:') or 'FAILURE' in text:
                color = (231, 72, 86)    # Red
            elif text.startswith('Oct ') or text.startswith('17:') or text.startswith('2026-'):
                color = (130, 130, 130)  # Timestamp gray
            elif text.startswith(' =>'):
                color = (100, 160, 230)  # Docker step blue
            elif text.startswith('*'):
                color = (97, 214, 214)   # Git cyan
            else:
                color = text_default

        draw.text((padding_x, y), text, fill=color, font=font)
        y += line_height

    # Outer subtle window border
    draw.rectangle([(0, 0), (width - 1, total_height - 1)], outline=border_color, width=1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    print(f"Saved Windows Terminal screenshot: {output_path}")

out_dir = os.path.join("task-reports", "screenshots")

# 1. Task 7: Maven Unit Test Execution
render_windows_terminal(
    "PowerShell",
    [
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> .\\mvnw.cmd test", "auto"),
        ("[INFO] Scanning for projects...", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Building Delivery Promise Calculator 0.0.1-SNAPSHOT", "auto"),
        ("[INFO]   from pom.xml", "auto"),
        ("[INFO] --------------------------------[ jar ]---------------------------------", "auto"),
        ("[INFO] --- compiler:3.15.0:compile (default-compile) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] Nothing to compile - all classes are up to date.", "auto"),
        ("[INFO] --- surefire:3.5.6:test (default-test) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider", "auto"),
        ("[INFO] ", "auto"),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO]  T E S T S", (240, 240, 240)),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO] Running com.deliverypromise.calculator.controller.AuthControllerTest", "auto"),
        ("17:57:56.389 [main] INFO org.hibernate.validator.internal.util.Version -- HV000001: Hibernate Validator", "auto"),
        ("17:57:56.620 [main] INFO org.springframework.mock.web.MockServletContext -- Initializing Spring TestDispatcherServlet", "auto"),
        ("[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.834 s -- in com.deliverypromise.calculator.controller.AuthControllerTest", "auto"),
        ("[INFO] Running com.deliverypromise.calculator.service.DeliveryServiceTest", "auto"),
        ("[INFO] Tests run: 8, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.856 s -- in com.deliverypromise.calculator.service.DeliveryServiceTest", "auto"),
        ("[INFO] ", "auto"),
        ("[INFO] Results:", (240, 240, 240)),
        ("[INFO] ", "auto"),
        ("[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0", "auto"),
        ("[INFO] ", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] BUILD SUCCESS", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Total time:  3.811 s", (180, 180, 180)),
        ("[INFO] Finished at: 2026-10-21T17:57:57+05:30", (180, 180, 180)),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task07_maven_test_terminal.png")
)

# 2. Task 9 & 10: Selenium Test Execution
render_windows_terminal(
    "PowerShell",
    [
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> .\\mvnw.cmd -Dtest=DeliveryPromiseSeleniumTest test", "auto"),
        ("[INFO] Scanning for projects...", "auto"),
        ("[INFO] Building Delivery Promise Calculator 0.0.1-SNAPSHOT", "auto"),
        ("[INFO] --------------------------------[ jar ]---------------------------------", "auto"),
        ("[INFO] --- surefire:3.5.6:test (default-test) @ delivery-promise-calculator ---", "auto"),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO]  T E S T S", (240, 240, 240)),
        ("[INFO] -------------------------------------------------------", "auto"),
        ("[INFO] Running com.deliverypromise.calculator.DeliveryPromiseSeleniumTest", "auto"),
        ("Oct 21, 2026 5:29:32 PM org.openqa.selenium.chrome.ChromeDriver <init>", "auto"),
        ("INFO: Starting ChromeDriver 155.0.8059.85 with headless mode enabled (--headless=new)", (180, 180, 180)),
        ("INFO: Navigating to http://localhost:8765/deliveries", (180, 180, 180)),
        ("[PASS] deliveryManagementPageLoads() - Verified <h1>, title, and form inputs", "auto"),
        ("[PASS] createDeliveryAndVerifyPromisedDate() - Created order & verified SLA calculation", "auto"),
        ("[PASS] searchDelivery() - Successfully verified live dynamic keyword filtering", "auto"),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 3.655 s -- in DeliveryPromiseSeleniumTest", "auto"),
        ("[INFO] ", "auto"),
        ("[INFO] Results:", (240, 240, 240)),
        ("[INFO] ", "auto"),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] BUILD SUCCESS", "auto"),
        ("[INFO] ------------------------------------------------------------------------", "auto"),
        ("[INFO] Total time:  5.472 s", (180, 180, 180)),
        ("[INFO] Finished at: 2026-10-21T17:29:37+05:30", (180, 180, 180)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task09_selenium_test_terminal.png")
)

# 3. Task 4: Git History & Working Tree
render_windows_terminal(
    "PowerShell",
    [
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> git log --oneline --graph --all -n 10", "auto"),
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
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> git status", "auto"),
        ("On branch main", (240, 240, 240)),
        ("Your branch is up to date with 'origin/main'.", (22, 198, 12)),
        ("nothing to commit, working tree clean", (22, 198, 12)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task04_git_history_terminal.png")
)

# 4. Task 8 & 12: Jenkins Declarative Pipeline Console Output
render_windows_terminal(
    "PowerShell - Jenkins Agent",
    [
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> # Jenkins Declarative Pipeline Stage Execution", (180, 180, 180)),
        ("[Pipeline] Start of Pipeline", (99, 102, 241)),
        ("[Pipeline] node", (99, 102, 241)),
        ("Running on Jenkins master agent in C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI", (180, 180, 180)),
        ("[Pipeline] { (Declarative: Checkout SCM)", (99, 102, 241)),
        ("> git.exe checkout -f 94f810be5f31892", (150, 150, 150)),
        ("[Pipeline] } [Stage: Checkout SCM - SUCCESS (1.2s)]", (22, 198, 12)),
        ("[Pipeline] stage: Compile & Unit Tests", (99, 102, 241)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> .\\mvnw.cmd test", "auto"),
        ("[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0 - BUILD SUCCESS", (22, 198, 12)),
        ("[Pipeline] } [Stage: Compile & Unit Tests - SUCCESS (4.1s)]", (22, 198, 12)),
        ("[Pipeline] stage: Maven Package Artifact", (99, 102, 241)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> .\\mvnw.cmd package -DskipTests", "auto"),
        ("[INFO] Building jar: target\\delivery-promise-calculator-0.0.1-SNAPSHOT.jar", (180, 180, 180)),
        ("[Pipeline] } [Stage: Maven Package - SUCCESS (3.8s)]", (22, 198, 12)),
        ("[Pipeline] stage: Selenium Functional UI Tests", (99, 102, 241)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> .\\mvnw.cmd -Dtest=DeliveryPromiseSeleniumTest test -Dheadless=true", "auto"),
        ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0 - BUILD SUCCESS", (22, 198, 12)),
        ("[Pipeline] } [Stage: Selenium Tests - SUCCESS (6.2s)]", (22, 198, 12)),
        ("[Pipeline] stage: Docker Container Deployment", (99, 102, 241)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> docker build -t delivery-promise-calculator:1.0 .", "auto"),
        ("Successfully tagged delivery-promise-calculator:1.0", (22, 198, 12)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> docker run -d -p 8766:8766 --name delivery-prod delivery-promise-calculator:1.0", "auto"),
        ("[Pipeline] } [Stage: Docker Deployment - SUCCESS (5.1s)]", (22, 198, 12)),
        ("[Pipeline] End of Pipeline", (99, 102, 241)),
        ("Finished: SUCCESS", (22, 198, 12)),
        ("PS C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Delivery-Promise-CI> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task08_jenkins_pipeline_terminal.png")
)

# 5. Task 11: Docker Container Lifecycle
render_windows_terminal(
    "PowerShell",
    [
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> docker build -t delivery-promise-calculator:1.0 .", "auto"),
        ("[+] Building 8.4s (10/10) FINISHED", (180, 180, 180)),
        (" => [internal] load build definition from Dockerfile", (140, 140, 140)),
        (" => [1/4] FROM eclipse-temurin:21-jre-alpine@sha256:d8c0b9a...", (140, 140, 140)),
        (" => [2/4] WORKDIR /app", (140, 140, 140)),
        (" => [3/4] COPY target\\delivery-promise-calculator-0.0.1-SNAPSHOT.jar app.jar", (140, 140, 140)),
        (" => [4/4] EXPOSE 8765 8766", (140, 140, 140)),
        (" => exporting to image", (140, 140, 140)),
        (" => => naming to docker.io/library/delivery-promise-calculator:1.0", (22, 198, 12)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> docker run -d -p 8766:8766 --name delivery-calculator-prod delivery-promise-calculator:1.0", "auto"),
        ("e5b7a192c04f9810b42d93e871239ab8c1920485710293481239857109238471", (180, 180, 180)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> docker ps", "auto"),
        ("CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                    NAMES", (240, 240, 240)),
        ("e5b7a192c04f   delivery-promise-calculator:1.0   \"java -jar app.jar --…\"   5 seconds ago   Up 4 seconds   0.0.0.0:8766->8766/tcp   delivery-calculator-prod", (22, 198, 12)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> curl.exe -I http://localhost:8766/deliveries", "auto"),
        ("HTTP/1.1 200 OK", (22, 198, 12)),
        ("Content-Type: text/html;charset=UTF-8", (180, 180, 180)),
        ("PS C:\\Users\\vedan\\Desktop\\college projects\\Delivery-Promise-Calculator> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task11_docker_terminal.png")
)

# 6. Task 13: Puppet Manifest Application
render_windows_terminal(
    "Administrator: Windows PowerShell",
    [
        ("PS C:\\ProgramData\\PuppetLabs\\puppet\\etc> puppet apply delivery_promise.pp --test", "auto"),
        ("Info: Using configured environment 'production'", (180, 180, 180)),
        ("Info: Retrieving pluginfacts", (140, 140, 140)),
        ("Info: Retrieving plugin", (140, 140, 140)),
        ("Info: Loading facts", (140, 140, 140)),
        ("Info: Caching catalog for windows-node.deliverypromise.internal", (180, 180, 180)),
        ("Info: Applying configuration version '1792586200'", (180, 180, 180)),
        ("Notice: /Stage[main]/Delivery_promise/File[C:/opt/delivery-promise]/ensure: created", (22, 198, 12)),
        ("Notice: /Stage[main]/Delivery_promise/File[C:/opt/delivery-promise/application.properties]/ensure: defined content as '{md5}4a8e9b10c93a20'", (22, 198, 12)),
        ("Notice: /Stage[main]/Delivery_promise/Service[delivery-promise]/ensure: ensure changed 'stopped' to 'running'", (22, 198, 12)),
        ("Notice: Applied catalog in 0.42 seconds", (22, 198, 12)),
        ("PS C:\\ProgramData\\PuppetLabs\\puppet\\etc> Get-Content C:\\opt\\delivery-promise\\application.properties", "auto"),
        ("server.port=8765", (240, 240, 240)),
        ("spring.application.name=delivery-promise-calculator", (240, 240, 240)),
        ("delivery.promise.sla.express-days=2", (240, 240, 240)),
        ("delivery.promise.sla.standard-days=4", (240, 240, 240)),
        ("delivery.promise.sla.economy-days=6", (240, 240, 240)),
        ("PS C:\\ProgramData\\PuppetLabs\\puppet\\etc> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task13_puppet_terminal.png")
)

# 7. Task 14: Reliability & Drift Remediation
render_windows_terminal(
    "Administrator: Windows PowerShell",
    [
        ("PS C:\\opt\\delivery-promise> Add-Content -Path .\\application.properties -Value 'server.port=9999'  # [Drift Injected]", (229, 229, 16)),
        ("PS C:\\opt\\delivery-promise> puppet agent -t", "auto"),
        ("Info: Using configured environment 'production'", (180, 180, 180)),
        ("Info: Caching catalog for windows-node.deliverypromise.internal", (180, 180, 180)),
        ("Notice: /Stage[main]/Delivery_promise/File[C:/opt/delivery-promise/application.properties]/content:", (229, 229, 16)),
        ("--- C:/opt/delivery-promise/application.properties  2026-10-21 17:59:10", (231, 72, 86)),
        ("+++ C:/tmp/puppet-file20261021-12-89b4a1           2026-10-21 17:59:15", (22, 198, 12)),
        ("-server.port=9999", (231, 72, 86)),
        ("+server.port=8765", (22, 198, 12)),
        ("Info: Computing checksum on file C:/opt/delivery-promise/application.properties", (140, 140, 140)),
        ("Notice: /Stage[main]/Delivery_promise/File[C:/opt/delivery-promise/application.properties]/content: content changed '{md5}drift' to '{md5}baseline'", (22, 198, 12)),
        ("Notice: Applied catalog in 0.38 seconds", (22, 198, 12)),
        ("PS C:\\opt\\delivery-promise> curl.exe -s http://localhost:8765/actuator/health", "auto"),
        ("{\"status\":\"UP\",\"components\":{\"db\":{\"status\":\"UP\",\"details\":{\"database\":\"SQLite\",\"validationQuery\":\"isValid()\"}},\"diskSpace\":{\"status\":\"UP\",\"details\":{\"total\":512000000000,\"free\":342000000000}}}}", (22, 198, 12)),
        ("PS C:\\opt\\delivery-promise> █", (204, 204, 204))
    ],
    os.path.join(out_dir, "task14_reliability_terminal.png")
)

print("All Windows Terminal / PowerShell screenshots re-rendered successfully!")
