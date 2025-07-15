from typing import List, Dict, Any
from pubmed_fetcher.utils import is_non_academic


def extract_info(article: Dict[str, Any]) -> Dict[str, Any]:
    """Extract relevant fields from a PubMed article."""
    medline = article.get("MedlineCitation", {})
    article_data = medline.get("Article", {})
    pub_date = (
        article_data.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
    )
    authors = article_data.get("AuthorList", [])

    non_academic_authors = []
    company_affiliations = []
    corresponding_email = None

    for author in authors:
        name = " ".join(
            [author.get("ForeName", ""), author.get("LastName", "")]
        ).strip()
        affiliations = author.get("AffiliationInfo", [])
        for aff in affiliations:
            aff_text = aff.get("Affiliation", "")
            if is_non_academic(aff_text):
                non_academic_authors.append(name)
                company_affiliations.append(aff_text)
                if "@" in aff_text and not corresponding_email:
                    corresponding_email = extract_email(aff_text)

    return {
        "PubmedID": medline.get("PMID", ""),
        "Title": article_data.get("ArticleTitle", ""),
        "Publication Date": format_pub_date(pub_date),
        "Non-academic Author(s)": "; ".join(set(non_academic_authors)),
        "Company Affiliation(s)": "; ".join(set(company_affiliations)),
        "Corresponding Author Email": corresponding_email or "N/A",
    }


def format_pub_date(pub_date: Dict[str, str]) -> str:
    """Format publication date into YYYY-MM-DD or partial if missing."""
    year = pub_date.get("Year", "Unknown")
    month = pub_date.get("Month", "")
    day = pub_date.get("Day", "")
    return f"{year}-{month.zfill(2) if month else '01'}-{day.zfill(2) if day else '01'}"


def extract_email(text: str) -> str:
    """Extract email from a string using regex."""
    import re

    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None
