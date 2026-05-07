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

for i, pub in enumerate(author['publications'][:20]):
    try:
        scholarly.fill(pub)
    except Exception as e:
        print(f"Failed to fill pub {i}: {e}")
        continue
        
    bib = pub.get('bib', {})
    title = bib.get('title', 'Unknown Title')
    year = bib.get('pub_year', '2026')
    authors = bib.get('author', 'Pablo Ouro')
    
    # Extract journal name, volume, pages
    journal = bib.get('journal', bib.get('conference', bib.get('venue', 'Unknown Venue')))
    volume = bib.get('volume', '')
    pages = bib.get('pages', '')
    
    # Format the venue/journal field for the markdown frontmatter
    venue_display = journal
    if volume: venue_display += f" {volume}"
    if pages: venue_display += f", {pages}"
    
    filename_title = re.sub(r'[^a-zA-Z0-9]+', '_', title.lower())[:40].strip('_')
    filename = f"{year}_{filename_title}.md"
    
    with open(os.path.join(pub_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"collection: publications\n")
        f.write(f"permalink: /publication/{year}-{filename_title}\n")
        f.write(f"date: {year}-01-01\n")
        f.write(f"venue: '{venue_display}'\n")
        f.write(f"---\n\n")
        f.write(f"**Authors:** {authors}<br>\n")
        f.write(f"**Title:** {title}<br>\n")
        f.write(f"**Year:** {year}<br>\n")
        f.write(f"**Journal/Venue:** {journal}<br>\n")
        if volume: f.write(f"**Volume:** {volume}<br>\n")
        if pages: f.write(f"**Pages:** {pages}<br>\n")

print("Done generating publications.")
