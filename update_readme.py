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
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    new_quote = fetch_quote()
    
    start_tag = "<!-- START_SECTION:quote -->"
    end_tag = "<!-- END_SECTION:quote -->"

    # Verify both tags exist in the file
    if start_tag in content and end_tag in content:
        # Grabs everything before the very first start tag
        before = content.split(start_tag)[0]
        # Grabs everything after the very last end tag (ignoring any duplicates in between)
        after = content.split(end_tag)[-1]
        
        # Reconstructs the file cleanly with exactly one pair of tags
        updated_content = f"{before}{start_tag}\n\n{new_quote}\n\n{end_tag}{after}"
        
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)
    else:
        print("Error: Could not find the START or END marker tags in README.md.")

if __name__ == "__main__":
    update_readme()
