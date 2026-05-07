import os
import re

pub_dir = '_publications'
for filename in os.listdir(pub_dir):
    if not filename.endswith('.md'): continue
    filepath = os.path.join(pub_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'pub_year:' in content: continue
    
    match = re.search(r'^date:\s*(\d{4})', content, re.MULTILINE)
    if match:
        year = match.group(1)
        content = re.sub(r'^(date: .*)$', rf'\1\npub_year: "{year}"', content, flags=re.MULTILINE)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with pub_year: {year}")
