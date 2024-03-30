import json
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


response = requests.get("https://brain.overment.com")
soup = BeautifulSoup(response.text, "html.parser")
result = str(soup.find("main"))
markdown = md(result)

url_pattern = r"(http|https):\/\/[^\s]+|\.\/[^\s]+"

formatted = re.sub(url_pattern, "[url]", markdown)

with open("12_web/python_docs.json", "w") as f:
    json.dump(formatted, f)
