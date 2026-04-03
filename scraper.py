def scrape_reviews(url):
    print("Using sample reviews (fallback mode)...")

    return [
        {
            "text": "The product quality is really good and I am satisfied.",
            "rating": 5,
            "author": "User1"
        },
        {
            "text": "Not worth the price. Very poor performance.",
            "rating": 2,
            "author": "User2"
        },
        {
            "text": "Average experience. It works fine but nothing special.",
            "rating": 3,
            "author": "User3"
        },
        {
            "text": "Excellent build quality and fast delivery.",
            "rating": 5,
            "author": "User4"
        },
        {
            "text": "Bad packaging and delayed shipping.",
            "rating": 1,
            "author": "User5"
        }
    ]