import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/about"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all FAQ questions (h3 headings)
questions = soup.find_all('h3')

print(f"Found {len(questions)} FAQ questions:\n")
for i, q in enumerate(questions, 1):
    question_text = q.get_text().strip()
    
    # Try to find the answer (next sibling paragraphs or list items)
    answer_parts = []
    next_elem = q.find_next_sibling()
    
    while next_elem and next_elem.name not in ['h3', 'h2', 'h1']:
        if next_elem.name == 'p':
            text = next_elem.get_text().strip()
            if text:
                answer_parts.append(text)
        elif next_elem.name == 'ul':
            for li in next_elem.find_all('li'):
                text = li.get_text().strip()
                if text:
                    answer_parts.append(f"- {text}")
        next_elem = next_elem.find_next_sibling()
    
    print(f"{i}. {question_text}")
    if answer_parts:
        for part in answer_parts:
            print(f"   {part}")
    print()
