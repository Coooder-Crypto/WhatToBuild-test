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
        frontmatter = content.split('---', 2)[1].strip()
        # 解析 YAML
        data = yaml.safe_load(frontmatter)
        return data

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parse_idea.py <idea_file>")
        sys.exit(1)
    
    idea_file = sys.argv[1]
    try:
        idea_data = parse_idea_md(idea_file)
        print("Parsed Idea Data:", idea_data)
    except Exception as e:
        print("Error parsing file:", e)
