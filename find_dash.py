import os

for root, _, files in os.walk('bab'):
    for file in files:
        if file.endswith('.tex'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.strip().startswith('%'):
                        continue
                    if '--' in line:
                        print(f"{filepath}:{i+1}: {line.strip()}")
