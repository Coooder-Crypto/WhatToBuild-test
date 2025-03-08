import os
import yaml

def parse_idea_md(file_path):
    # 获取仓库根目录
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 拼接完整路径
    full_path = os.path.join(repo_root, file_path)
    print("Full Path:", full_path)
    
    with open(full_path, 'r') as f:
        content = f.read()
        # 提取 YAML 部分
        _, yaml_content, _ = content.split('---', 2)
        # 解析 YAML
        data = yaml.safe_load(yaml_content.strip())
        return data

def update_readme(idea_data):
    readme_path = "README.md"
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # 在 README 中插入新内容
    new_section = f"## {idea_data['title']}\n\n{idea_data['description']}\n\n"
    updated_readme = readme_content + new_section
    
    # 写回 README
    with open(readme_path, 'w') as f:
        f.write(updated_readme)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parse_idea.py <idea_file>")
        sys.exit(1)
    
    idea_file = sys.argv[1]
    try:
        idea_data = parse_idea_md(idea_file)
        print("Parsed Idea Data:", idea_data)
        update_readme(idea_data)
    except Exception as e:
        print("Error parsing file:", e)
