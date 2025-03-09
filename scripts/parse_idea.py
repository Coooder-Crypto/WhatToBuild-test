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

def update_readme(idea_data, file_path, readme_content):
    # 生成新内容的标题（基于 YAML 数据）
    idea_title = idea_data.get("title", "Untitled Idea")
    new_section = f"## {idea_title}\n\n{idea_data.get('description', '')}\n\n"
    
    # 查找旧标题（基于文件路径）
    old_section_pattern = f"## .*? \\(File: {file_path}\\)"
    import re
    match = re.search(old_section_pattern, readme_content, re.DOTALL)
    
    if match:
        # 如果找到旧标题，替换为新内容
        readme_content = re.sub(old_section_pattern, new_section.rstrip(), readme_content, flags=re.DOTALL)
    else:
        # 如果未找到旧标题，追加新内容
        readme_content += new_section
    
    return readme_content

def generate_readme(idea_files):
    readme_content = "# Idea List\n\n"
    for idea_file in idea_files:
        try:
            idea_data = parse_idea_md(idea_file)
            print("Parsed Idea Data:", idea_data)
            readme_content = update_readme(idea_data, idea_file, readme_content)
        except Exception as e:
            print(f"Error parsing file {idea_file}: {e}")
    
    # 写入到 README.md
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
