import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_paginated_results():
    driver = webdriver.Chrome()
    url = 'https://www.perlentaucher.de/stichwort/dystopien/buecher.html'
    driver.get(url)

    all_results = []
    max_pages = 5

    for page_num in range(1, max_pages + 1):
        try:

            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "book.teaser-block"))
            )

            books = driver.find_elements(By.CLASS_NAME, "book.teaser-block")
            for book in books:
                title_elem = book.find_element(By.TAG_NAME, "h3")
                title = title_elem.text
                link = title_elem.find_element(By.TAG_NAME, "a").get_attribute("href")
                all_results.append({"title": title, "url": link})

            # Finde the "Weiter"-Button
            pagination = driver.find_element(By.CLASS_NAME, "back-matter.box")
            next_button = pagination.find_element(By.XPATH, f"//a[text()='{page_num + 1}']")
            next_button.click()

        except Exception as e:
            print(f"Error on the page {page_num}: {e}")
            break

    driver.quit()
    return all_results

if __name__ == "__main__":
    results = scrape_paginated_results()
    for book in results:
        print(book)

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
def save_to_csv(results, filename='books.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for result in results:
            writer.writerow(result)

    print(f"Results in the {filename} saved.")

results = [
    {'title': 'Kai-Fu Lee / Qiufan Chen: KI 2041. Zehn Zukunftsvisionen',
     'url': 'https://www.perlentaucher.de/buch/kai-fu-lee-qiufan-chen/ki-2041.html'},
    {'title': 'Rudi Nuss: Die Realität kommt. Roman',
     'url': 'https://www.perlentaucher.de/buch/rudi-nuss/die-realitaet-kommt.html'},
    {'title': 'Kay Dick: Sie. Szenen des Unbehagens', 'url': 'https://www.perlentaucher.de/buch/kay-dick/sie.html'},
    {'title': 'Gerhard Roth: Die Imker. Roman', 'url': 'https://www.perlentaucher.de/buch/gerhard-roth/die-imker.html'},
    {'title': 'Herbert Genzmer: Liquid. Thriller',
     'url': 'https://www.perlentaucher.de/buch/herbert-genzmer/liquid.html'},
    {'title': 'Sibylle Berg: RCE. #RemoteCodeExecution. Roman',
     'url': 'https://www.perlentaucher.de/buch/sibylle-berg/rce.html'},
    {'title': 'Dmitry Glukhovsky: Outpost - Der Posten. Roman',
     'url': 'https://www.perlentaucher.de/buch/dmitry-glukhovsky/outpost-der-posten.html'},
    {'title': 'Femi Fadugba: The Upper World - Ein Hauch Zukunft. (Ab 14 Jahre)',
     'url': 'https://www.perlentaucher.de/buch/femi-fadugba/the-upper-world-ein-hauch-zukunft.html'},
    {'title': 'Paola Mendoza / Abby Sher: Sanctuary - Flucht in die Freiheit. (Ab 14 Jahre)',
     'url': 'https://www.perlentaucher.de/buch/paola-mendoza-abby-sher/sanctuary-flucht-in-die-freiheit.html'},
    {'title': 'Alain Damasio: Die Flüchtigen. Roman',
     'url': 'https://www.perlentaucher.de/buch/alain-damasio/die-fluechtigen.html'},
    {'title': 'Dave Eggers: Every . Roman', 'url': 'https://www.perlentaucher.de/buch/dave-eggers/every.html'},
    {'title': 'Dietmar Dath: Gentzen oder: Betrunken aufräumen. Ein Kalkülroman',
     'url': 'https://www.perlentaucher.de/buch/dietmar-dath/gentzen-oder-betrunken-aufraeumen.html'},
    {'title': 'Simon Stalenhag: Things from the Flood. Ein illustrierter Roman',
     'url': 'https://www.perlentaucher.de/buch/simon-stalenhag/things-from-the-flood.html'},
    {'title': 'Juliane Liebert: lieder an das große nichts. Gedichte',
     'url': 'https://www.perlentaucher.de/buch/juliane-liebert/lieder-an-das-grosse-nichts.html'},
    {'title': 'George Orwell: 1984. Roman',
     'url': 'https://www.perlentaucher.de/buch/george-orwell/1984-roman-2021.html'},
    {'title': 'Mary Shelley: Der letzte Mensch. Roman',
     'url': 'https://www.perlentaucher.de/buch/mary-shelley/der-letzte-mensch.html'},
    {'title': 'Raphaela Edelbauer: DAVE. Roman',
     'url': 'https://www.perlentaucher.de/buch/raphaela-edelbauer/dave.html'},
    {'title': 'Camilla Grubova: Das Alphabet der Puppen',
     'url': 'https://www.perlentaucher.de/buch/camilla-grubova/das-alphabet-der-puppen.html'},
    {'title': 'Martin Schäuble: Cleanland. (Ab 12 Jahre)',
     'url': 'https://www.perlentaucher.de/buch/martin-schaeuble/cleanland.html'},
    {'title': 'Marc-Uwe Kling: QualityLand 2.0. Kikis Geheimnis',
     'url': 'https://www.perlentaucher.de/buch/marc-uwe-kling/quality-land-2.html'},
    {'title': 'Laurel Snyder: Insel der Waisen. (Ab 12 Jahre)',
     'url': 'https://www.perlentaucher.de/buch/laurel-snyder/insel-der-waisen.html'},
    {'title': 'Karoline Georges: Totalbeton. Roman',
     'url': 'https://www.perlentaucher.de/buch/karoline-georges/totalbeton.html'},
    {'title': 'Zep: The End', 'url': 'https://www.perlentaucher.de/buch/zep/the-end.html'},
    {'title': 'Laura Lichtblau: Schwarzpulver. Roman',
     'url': 'https://www.perlentaucher.de/buch/laura-lichtblau/schwarzpulver.html'},
    {'title': 'Zoe Beck: Paradise City. Thriller',
     'url': 'https://www.perlentaucher.de/buch/zoe-beck/paradise-city.html'},
    {'title': 'Wolf Harlander: 42 Grad', 'url': 'https://www.perlentaucher.de/buch/wolf-harlander/42-grad.html'},
    {'title': 'Thomas Harding: Future History 2050',
     'url': 'https://www.perlentaucher.de/buch/thomas-harding/future-history-2050.html'},
    {'title': 'Katie Hale: Mein Name ist Monster. Roman',
     'url': 'https://www.perlentaucher.de/buch/katie-hale/mein-name-ist-monster.html'},
    {'title': 'Rob van Essen: Der gute Sohn',
     'url': 'https://www.perlentaucher.de/buch/rob-van-essen/der-gute-sohn.html'},
    {'title': 'William Sutcliffe: Wir sehen alles. Roman. (Ab 14 Jahre)',
     'url': 'https://www.perlentaucher.de/buch/william-sutcliffe/wir-sehen-alles.html'},
    {'title': 'Sandra Newman: Ice Cream Star. Roman',
     'url': 'https://www.perlentaucher.de/buch/sandra-newman/ice-cream-star.html'},
    {'title': 'Margaret Atwood: Die Zeuginnen. Roman',
     'url': 'https://www.perlentaucher.de/buch/margaret-atwood/die-zeuginnen.html'},
    {'title': 'E.M. Forster: Die Maschine steht still. 1 CD',
     'url': 'https://www.perlentaucher.de/buch/e-m-forster/die-maschine-steht-still.html'},
    {'title': 'Hendrik Otremba: Kachelbads Erbe. Roman',
     'url': 'https://www.perlentaucher.de/buch/hendrik-otremba/kachelbads-erbe.html'},
    {'title': 'Uwe Rasch / Gerhard Wagner: Aldous Huxley',
     'url': 'https://www.perlentaucher.de/buch/uwe-rasch-gerhard-wagner/aldous-huxley.html'},
    {'title': 'Vincent Perriot: Negalyod', 'url': 'https://www.perlentaucher.de/buch/vincent-perriot/negalyod.html'},
    {'title': 'Ryu Murakami: In Liebe, Dein Vaterland. Band 2: Der Untergang',
     'url': 'https://www.perlentaucher.de/buch/ryu-murakami/in-liebe-dein-vaterland-band-2.html'},
    {'title': 'Helene Bukowski: Milchzähne. Roman',
     'url': 'https://www.perlentaucher.de/buch/helene-bukowski/milchzaehne.html'},
    {'title': 'Martin Schneitewind: An den Mauern des Paradieses. Roman',
     'url': 'https://www.perlentaucher.de/buch/martin-schneitewind/an-den-mauern-des-paradieses.html'},
    {'title': 'Sibylle Berg: GRM. Brainfuck. Roman', 'url': 'https://www.perlentaucher.de/buch/sibylle-berg/grm.html'},
    {'title': 'Ryu Murakami: In Liebe, Dein Vaterland. Band 1: Die Invasion',
     'url': 'https://www.perlentaucher.de/buch/ryu-murakami/in-liebe-dein-vaterland-band-1.html'},
    {'title': 'Yoko Tawada: Sendbo-o-te. Roman',
     'url': 'https://www.perlentaucher.de/buch/yoko-tawada/sendbo-o-te.html'},
    {'title': 'Christian Dittloff: Das Weiße Schloss. Roman',
     'url': 'https://www.perlentaucher.de/buch/christian-dittloff/das-weisse-schloss.html'},
    {'title': 'Tijan Sila: Die Fahne der Wünsche. Roman',
     'url': 'https://www.perlentaucher.de/buch/tijan-sila/die-fahne-der-wuensche.html'},
    {'title': 'Eckhart Nickel: Hysteria. Roman',
     'url': 'https://www.perlentaucher.de/buch/eckhart-nickel/hysteria.html'},
    {'title': 'Max Annas: Finsterwalde. Roman', 'url': 'https://www.perlentaucher.de/buch/max-annas/finsterwalde.html'},
    {'title': 'Maja Lunde: Die Geschichte des Wassers. Roman',
     'url': 'https://www.perlentaucher.de/buch/maja-lunde/die-geschichte-des-wassers.html'},
    {'title': 'Juli Zeh: Leere Herzen. Roman', 'url': 'https://www.perlentaucher.de/buch/juli-zeh/leere-herzen.html'},
    {'title': 'E.M. Forster: Die Maschine steht still. Roman',
     'url': 'https://www.perlentaucher.de/buch/e-m-forster/die-maschine-steht-still-roman-2016.html'},
    {'title': 'Claire Vaye Watkins: Gold Ruhm Zitrus. Roman',
     'url': 'https://www.perlentaucher.de/buch/claire-vaye-watkins/gold-ruhm-zitrus.html'},
    {'title': 'Boualem Sansal: 2084. Das Ende der Welt',
     'url': 'https://www.perlentaucher.de/buch/boualem-sansal/2084.html'},
    {'title': 'Aldous Huxley: Schöne Neue Welt. Ein Roman der Zukunft',
     'url': 'https://www.perlentaucher.de/buch/aldous-huxley/schoene-neue-welt.html'},
    {'title': 'Anja Kümmel: Träume Digitaler Schläfer. Roman',
     'url': 'https://www.perlentaucher.de/buch/anja-kuemmel/traeume-digitaler-schlaefer.html'},
    {'title': 'Stephen King: Der Anschlag. Roman',
     'url': 'https://www.perlentaucher.de/buch/stephen-king/der-anschlag.html'},
    {'title': 'Jeanette Winterson: Die steinernen Götter. Roman',
     'url': 'https://www.perlentaucher.de/buch/jeanette-winterson/die-steinernen-goetter.html'},
    {'title': 'Helga Nowotny: Unersättliche Neugier. Innovation in einer fragilen Zukunft',
     'url': 'https://www.perlentaucher.de/buch/helga-nowotny/unersaettliche-neugier.html'},
    {'title': 'Michel Houellebecq: Elementarteilchen. Roman',
     'url': 'https://www.perlentaucher.de/buch/michel-houellebecq/elementarteilchen.html'},
]

# Save the results in CSV
save_to_csv(results)