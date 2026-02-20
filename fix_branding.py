
import os

path = r"c:\Users\AMD - ARCO\Downloads\site teste\index.html"
with open(path, 'rb') as f:
    content = f.read()

# Try to decode from various encodings to handle previous corruption
for enc in ['utf-8', 'utf-16', 'iso-8859-1']:
    try:
        text = content.decode(enc)
        break
    except:
        continue
else:
    # If all fail, try to just replace the broken byte sequences if it was mixed
    text = content.decode('utf-8', errors='replace')

# Replacements
replacements = {
    'CAMPONES GOOMER': 'Kefir Camponês',
    'Campones Goomer': 'Kefir Camponês',
    'CAMPONES<span> GOOMER</span>': 'KEFIR<span> CAMPONÊS</span>',
    'Kefir Campons': 'Kefir Camponês',
    'Kefir Campons': 'Kefir Camponês',
    'Campones': 'Camponês'
}

for old, new in replacements.items():
    text = text.replace(old, new)

# Also fix the weird characters from previous attempts
text = text.replace('Inovaǜo', 'Inovação').replace('Tradiǜo', 'Tradição')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Branding update completed successfully.")
