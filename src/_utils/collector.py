import os
import yaml
import re
import requests

def collect(path='.', pattern='*.md'):
    def extract_frontmatter(content):
        frontmatter = {}
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                frontmatter = yaml.safe_load(content[3:end].strip())
                content = content[end + 3:].strip()
        return frontmatter, content

    markdown_files = {}
    base_path = os.path.abspath(path)
    conf_py_dir = os.getcwd()

    for root, _, files in os.walk(base_path):
        for file_name in files:
            if re.match(pattern.replace('.', r'\.').replace('*', r'.*'), file_name):
                full_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(full_path, conf_py_dir)
                url = os.path.splitext(relative_path)[0]
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    frontmatter, content = extract_frontmatter(content)

                    markdown_files[os.path.splitext(file_name)[0]] = {
                        'path': {
                            'full': full_path,
                            'relative': relative_path,
                            'url': url,
                        },
                        'frontmatter': frontmatter,
                        'content': content
                    }

    return markdown_files

def fetch_yaml_files():
    repo_owner = "your-username"
    repo_name = "your-repo"
    file_path = "path/to/your/file.yaml"
    token = os.environ.get('GITHUB_TOKEN')

    headers = {'Authorization': f'token {token}'}
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json()
        if content['encoding'] == 'base64':
            yaml_content = base64.b64decode(content['content'])
            # Further processing of YAML content

if __name__ == '__main__':
    fetch_yaml_files()
