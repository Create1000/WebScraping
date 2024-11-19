import requests
import re
import json
import sqlite3
import csv


url = "https://www.lejobadequat.com/emplois"

# User-Agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    # Fetching the page content
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Page successfully retrieved!")
        html_content = response.text

        # Extract job titles
        job_titles = re.findall(r'<a .*?title="Consulter l\'offre d\'emploi (.*?)"', html_content)

        # Extract job links
        job_links = re.findall(r'<a href="(https://www\.lejobadequat\.com/emplois/.*?)"', html_content)

        if len(job_titles) == len(job_links):
            jobs = list(zip(job_titles, job_links))
            print("\nFound jobs:")
            for title, link in jobs:
                print(f"{title}: {link}")
        else:
            print("The number of job titles and links do not match!")
    else:
        print(f"Error while retrieving the page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")
#CSV
def write_csv(data: list) -> None:
    filename = 'output.csv'

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'url'])
        writer.writerows(data)

#JSON
def write_json(data: list) -> None:
    filename = 'output.json'

    data = [
        {
            'title': item[0],
            'url': item[1]
        }
        for item in data
    ]
    with open(filename, mode='w') as f:
        json.dump(data, f, indent=4)

#SQLite
# Save data to SQLite
def write_sql(data: list) -> None:
    filename = 'output.db'

    # 1. Create table
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Jobs_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT
        )
    """
    cursor.execute(sql)

    # 2. Insert data
    for idx, item in enumerate(data, start=1):
        cursor.execute("""
            INSERT INTO Jobs_table (title, url)
            VALUES (?, ?)
        """, (item[0], item[1]))

    # Commit and close the connection
    conn.commit()
    conn.close()
    print(f"Data successfully written to {filename}")


# Run the script
if __name__ == '__main__':
    # Example scraped data (replace with actual scraped results)
    jobs = [
        ("Technicien qualité H/F", "https://www.lejobadequat.com/emplois/261607-technicien-qualite-f-h-fr"),
        ("Opérateur de saisie H/F", "https://www.lejobadequat.com/emplois/261605-operateur-de-saisie-h-f-fr"),
        ("Chauffeur VL H/F", "https://www.lejobadequat.com/emplois/261604-chauffeur-vl-h-f-fr"),
        ("Employé libre service", "https://www.lejobadequat.com/emplois/261603-employe-libre-service-fr"),
        ("Plaquiste H/F", "https://www.lejobadequat.com/emplois/261602-plaquiste-h-f-fr"),
        ("Peintre H/F", "https://www.lejobadequat.com/emplois/261601-peintre-h-f-fr"),
        ("Magasinier / cariste H / F", "https: // www.lejobadequat.com / emplois / 261600 - magasinier - cariste - f - h - fr"),
        ("Inventoriste H / F", "https: // www.lejobadequat.com / emplois / 261599 - inventoriste - h - f - fr"),
        ("Grutier cabine H / F", "https: // www.lejobadequat.com / emplois / 261598 - grutier - cabine - h - f - fr"),
        ("Grutier H / F", "https: // www.lejobadequat.com / emplois / 261596 - grutier - f - h - fr"),
        ("Plombier H / F", "https: // www.lejobadequat.com / emplois / 261594 - plombier - f - h - fr"),
        ("Electricien bâtiment H / F", "https: // www.lejobadequat.com / emplois / 261593 - electricien - batiment - f - h - fr")
    ]

    #write_json(jobs)
    #write_sql(jobs)
    write_csv(jobs)