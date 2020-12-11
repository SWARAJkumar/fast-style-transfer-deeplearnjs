import webbrowser

url = 'https://reiinakano.com/fast-style-transfer-deeplearnjs/'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)

print("Opening Demo")