import requests 
# from requests.exceptions import HTTPError
import re
import os

# try: 
    response = requests.get('https://raw.githubusercontent.com/lite-speed/src/index.html')
    response.raise_for_status()
    html = response.text
    components = re.findall('^<script src="/components/.\.js" defer></script>$', html)
    mainJsFileText = ""
    for component in components:
        response2 = requests.get("https://raw.githubusercontent.com/lite-speed/editor/src" + component.split('"')[1].split('"')[0])
        response2.raise_for_status()
        mainJsFileText += response2.text
    response3 = requests.get("https://raw.githubusercontent.com/lite-speed/editor/src/main.js")
    response3.raise_for_status()
    mainJsFileText += response3.text
    mainJsFileText = re.sub(r"\n", "", mainJsFile)
    os.system("curl -u " + os.getenv("USERNAME") + ":" + os.getenv("TOKEN") + "https://api.github.com/user")
    os.system('''curl \
                   -x PUT \
                   -H "Accept: application/vnd.github.v3+json" \
                   https://api.github.com/repos/lite-speed/editor/contents/dist/main.js \
                   -d {"message": "Auto build", "content": "'''+mainJsFileText)
               
        
"""
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
"""
