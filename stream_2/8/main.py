import json
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def save_to_db(data):
    # Connect to SQLite
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    # Create_the_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        url TEXT NOT NULL
    )
    """)

    # Add_results
    for job in data:
        cursor.execute("INSERT INTO jobs (title, url) VALUES (?, ?)", (job["title"], job["url"]))

    # Save_and _close
    conn.commit()
    conn.close()
    print("Data saved in the database!")


# Parse_the_jobs
def parse():
    driver = webdriver.Chrome()
    max_page = 2
    wait = WebDriverWait(driver, 10)
    result = []

    for page in range(1, max_page + 1):
        driver.get(f'https://jobs.marksandspencer.com/job-search?page={page}')

        # Wait_the job elements loaded
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ais-Hits-item')))


        jobs = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')

        for job in jobs:
            # Title
            title_element = job.find_element(By.CLASS_NAME, 'text-2xl.bold.mb-16')
            title = title_element.text

            # Link
            link_element = job.find_element(By.CLASS_NAME, 'c-btn.c-btn--primary')
            relative_url = link_element.get_attribute('href')
            full_url = f'https://jobs.marksandspencer.com{relative_url}' if relative_url.startswith(
                '/') else relative_url


            result.append({
                'title': title,
                'url': full_url
            })

    # Close_the Webdriver
    driver.quit()

    # Saved_JSON
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    # Save_DB
    save_to_db(result)

#DB_test
def read_from_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    for row in rows:
       print(row)

    conn.close()

read_from_db()

if __name__ == '__main__':
    parse()