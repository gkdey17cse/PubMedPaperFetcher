import re


def is_non_academic(affiliation: str) -> bool:
    """Return True if affiliation likely belongs to a non-academic (industry) organization."""
    aff_lower = affiliation.lower()

    academic_keywords = [
        "university",
        "institute",
        "hospital",
        "school",
        "center",
        "college",
        "dept",
        "department",
        "faculty",
        "lab",
        "research foundation",
    ]

    industry_keywords = [
        "inc",
        "ltd",
        "gmbh",
        "corp",
        "co.",
        "pharma",
        "biotech",
        "biosciences",
        "therapeutics",
        "diagnostics",
        "research labs",
        "solutions",
        "healthcare",
        "life sciences",
    ]

    # If any academic keyword found → reject
    if any(word in aff_lower for word in academic_keywords):
        return False

    # If any industry keyword found → accept
    if any(word in aff_lower for word in industry_keywords):
        return True

    # Otherwise, unsure → reject conservatively
    return False
