import unittest
from unittest.mock import patch, MagicMock
from pubmed_fetcher import fetcher


class TestFetcher(unittest.TestCase):

    @patch("pubmed_fetcher.fetcher.Entrez.esearch")
    @patch("pubmed_fetcher.fetcher.Entrez.read")
    def test_search_pubmed(self, mock_read, mock_esearch):
        mock_esearch.return_value = MagicMock()
        mock_read.return_value = {"IdList": ["12345", "67890"]}

        result = fetcher.search_pubmed("cancer", max_results=2)
        self.assertEqual(result, ["12345", "67890"])
        mock_esearch.assert_called_once()
        mock_read.assert_called_once()

    @patch("pubmed_fetcher.fetcher.Entrez.efetch")
    @patch("pubmed_fetcher.fetcher.Entrez.read")
    def test_fetch_details(self, mock_read, mock_efetch):
        fake_article = {"PubmedArticle": [{"MedlineCitation": {"PMID": "123"}}]}
        mock_efetch.return_value = MagicMock()
        mock_read.return_value = fake_article

        result = fetcher.fetch_details(["123"])
        self.assertEqual(result, fake_article["PubmedArticle"])
        mock_efetch.assert_called_once()
        mock_read.assert_called_once()


if __name__ == "__main__":
    unittest.main()
