# Run: python build.py  -> regenerates every page from the data below.
import os
NAME="Mohamed Abubakar"; ROLE="Computer Science Graduate"; EMAIL="mohamedabubakar6710@gmail.com"
GH="https://github.com/shadowabu254"; LI="https://www.linkedin.com/in/mohamed-abubakar-ba10232b5/"
S=[
("theory",250,"Theoretical Computer Science and Algorithms","I solve problems efficiently and can prove why the solution works.",
"I learned to measure the cost of a program before writing it. I choose the right data structure, analyze time and memory, and know when a problem is intractable and needs an approximation.",
"Data structures|Graph algorithms|Dynamic programming|Complexity (P vs NP)|Automata and formal languages|Discrete mathematics","C++|Python|Java",
"a route planner using Dijkstra and A*","Fast, scalable code, and performance problems caught before they reach production."),
("robotics",20,"Robotics and Embedded Systems","I make software control real hardware, reliably.",
"I program microcontrollers, read sensors, drive motors and write real-time control loops that run within tight memory and power limits.",
"Microcontrollers|Sensors and actuators|PID control|Real-time systems|I2C, SPI and UART|Robot kinematics","C and C++|Arduino|Raspberry Pi|ROS|Python",
"an obstacle-avoiding robot, with a build video","Comfort close to the hardware, valuable for IoT, devices and automation teams."),
("database",200,"Database Engineering","I design data models that stay correct, fast and easy to change.",
"I turn requirements into normalized schemas, write complex queries, tune them with indexes and execution plans, and reason about transactions and consistency.",
"Relational modeling|Advanced SQL|Indexing and query tuning|ACID transactions|NoSQL models|Backup and recovery","PostgreSQL|MySQL|MongoDB|Redis",
"a booking system schema with a query tuned from seconds to milliseconds","Trustworthy data and applications that stay fast as data grows."),
("networks",160,"Computer Networks and Systems Administration","I understand how data moves and how to keep servers healthy.",
"I configure networks and Linux servers, from addressing and routing to DNS, firewalls and monitoring, and I troubleshoot from the packet upward.",
"TCP/IP and OSI|Subnetting and routing|DNS, DHCP, HTTP|Firewalls and VPNs|Linux administration|Shell scripting","Linux|Wireshark|Cisco Packet Tracer|Bash|Nginx",
"a segmented campus network with VLANs and a firewall","Someone who can diagnose “the site is down” instead of waiting for another team."),
("cloud",215,"Cloud Computing and DevOps","I ship software through automated, repeatable pipelines.",
"I package apps in containers, deploy them to the cloud, describe infrastructure as code, and automate testing and release so deployments become routine.",
"Containers and orchestration|CI/CD pipelines|Infrastructure as code|Cloud compute, storage, networking|Monitoring and logging|Git workflows","Docker|Kubernetes|GitHub Actions|Terraform|AWS, Azure or GCP",
"an app deployed by a pipeline that tests and releases on every push","Faster, safer releases and less manual work for the team."),
("data",140,"Data Science and Analytics","I turn raw data into decisions.",
"I clean messy datasets, explore them statistically, build visualizations and explain the findings so non-technical people can act on them.",
"Data cleaning|Exploratory analysis|Statistics and hypothesis testing|Visualization|Dashboards|Feature engineering","Python|pandas|NumPy|Matplotlib|Power BI or Tableau|Jupyter",
"an analysis of a real dataset with a dashboard and a recommendation","Evidence-based answers and clear storytelling with data."),
("security",350,"Cybersecurity","I think like an attacker so I can defend like an engineer.",
"I find and fix weaknesses in applications and networks, apply cryptography correctly and build secure habits into design from day one.",
"OWASP Top 10|Cryptography basics|Authentication and access control|Network security|Ethical penetration testing|Incident response","Kali Linux|Burp Suite|Nmap|Metasploit|Wireshark",
"a lab where I found and patched SQL injection","Software that protects customer data and a teammate who raises risks early."),
("ai",280,"Artificial Intelligence and Machine Learning","I build models and check honestly whether they work.",
"I train, evaluate and improve models, from classic algorithms to neural networks, and I measure them properly so results can be trusted.",
"Supervised and unsupervised learning|Neural networks|Natural language processing|Computer vision|Model evaluation|Responsible AI","Python|scikit-learn|PyTorch or TensorFlow|Hugging Face|Jupyter",
"an image or text classifier with a live demo","Practical AI features that are tested, explained and ready to integrate."),
("software",35,"Software Engineering and Development","I build maintainable software with a team.",
"I take features from requirements to design, code, tests and review. I write clean code, work in agile teams and document so others can continue my work.",
"Object-oriented design|Design patterns|REST APIs|Front end and back end|Automated testing|Agile and code review","JavaScript and TypeScript|Python|Java|React|Node.js|Git",
"my final-year full-stack app, with live link and my role","A developer who delivers working features and leaves the codebase better."),
("hci",320,"Human-Computer Interaction (HCI)","I design interfaces people can actually use.",
"I study how people think and behave, then design and test interfaces around them: research, wireframes, prototypes and usability testing.",
"User research|Usability heuristics|Wireframing and prototyping|Accessibility (WCAG)|Usability testing|Interaction design","Figma|Miro|Maze or Hotjar|HTML and CSS",
"a redesign of an app, with before and after test results","Products that are easier to use, which means higher adoption and fewer support tickets."),
("infosys",180,"Information Systems","I connect technology to how organizations really work.",
"I analyze business processes, model requirements and design systems that give organizations reliable information, from ERP and reporting to governance and security.",
"Systems analysis and design|Business process modeling|Requirements engineering|ERP and enterprise systems|IT governance|Project management","UML and BPMN|Draw.io|SQL|Excel and Power BI|Jira",
"a system proposal for a real organization, with diagrams and a cost case","Someone who speaks both technical and business language and turns needs into working systems."),
]
PROJ=[
("Rental Website","Soltech Kenya",["software","database","hci"],"A website that lists rental properties and lets people search and enquire. [Add features and your role.]"),
("Community Disaster Project","Machakos University",["robotics","data","software"],"A project to sense and reduce the effects of disasters in the community. [Add what you sensed, how, and the outcome.]"),
("Study Session Website","Personal project",["software","hci"],"A website where students organize and join study sessions. [Add features and who uses it.]"),
("Tenant Monitoring System","Property management",["infosys","database","software"],"A system to track tenants, payments and property records. [Add features and impact.]"),
("Programmer Team Lead and Lecturer","Machakos Youth Service",["software","infosys"],"I formed and taught a team of programmers as a lecturer. [Add how many people and what they built.]"),
("Money Market System","Soltech Kenya",["software","database","security","infosys"],"A system for managing money market transactions. [Add features, security measures and users.]"),
("Network Engineer","Dwa Estate",["networks","security"],"I designed, ran and fixed the network for an estate company. [Add scale: devices, sites, uptime.]"),
("Network Applications for Companies","Client work",["networks","software"],"Applications that help companies manage and monitor their networks. [Add clients and tools.]"),
("AI and Machine Learning System","Soltech Kenya",["ai","data"],"An AI system built on company data. [Add the problem, model and accuracy.]"),
("Other Company Projects","Soltech Kenya",["software","cloud"],"A range of other systems I delivered at the company. [List your top 2 to 3 here.]")]
def card(p,pre):
    links=" · ".join(f'<a href="{pre}{i}.html" style="--h:{next(s[1] for s in S if s[0]==i)}">{next(s[2] for s in S if s[0]==i).split(" (")[0].split(" and ")[0]}</a>' for i in p[2])
    return f'<article class="pc"><small>{p[1]}</small><h3>{p[0]}</h3><p>{p[3]}</p><p><b>Result:</b> [Add a real number: users, speed, time saved]</p><div class="sl">{links}</div></article>'
CSS="""
:root{--bg:#f7f8fa;--card:#fff;--ink:#0f1626;--mute:#556078;--line:#dde2ea;--h:250;--ac:hsl(var(--h) 70% 46%);--tint:hsl(var(--h) 80% 94%)}
@media (prefers-color-scheme:dark){:root{--bg:#0b101b;--card:#131a29;--ink:#eef1f8;--mute:#a1abc2;--line:#27314a;--ac:hsl(var(--h) 85% 70%);--tint:hsl(var(--h) 35% 17%);color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.7 "DM Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,.d{font-family:"Bricolage Grotesque","DM Sans",system-ui,sans-serif;letter-spacing:-.025em;line-height:1.05;margin:0}
a{color:var(--ac)}:focus-visible{outline:3px solid var(--ac);outline-offset:3px}
.w{max-width:1120px;margin:0 auto;padding:0 24px}
nav.t{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav.t .w{display:flex;justify-content:space-between;align-items:center;height:62px}
nav.t b{font:700 18px "Bricolage Grotesque",sans-serif}nav.t div a{margin-left:22px;color:var(--mute);text-decoration:none;font-size:15px}nav.t div a:hover{color:var(--ink)}
.hero{padding:96px 0 56px}.hero h1{font-size:clamp(2.8rem,9vw,7rem);max-width:12em}
.hero p{font-size:1.25rem;color:var(--mute);max-width:34em;margin:28px 0 0}
.b{display:inline-block;margin:32px 12px 0 0;padding:14px 26px;border-radius:999px;font:600 15px "DM Sans",sans-serif;text-decoration:none;border:2px solid var(--ink);color:var(--ink)}
.b.p{background:var(--ink);color:var(--bg)}.b:hover{border-color:var(--ac)}
section.s{padding:72px 0;border-top:1px solid var(--line)}
.lab{font:600 15px "DM Sans",sans-serif;color:var(--mute);margin-bottom:20px}
.about p{font-size:1.4rem;line-height:1.5;max-width:30em}
.st{display:flex;gap:48px;flex-wrap:wrap;margin-top:36px}.st b{display:block;font:700 2.6rem "Bricolage Grotesque",sans-serif}.st span{color:var(--mute);font-size:15px}
.rows a{display:grid;grid-template-columns:20px 1fr 1.1fr;gap:20px;align-items:center;padding:26px 16px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);transition:background .2s,padding .2s}
.rows a:first-child{border-top:1px solid var(--line)}
.rows i{width:14px;height:14px;border-radius:50%;background:var(--ac)}
.rows h3{font-size:clamp(1.3rem,2.6vw,2rem)}.rows p{margin:0;color:var(--mute);font-size:15px;line-height:1.5}
.rows a:hover{background:var(--tint);padding-left:28px}
.ph{padding:80px 0 56px;background:var(--tint);border-bottom:1px solid var(--line)}
.ph a.back{color:var(--mute);text-decoration:none;font-size:15px}.ph h1{font-size:clamp(2.3rem,6.5vw,5rem);margin:22px 0 18px;max-width:14em}
.ph p{font-size:1.3rem;max-width:30em;margin:0;color:var(--ink)}
.blk{display:grid;grid-template-columns:230px 1fr;gap:40px;padding:48px 0;border-bottom:1px solid var(--line)}
.blk h2{font-size:1.5rem;color:var(--ac)}.blk p{margin:0 0 14px;max-width:36em}
ul.c{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
ul.c li{padding:7px 16px;border-radius:999px;border:1px solid var(--line);background:var(--card);font-size:15px}
.pr{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px}
.pr h3{font-size:1.5rem;margin-bottom:14px}.pr dt{font-weight:700;margin-top:14px}.pr dd{margin:2px 0 0;color:var(--mute)}
.hire{font-size:1.35rem;line-height:1.5;max-width:28em}
.pn{display:flex;justify-content:space-between;gap:20px;padding:40px 0}.pn a{text-decoration:none;color:var(--ink);font:700 1.2rem "Bricolage Grotesque",sans-serif;max-width:45%}.pn small{display:block;color:var(--mute);font:400 14px "DM Sans",sans-serif}.pn a:last-child{text-align:right}.pn a:hover{color:var(--ac)}
footer{padding:40px 24px;text-align:center;color:var(--mute);font-size:14px;border-top:1px solid var(--line)}
.ct{text-align:center}.ct h2{font-size:clamp(2.2rem,6vw,4.5rem);margin-bottom:20px}.ct p{color:var(--mute);max-width:28em;margin:0 auto}
.pcs{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}.pc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:24px;display:flex;flex-direction:column}.pc small{color:var(--mute);font-weight:600}.pc h3{font-size:1.35rem;margin:6px 0 10px}.pc p{margin:0 0 10px;font-size:15px;color:var(--mute)}.pc .sl{margin-top:auto;font-size:14px;font-weight:600}.pc .sl a{color:var(--ac)}
@media(max-width:760px){.rows a{grid-template-columns:16px 1fr}.rows p{grid-column:2}.blk{grid-template-columns:1fr;gap:14px}nav.t div a:not(:last-child){display:none}.pn a{max-width:48%}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""
def page(title,body,root,h=250):
    return f'''<!DOCTYPE html><html lang="en" style="--h:{h}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{NAME}: {ROLE} portfolio.">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700&family=DM+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css"></head><body>
<nav class="t"><div class="w"><b>{NAME}</b><div><a href="{root}index.html#skills">Skills</a><a href="{root}index.html#projects">Projects</a><a href="{root}index.html#about">About</a><a href="{root}index.html#contact">Contact</a></div></div></nav>
{body}<footer>© 2026 {NAME}. Handcrafted with HTML and CSS.</footer></body></html>'''
li=lambda t:"<ul class='c'>"+"".join(f"<li>{x}</li>" for x in t.split("|"))+"</ul>"
rows="".join(f'<a href="skills/{s[0]}.html" style="--h:{s[1]}"><i></i><h3>{s[2]}</h3><p>{s[3]}</p></a>' for s in S)
idx=f'''<main><div class="w hero"><h1>{NAME}. I build software from the circuit board to the cloud.</h1>
<p>{ROLE} with four years of hands-on work across eleven areas of computing and {len(PROJ)} real projects. Open any skill to see what I learned, my tools, and a project that proves it.</p>
<a class="b p" href="#skills">Explore my skills</a><a class="b" href="#contact">Hire me</a></div>
<section class="s about" id="about"><div class="w"><div class="lab">About me</div>
<p>I like understanding every layer of a system: the algorithm behind it, the data under it, the network around it and the person using it. I studied in Machakos University, My goal is to become a productive person in the ecosystem especially in tech related fields and the role i want is variety because i understand systems in different patterns unifying them to become an expert in computer science.</p>
<div class="st"><div><b>4</b><span>years of study</span></div><div><b>11</b><span>skill areas</span></div><div><b>{len(PROJ)}</b><span>projects</span></div><div><b>2026</b><span>graduation</span></div></div></div></section>
<section class="s" id="skills"><div class="w"><div class="lab">Skills. Select one to read more.</div><div class="rows">{rows}</div></div></section>
<section class="s" id="projects"><div class="w"><div class="lab">Projects and experience</div><div class="pcs">{"".join(card(p,"skills/") for p in PROJ)}</div></div></section>
<section class="s ct" id="contact"><div class="w"><h2>Let’s build something together.</h2><p>I’m open to internships, graduate roles and projects. I reply within two days.</p>
<a class="b p" href="mailto:{EMAIL}">Email me</a><a class="b" href="{GH}">GitHub</a><a class="b" href="{LI}">LinkedIn</a><a class="b" href="cv.pdf" download="MohamedAbubakarCv.pdf">Download CV</a></div></section></main>'''
os.makedirs("skills",exist_ok=True)
open("style.css","w").write(CSS); open("index.html","w").write(page(f"{NAME} · Portfolio",idx,"",250))
for n,s in enumerate(S):
    p=S[n-1]; q=S[(n+1)%len(S)]; rel="".join(card(x,"") for x in PROJ if s[0] in x[2])
    b=f'''<main><header class="ph"><div class="w"><a class="back" href="../index.html#skills">Back to all skills</a><h1>{s[2]}</h1><p>{s[3]}</p></div></header><div class="w">
<div class="blk"><h2>What I learned</h2><div><p>{s[4]}</p></div></div>
<div class="blk"><h2>Topics I know</h2>{li(s[5])}</div>
<div class="blk"><h2>Tools I use</h2>{li(s[6])}</div>
<div class="blk"><h2>Proof of work</h2><div class="pcs">{rel}</div></div>
<div class="blk" style="border:0"><h2>Why this matters to you</h2><p class="hire">{s[8]}</p></div>
<div class="pn"><a href="{p[0]}.html"><small>Previous</small>{p[2]}</a><a href="{q[0]}.html"><small>Next</small>{q[2]}</a></div></div></main>'''
    open(f"skills/{s[0]}.html","w").write(page(f"{s[2]} · {NAME}",b,"../",s[1]))
print("built",len(S)+1,"pages")
