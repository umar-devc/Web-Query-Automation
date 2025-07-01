from googlesearch import search
import random
import time
import requests

"""This script retrieves all queries from a file and performs a web search for each query."""

def get_querylist():
    """Retrieve all queries from the query.txt file as a list."""
    with open("query.txt", 'r') as file:
        return [line.strip() for line in file if line.strip()]

def web_search(query):
    """
    Perform a web search using the provided query.
    Returns a list of URLs found in the search results.
    """
    links = []
    num_results = 10  # Adjust the number of results as needed

    print(f"Searching for: {query}")
    print(f"Number of results to fetch: {num_results}")
    try:
        for idx, url in enumerate(search(query, num_results=num_results), 1):
            links.append(url)
            print(f"[{idx}/{num_results}] {url}")  
            time.sleep(random.uniform(1, 3))      # Random delay between 1 and 3 seconds
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred during the search: {http_err}")
    except Exception as e:
        print(f"An error occurred during the search: {e}")
    finally:
        print(f"Search completed.\nFound {len(links)} links.")
        with open("links.txt", "a") as f:
            for link in links:
                f.write(link + "\n")

if __name__ == "__main__":
    queries = get_querylist()
    if queries:
        for query in queries:
            web_search(query)
    else:
        print("No queries found in query.txt")