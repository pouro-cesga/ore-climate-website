import os
import re
import sys

try:
    from scholarly import scholarly
except ImportError:
    print("scholarly not installed")
    sys.exit(1)

print("Fetching Pablo Ouro...")
try:
    author = scholarly.search_author_id('_VVX33wAAAAJ')
    scholarly.fill(author, sections=['publications'])
except Exception as e:
    print("Error fetching author:", e)
    sys.exit(1)

pub_dir = "_publications"
os.makedirs(pub_dir, exist_ok=True)

for f in os.listdir(pub_dir):
    if f.endswith('.md'):
        os.remove(os.path.join(pub_dir, f))

for i, pub in enumerate(author['publications'][:100]):
    try:
        scholarly.fill(pub)
    except Exception as e:
        print(f"Failed to fill pub {i}: {e}")
        continue
        
    bib = pub.get('bib', {})
    title = bib.get('title', 'Unknown Title').replace('"', '\\"')
    year = bib.get('pub_year', '2026')
    authors = bib.get('author', 'Pablo Ouro')
    
    # Highlight group members in black font
    members = ["Ouro", "Fernandez", "Rosquete", "Vigara"]
    if authors:
        authors = authors.replace(' and ', ', ')
        parts = authors.split(',')
        for j in range(len(parts)):
            for m in members:
                if m.lower() in parts[j].lower() and '<strong>' not in parts[j]:
                    parts[j] = f'<strong><span style="color: black;">{parts[j].strip()}</span></strong>'
            parts[j] = parts[j].strip()
        authors = ', '.join(parts).strip()
    
    journal = bib.get('journal', bib.get('conference', bib.get('venue', 'Unknown Journal')))
    journal = journal.replace('"', '\\"')
    volume = bib.get('volume', '')
    pages = bib.get('pages', '')
    
    vp = ""
    if volume: vp += str(volume)
    if pages: 
        if vp: vp += f", {pages}"
        else: vp += str(pages)
    vp = vp.replace('"', '\\"')
    
    filename_title = re.sub(r'[^a-zA-Z0-9]+', '_', title.lower())[:40].strip('_')
    filename = f"{year}_{filename_title}.md"
    
    with open(os.path.join(pub_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"collection: publications\n")
        f.write(f"permalink: /publication/{year}-{filename_title}\n")
        f.write(f"date: {year}-01-01\n")
        f.write(f"journal: \"{journal}\"\n")
        f.write(f"authors: \"{authors}\"\n")
        f.write(f"volume_pages: \"{vp}\"\n")
        f.write(f"---\n\n")

print("Done generating publications.")
