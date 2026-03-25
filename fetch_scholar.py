import urllib.request
from bs4 import BeautifulSoup
import re
import os

url = "https://scholar.google.co.uk/citations?user=_VVX33wAAAAJ&hl=en&pagesize=20"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

print("Fetching URL...")
try:
    html = urllib.request.urlopen(req).read()
except Exception as e:
    print(f"Error: {e}")
    exit(1)

print("Parsing HTML...")
soup = BeautifulSoup(html, 'html.parser')

pub_dir = "_publications"
os.makedirs(pub_dir, exist_ok=True)
for f in os.listdir(pub_dir):
    if f.endswith('.md'):
        os.remove(os.path.join(pub_dir, f))

rows = soup.find_all('tr', class_='gsc_a_tr')
print(f"Found {len(rows)} publications.")

for row in rows:
    title_a = row.find('a', class_='gsc_a_at')
    if not title_a: continue
    title = title_a.text
    
    divs = row.find_all('div', class_='gs_gray')
    authors = divs[0].text if len(divs) > 0 else "Pablo Ouro"
    journal = divs[1].text if len(divs) > 1 else "Unknown Journal"
    
    year_span = row.find('span', class_='gsc_a_h gsc_a_hc gs_ibl')
    year = year_span.text if year_span and year_span.text.strip() else "2026"
    
    filename_title = re.sub(r'[^a-zA-Z0-9]+', '_', title.lower())[:40].strip('_')
    filename = f"{year}_{filename_title}.md"
    
    with open(os.path.join(pub_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"collection: publications\n")
        f.write(f"permalink: /publication/{year}-{filename_title}\n")
        f.write(f"date: {year}-01-01\n")
        f.write(f"venue: '{journal}'\n")
        f.write(f"---\n\n")
        f.write(f"**Authors:** {authors}<br>\n")
        f.write(f"**Title:** {title}<br>\n")
        f.write(f"**Year:** {year}<br>\n")
        f.write(f"**Journal/Venue:** {journal}\n")

print("Done generating publications.")
