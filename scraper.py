import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.unternehmensregister.de/ureg/result.html"
    session = requests.Session()

    # Beispiel-Anfrage (Achtung: URL ist meist Session-gebunden – echte Umsetzung braucht POST oder Formdatenhandling)
    response = session.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "lxml")

    entries = []

    for section in soup.find_all("div", class_="ergebnisliste"):
        lines = section.get_text(separator="\n").split("\n")
        lines = [line.strip() for line in lines if line.strip()]
        entries.append(lines)

    for i, entry in enumerate(entries):
        print(f"\n🔹 Eintrag {i+1}:")
        for line in entry:
            print("  ", line)

if __name__ == "__main__":
    main()
