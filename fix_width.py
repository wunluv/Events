import re

with open('Mabon/index.html', 'r') as f:
    content = f.read()

content = content.replace('<div class="mt-10">', '<div class="mt-10 max-w-3xl">')

with open('Mabon/index.html', 'w') as f:
    f.write(content)
