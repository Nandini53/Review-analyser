import pandas as pd
from scraper import scrape_reviews
from preprocess import clean_text
from llm import summarize_review
from utils import safe_api_call

# IMPORTANT: Use STATIC URL
URL = "https://webscraper.io/test-sites/e-commerce/static/product/545"

def main():
    print("🔍 Scraping reviews...")

    reviews = scrape_reviews(URL)

    if not reviews:
        print("❌ No reviews found! Check scraper.")
        return

    print(f"✅ Found {len(reviews)} reviews")

    processed_data = []

    for i, r in enumerate(reviews):
        print(f"Processing review {i+1}...")

        clean = clean_text(r["text"])
        summary = safe_api_call(summarize_review, clean)

        processed_data.append({
            "author": r["author"],
            "rating": r["rating"],
            "review": r["text"],
            "summary": summary
        })

    df = pd.DataFrame(processed_data)
    df.to_csv("reviews.csv", index=False)

    print("✅ Done! File saved as reviews.csv")

if __name__ == "__main__":
    main()