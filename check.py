import os, re

def check_headings(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    headings = []
    for i, line in enumerate(lines):
        m = re.match(r'^\s*\\(chapter|section|subsection|subsubsection)\{([^}]+)\}', line)
        if m:
            headings.append((i, m.group(1), m.group(2)))
            
    no_text_headings = []
    for i in range(len(headings) - 1):
        idx1, type1, title1 = headings[i]
        idx2, type2, title2 = headings[i+1]
        
        # Check if there is any text between idx1 and idx2
        has_text = False
        for j in range(idx1 + 1, idx2):
            line = lines[j].strip()
            # Ignore comments, labels, and empty lines
            if line and not line.startswith('%') and not line.startswith('\\label'):
                has_text = True
                break
        
        if not has_text:
            no_text_headings.append(f'{type1.capitalize()} "{title1}"')
            
    return no_text_headings

for root, dirs, files in os.walk(r'c:\Users\shafnats\Development\Book-FoodAIRescue - Copy\bab'):
    for file in files:
        if file.endswith('.tex'):
            path = os.path.join(root, file)
            res = check_headings(path)
            if res:
                print(f'File: {file}')
                for h in res:
                    print(f'  - {h}')
