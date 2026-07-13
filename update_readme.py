import urllib.request
import json
import re

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
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    new_quote = fetch_quote()
    
    # Replace content between marker tags
    pattern = r"()(.*?)()"
    replacement = f"\\1\n\n{new_quote}\n\n\\3"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()
