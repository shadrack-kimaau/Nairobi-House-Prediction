import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import html
import time
import random
from pathlib import Path
from fake_useragent import UserAgent

BASE_URL = "https://www.buyrentkenya.com/houses-for-rent"


def scrape_buyrentkenya(target_count=502):

    ua = UserAgent()
    session = requests.Session()
    all_properties = []
    page = 1

    # Property type keywords
    property_keywords = [
        "bungalow",
        "villa",
        "en suite",
        "bedsitter",
        "mansion",
        "apartment",
        "townhouse"
    ]

    while len(all_properties) < target_count:

        print(f"\nScraping page {page}...")

        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}?page={page}"

        headers = {
            "User-Agent": ua.random,
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Referer": BASE_URL
        }

        try:
            response = session.get(url, headers=headers, timeout=20)

            if response.status_code != 200:
                print(f"Stopped. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, "html.parser")
            listings = soup.find_all("a", {"data-cy": "listing-information-link"})

            if not listings:
                print("No listings found. Possibly blocked or end.")
                break

            for listing in listings:

                if len(all_properties) >= target_count:
                    break

                raw_click = listing.get("x-on:click.prevent")
                if not raw_click:
                    continue

                match = re.search(r"JSON\.parse\('(.*?)'\)", raw_click)
                if not match:
                    continue

                try:
                    json_string = html.unescape(match.group(1))
                    json_string = json_string.encode().decode("unicode_escape")
                    data = json.loads(json_string)
                    item = data.get("item", {})
                except:
                    continue

                # ======================
                # BASIC FIELDS
                # ======================
                location = f"{item.get('propertyCounty')} - {item.get('propertyArea')}"
                bedrooms = item.get("item_category3")
                price = item.get("itemPrice")

                # ----------------------
                # PROPERTY TYPE FROM TITLE
                # ----------------------
                title_text = item.get("item_title", "")
                title_lower = title_text.lower()

                property_type = "House"  # default

                for kw in property_keywords:
                    if kw in title_lower:
                        property_type = kw.title()
                        break

                # ----------------------
                # BATHROOMS
                # ----------------------
                parent = listing.find_parent("div")
                bathrooms = None

                if parent:
                    bath_tag = parent.find("span", {"data-cy": "card-bathroom_count"})
                    if bath_tag:
                        bath_match = re.search(r"\d+", bath_tag.get_text())
                        bathrooms = bath_match.group() if bath_match else None

                # =========================
                # DETAIL PAGE SCRAPING
                # =========================
                detail_url = listing.get("href")
                if not detail_url.startswith("http"):
                    detail_url = "https://www.buyrentkenya.com" + detail_url

                size = None
                listing_date = None
                amenities = []

                try:
                    time.sleep(random.uniform(1, 3))

                    detail_res = session.get(detail_url, headers=headers, timeout=20)
                    detail_soup = BeautifulSoup(detail_res.text, "html.parser")

                    # ---- Listing Date ----
                    date_tag = detail_soup.find(
                        "span",
                        string=re.compile("Created At")
                    )
                    if date_tag:
                        listing_date = (
                            date_tag.get_text(strip=True)
                            .replace("Created At:", "")
                            .strip()
                        )

                    # ---- Size ----
                    size_tag = detail_soup.find("span", string=re.compile("m²"))
                    if size_tag:
                        size = size_tag.get_text(strip=True)

                    # ---- Amenities ----
                    amenity_spans = detail_soup.select("div.flex.flex-wrap.gap-3 span")
                    for span in amenity_spans:
                        text = span.get_text(strip=True)
                        if text:
                            amenities.append(text)

                except Exception as e:
                    print("Detail scrape failed:", e)

                all_properties.append({
                    "Location": location,
                    "Property Type": property_type,
                    "Bedrooms": bedrooms,
                    "Bathrooms": bathrooms,
                    "Size": size,
                    "Price (KES)": price,
                    "Listing Date": listing_date,
                    "Amenities": ", ".join(amenities)
                })

                print(f"Collected: {len(all_properties)}")

                time.sleep(random.uniform(2, 6))

            sleep_time = random.uniform(5, 10)
            print(f"Sleeping {round(sleep_time,2)} seconds before next page...")
            time.sleep(sleep_time)

            page += 1

        except Exception as e:
            print("Error occurred:", e)
            break

    return pd.DataFrame(all_properties)


def save_raw_data(df):

    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / "data" / "raw"
    raw_path.mkdir(parents=True, exist_ok=True)

    file_path = raw_path / "raw_listings.csv"
    df.to_csv(file_path, index=False)

    print(f"\nSaved {len(df)} listings to:")
    print(file_path)


if __name__ == "__main__":
    df = scrape_buyrentkenya(target_count=502)
    save_raw_data(df)