import re
import sys

def remove_textbf(text):
    result = []
    i = 0
    while i < len(text):
        if text.startswith('\\textbf{', i):
            i += 8 # len('\textbf{')
            brace_count = 1
            content_start = i
            while i < len(text) and brace_count > 0:
                if text[i] == '{':
                    brace_count += 1
                elif text[i] == '}':
                    brace_count -= 1
                i += 1
            content_end = i - 1
            # Recurse on the extracted content just in case there's nested \textbf
            content = text[content_start:content_end]
            result.append(remove_textbf(content))
        else:
            result.append(text[i])
            i += 1
    return "".join(result)

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = remove_textbf(content)
    
    # Also replace \bfseries
    new_content = re.sub(r'\\bfseries\s+', '', new_content)
    new_content = new_content.replace('\\bfseries', '')
    
    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

process_file('bab/bab1.tex')
process_file('bab/bab2.tex')
