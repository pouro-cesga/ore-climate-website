import os

pub_dir = '_publications'
for filename in os.listdir(pub_dir):
    if not filename.endswith('.md'): continue
    filepath = os.path.join(pub_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace double quotes inside the span style with single quotes
    new_content = content.replace('style="color: black;"', "style='color: black;'")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed quotes in {filename}')
