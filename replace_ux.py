import re

# Read bab2.tex
with open('bab/bab2.tex', 'r') as f:
    bab2 = f.read()

# Read UX.md
with open('update/UX.md', 'r') as f:
    ux = f.read()

def markdown_to_latex(text):
    # Convert *text* to \textit{text}
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    # Convert **text** to \textbf{text} ... Wait! 
    # If I run * first, ** becomes \textit{\textit{text}} or something.
    # Let's do ** first.
    return text

def convert_md(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    # Make sure we don't accidentally escape & that is already escaped
    # Wait, the user already wrote \& in UX.md. Let's just use the text.
    return text

# Extract sections from UX.md
# We can just extract them manually here in the script.
