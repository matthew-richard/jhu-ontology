import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as myfile:
    data = myfile.read()

soup = BeautifulSoup(data, 'lxml-xml')

# Run `python -i load_file.py jhu-0.xml` to open a shell with jhu-0.xml
# already loaded into the `soup` variable.

# Try this: 

# for desc in soup.find_all('Description'):
#     print(desc.find('foaf:name').string)
