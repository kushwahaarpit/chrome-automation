import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  // path of chrome
    URLS = {
        "stackoverflow.com",
        "gmail.com",
        "github.com",
        "google.com",
        "youtube.com"
    }
    for url in URLS:
        print("opening : "+ url)
        wb.get(chrome_path).open(url)

webauto()
