import os
import yaml
from datetime import datetime

def parse_idea_md(file_path):
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(repo_root, file_path)
    print("Processing:", full_path)
    
    with open(full_path, 'r') as f:
        content = f.read()
        # Extract YAML part
        _, yaml_content, _ = content.split('---', 2)
        # Parse YAML
        data = yaml.safe_load(yaml_content.strip())
        # Add file path to data
        data['file_path'] = os.path.relpath(full_path, repo_root)
        return data

def format_tags(tags):
    return ', '.join([f'`{tag}`' for tag in tags])

def format_contributors(contributors):
    return ', '.join([f'[{c["name"]}](https://github.com/{c["github"]})' for c in contributors])

def generate_readme_content(ideas):
    # Start with the header
    content = [
        "# 🚀 Awesome Ideas Collection",
        "",
        "Welcome to the **Awesome Ideas Collection**! This is a place to share, discuss, and collaborate on innovative ideas. Feel free to submit your own idea or contribute to existing ones.",
        "",
        "## 📝 How to Submit an Idea",
        "",
        "1. Fork this repository",
        "2. Copy the [template](template.md) to create your idea file in the `ideas/` folder",
        "3. Fill in all required fields and any optional fields that are relevant",
        "4. Submit a Pull Request",
        "5. After review and merge, your idea will be automatically added to this list",
        "",
        "## 🔍 Ideas List",
        "",
        "| Idea | Description | Tags | Contributors | Status |",
        "| ---- | ----------- | ---- | ------------ | ------ |"
    ]

    # Add each idea to the table
    for idea in ideas:
        title = f"[{idea['title']}]({idea['file_path']})"
        description = idea.get('description', '').split('\n')[0]  # First line only
        tags = format_tags(idea.get('tags', []))
        contributors = format_contributors(idea.get('contributors', []))
        status = f"🔵 {idea.get('status', 'ideation')}" if idea.get('status') else '🔵 ideation'

        row = f"| {title} | {description} | {tags} | {contributors} | {status} |"
        content.append(row)

    # Add footer
    content.extend([
        "",
        "## 📊 Status Legend",
        "",
        "- 🔵 ideation - Initial idea stage",
        "- 🟡 in-progress - Active development",
        "- 🟢 completed - Ready to use",
        "",
        "---",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    ])

    return '\n'.join(content)

def generate_readme(idea_files):
    ideas = []
    for idea_file in idea_files:
        try:
            idea_data = parse_idea_md(idea_file)
            ideas.append(idea_data)
        except Exception as e:
            print(f"Error parsing file {idea_file}: {e}")
    
    # Sort ideas by title
    ideas.sort(key=lambda x: x['title'].lower())
    
    # Generate and write README
    readme_content = generate_readme_content(ideas)
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("Updated README.md with all ideas.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parse_idea.py <idea_files>")
        sys.exit(1)
    
    idea_files = sys.argv[1].split()
    generate_readme(idea_files)
