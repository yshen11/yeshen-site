import os, json, sys, requests, pathlib

API_KEY = os.environ.get("SERPAPI_API_KEY", "").strip()
AUTHOR_ID = os.environ.get("SCHOLAR_AUTHOR_ID", "c3IRn-EAAAAJ").strip()

OUT = pathlib.Path("assets/data/publications.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

def main():
    if not API_KEY:
        print("SERPAPI_API_KEY not set; skipping Scholar pull.", file=sys.stderr)
        return 0

    # SerpAPI Scholar Author endpoint
    # Docs: https://serpapi.com/google-scholar-author-api
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_scholar_author",
        "author_id": AUTHOR_ID,
        "api_key": API_KEY,
        "hl": "en",
        "num": "100"
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()

    pubs = []
    for pub in data.get("articles", []):
        pubs.append({
            "title": pub.get("title"),
            "authors": pub.get("authors"),
            "publication": pub.get("publication"),
            "year": pub.get("year"),
            "link": pub.get("link") or pub.get("result_id"),
            "citation_id": pub.get("result_id"),
        })

    if not pubs:
        print("No publications found from SerpAPI response; leaving file unchanged.", file=sys.stderr)
        return 0

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(pubs, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(pubs)} publications to {OUT}")

if __name__ == "__main__":
    sys.exit(main())