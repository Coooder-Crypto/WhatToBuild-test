import os
import yaml
import re

def parse_idea_md(file_path):
    try:
        # Get the repository root directory
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Construct the full path
        full_path = os.path.join(repo_root, file_path)
        print("Full Path:", full_path)
        
        with open(full_path, 'r') as f:
            content = f.read()
            # Extract YAML part
            _, yaml_content, _ = content.split('---', 2)
            # Parse YAML
            data = yaml.safe_load(yaml_content.strip())
            return data
    except Exception as e:
        print(f"Error parsing YAML from {file_path}: {e}")
        raise

def update_readme(idea_data, file_path):
    try:
        readme_path = "README.md"
        with open(readme_path, 'r') as f:
            readme_content = f.read()
        
        # Generate new content title (based on YAML data)
        idea_title = idea_data.get("title", "Untitled Idea")
        new_section = f"## {idea_title}\n\n{idea_data.get('description', '')}\n\n"
        
        # Find old title (based on file path)
        old_section_pattern = f"## .*? \\(File: {file_path}\\)"
        match = re.search(old_section_pattern, readme_content, re.DOTALL)
        
        if match:
            # If old title found, replace with new content
            updated_content = re.sub(old_section_pattern, new_section.rstrip(), readme_content, flags=re.DOTALL)
            with open(readme_path, 'w') as f:
                f.write(updated_content)
            print(f"Updated README with new section for '{idea_title}'.")
        else:
            # If old title not found, append new content
            with open(readme_path, 'a') as f:
                f.write(new_section)
            print(f"Appended new section to README for '{idea_title}'.")
    except Exception as e:
        print(f"Error updating README: {e}")
        raise

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parse_idea.py <idea_file>")
        sys.exit(1)
    
    idea_file = sys.argv[1]
    try:
        idea_data = parse_idea_md(idea_file)
        print("Parsed Idea Data:", idea_data)
        update_readme(idea_data, idea_file)
    except Exception as e:
        print("Error processing file:", e)