import requests
from typing import Dict, List, Any


class Tools:
    def __init__(self):
        pass

    # Add your custom tools using pure Python code here, make sure to add type hints
    # Use Sphinx-style docstrings to document your tools, they will be used for generating tools specifications
    # Please refer to function_calling_filter_pipeline.py file from pipelines project for an example

    def query_wikidata(self, query: str) -> List[Dict[str, Any]]:
        """
        Query Wikidata using SPARQL and return the results.

        :param query: A SPARQL query string.
        """
        endpoint_url = "https://query.wikidata.org/sparql"

        try:
            response = requests.get(
                endpoint_url, params={"query": query, "format": "json"}
            )
            response.raise_for_status()  # Raise an exception for bad status codes

            data = response.json()

            results = []
            for binding in data["results"]["bindings"]:
                result = {}
                for var, value in binding.items():
                    result[var] = value["value"]
                results.append(result)

            return results

        except requests.RequestException as e:
            print(f"Error querying Wikidata: {str(e)}")
            return []
