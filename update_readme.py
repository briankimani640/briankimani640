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
    
    # Overwrites the entire README cleanly from scratch — making duplicates impossible
    readme_content = f"""# Hi there 👋

Here is your daily dose of dev humor, updated automatically via GitHub Actions:

{new_quote}
"""
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()
