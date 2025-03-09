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

def update_readme(idea_data, file_path):
    readme_path = "README.md"
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # 生成新内容的标题（基于文件名和 YAML 数据）
    idea_title = idea_data.get("title", os.path.splitext(os.path.basename(file_path))[0])
    new_section = f"## {idea_title}\n\n{idea_data.get('description', '')}\n\n"
    
    # 检查是否已经存在相同标题的内容
    if f"## {idea_title}" in readme_content:
        print(f"Section for '{idea_title}' already exists in README. Skipping update.")
        return
    
    # 在 README 中追加新内容
    with open(readme_path, 'a') as f:
        f.write(new_section)
    print(f"Updated README with new section for '{idea_title}'.")

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
        print("Error parsing file:", e)
