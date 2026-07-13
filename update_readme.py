import urllib.request
import json

def fetch_quote():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())[0]
            return f"**\"{data['setup']}\"**\n\n*{data['punchline']}*"
    except Exception as e:
        return "**\"Code is like humor. When you have to explain it, it’s bad.\"**\n\n*– Cory House*"

def update_readme():
    new_quote = fetch_quote()
    
    # Everything outside the quote marker tags stays permanent on your profile
    readme_content = f"""# Hi there, I'm Brian 👋

I'm a Mathematics and Computer Science student and full-stack software developer who enjoys building clean, scalable web and mobile applications. 

### 🚀 What I'm Up To
- 💻 Actively developing modular full-stack applications and RESTful APIs.
- 📱 Exploring cross-platform mobile development and database architecture.
- 🌱 Continuously refining my skills in algorithmic problem-solving and clean code practices.

### 🛠️ Tech Stack & Tools
- **Languages:** Python, JavaScript, TypeScript, SQL, HTML5/CSS3
- **Frameworks & Libraries:** Django, React, React Native, Tailwind CSS, Bootstrap
- **Databases & ORMs:** PostgreSQL, MySQL, SQLite, Prisma ORM
- **Tools & Workflow:** Git, GitHub, Linux, VS Code

---

### ⚡ Daily Dev Humor
Here is a random programming joke fetched and updated automatically every day via GitHub Actions:

<!-- START_SECTION:quote -->
{new_quote}
<!-- END_SECTION:quote -->

---
💬 *Feel free to reach out or check out my repositories below!*
"""
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()
