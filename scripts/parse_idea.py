#!/usr/bin/env python3
import os
import yaml
import sys

def parse_idea_md(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    frontmatter = content.split('---')[1]
    data = yaml.safe_load(frontmatter)
    return data

def update_readme(idea_data):
    readme_path = 'README.md'
    idea_entry = f"## {idea_data['name']}\n"
    idea_entry += f"- **Description**: {idea_data['description']}\n"
    idea_entry += f"- **Tags**: {', '.join(idea_data['tags'])}\n"
    idea_entry += f"- **Contributors**: {', '.join(idea_data['contributors'])}\n"
    if 'related_links' in idea_data:
        idea_entry += "- **Related Links**:\n"
        for link in idea_data['related_links']:
            idea_entry += f"  - [{link[0]}]({link[1]})\n"
    idea_entry += "\n"

    with open(readme_path, 'a') as f:
        f.write(idea_entry)

if __name__ == '__main__':
    idea_file = sys.argv[1]
    idea_data = parse_idea_md(idea_file)
    update_readme(idea_data)
