from Bio import Entrez
from typing import List, Dict

# My valid email id
Entrez.email = "gour24035@iiitd.ac.in"


def search_pubmed(query: str, max_results: int = 50) -> List[str]:
    """Search PubMed and return a list of PubMed IDs."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    results = Entrez.read(handle)
    handle.close()
    return results["IdList"]


def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch full article details for given PubMed IDs."""
    if not pubmed_ids:
        return []

    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    return records["PubmedArticle"]
