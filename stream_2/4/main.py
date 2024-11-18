import requests
import re

# URL
url = "https://www.lejobadequat.com/emplois"

# Header_User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    # HTML- responce for URL/ Website
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Page successfully retrieved!")
        html_content = response.text

        # Pattern for job-titles
        job_titles = re.findall(r'<div class="job_secteur_title">(.*?)</div>', html_content)

        # Clean results  (f.e. `<wbr>`-Tags clean up)
        job_titles = [title.replace("<wbr>", "").replace("</wbr>", "").strip() for title in job_titles]

        # Job titles output
        print("Job titles found:")
        print(job_titles)
    else:
        print(f"Error when retrieving the page. Statuscode: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"There was a problem with the request: {e}")
for job in job_titles:
    print(job)