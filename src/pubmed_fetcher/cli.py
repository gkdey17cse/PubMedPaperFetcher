import argparse
from pubmed_fetcher.fetcher import search_pubmed, fetch_details
from pubmed_fetcher.parser import extract_info
from pubmed_fetcher.writer import write_csv

# run : poetry run get-papers-list "cancer therapy" -f result.csv -d

def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with company authors."
    )
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Filename to save output (CSV)")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output"
    )

    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] Running query:", args.query)

    # Step 1: Search PubMed
    pubmed_ids = search_pubmed(args.query)

    if args.debug:
        print(f"[DEBUG] Found {len(pubmed_ids)} articles.")

    # Step 2: Fetch article details
    articles = fetch_details(pubmed_ids)

    if args.debug:
        print(f"[DEBUG] Retrieved {len(articles)} full records.")

    # Step 3: Parse articles
    parsed = [extract_info(article) for article in articles]

    if args.file:
        write_csv(parsed, args.file)
    else:
        for record in parsed:
            print(record)
