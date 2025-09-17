import json
import random
import time
class Paper:
    """Represents a research paper."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Paper(Title='{self.title}', Author='{self.author}')"
def generate_dataset(size=100000):
    """Generates a large list of random research paper data and saves it to a JSON file."""
    papers = []
    for i in range(size):
        papers.append({
            "title": f"Research Paper on Topic {i:06d}",
            "author": f"Author Name {i:06d}"
        })
    with open("papers.json", "w") as f:
        json.dump(papers, f, indent=4)
    print(f"Generated a dataset of {size} papers and saved to papers.json.")
    return papers
def load_data(file_path="papers.json"):
    """Loads paper data from a JSON file."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return [Paper(d['title'], d['author']) for d in data]
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Generating a new dataset.")
        return [Paper(d['title'], d['author']) for d in generate_dataset()]
# --- Search Algorithms ---
def linear_search(papers, keyword):
    """Performs a linear search for a keyword in titles and authors."""
    matches = []
    keyword_lower = keyword.lower()
    for paper in papers:
        if keyword_lower in paper.title.lower() or keyword_lower in paper.author.lower():
            matches.append(paper)
    return matches

def binary_search(sorted_papers, keyword):
    """
    Performs a binary search on a sorted list of papers by title.
    Note: This is a simplified version and works best for exact title matches.
    """
    matches = []
    keyword_lower = keyword.lower()
    
    # Find a potential match using a standard binary search
    low, high = 0, len(sorted_papers) - 1
    found_index = -1
    while low <= high:
        mid = (low + high) // 2
        mid_title_lower = sorted_papers[mid].title.lower()
        if mid_title_lower == keyword_lower:
            found_index = mid
            break
        elif mid_title_lower < keyword_lower:
            low = mid + 1
        else:
            high = mid - 1
    
    if found_index != -1:
        # Check for all papers with the exact same title
        # Look backwards
        i = found_index
        while i >= 0 and sorted_papers[i].title.lower() == keyword_lower:
            matches.append(sorted_papers[i])
            i -= 1
        # Look forwards
        j = found_index + 1
        while j < len(sorted_papers) and sorted_papers[j].title.lower() == keyword_lower:
            matches.append(sorted_papers[j])
            j += 1
            
    return matches

def build_hash_tables(papers):
    """Builds hash-based data structures for quick lookups."""
    title_map = {}
    author_map = {}
    
    for paper in papers:
        if paper.title in title_map:
            title_map[paper.title].append(paper)
        else:
            title_map[paper.title] = [paper]
            
        if paper.author in author_map:
            author_map[paper.author].append(paper)
        else:
            author_map[paper.author] = [paper]
            
    return title_map, author_map

def hash_search(title_map, author_map, keyword):
    """Performs a hash-based search for exact matches."""
    matches = []
    if keyword in title_map:
        matches.extend(title_map[keyword])
    if keyword in author_map:
        # Use a set to avoid adding the same paper twice if it matches both
        unique_matches = set(matches)
        unique_matches.update(author_map[keyword])
        matches = list(unique_matches)
    return matches

# --- Main Program ---

if __name__ == "__main__":
    # Load or generate the dataset
    papers_list = load_data()
    
    # User input for search
    search_keyword = input("Enter a keyword (e.g., a title or author name): ")

    # --- Performance and Results Comparison ---
    print(f"\nSearching for '{search_keyword}' in a dataset of {len(papers_list)} papers...")

    # Linear Search
    start_time_linear = time.perf_counter()
    linear_results = linear_search(papers_list, search_keyword)
    end_time_linear = time.perf_counter()
    print(f"\nLinear Search: Found {len(linear_results)} matches in {end_time_linear - start_time_linear:.6f} seconds.")

    # Binary Search
    # Note: Binary search requires the data to be sorted first. This step is crucial.
    start_time_sort = time.perf_counter()
    sorted_papers = sorted(papers_list, key=lambda p: p.title.lower())
    end_time_sort = time.perf_counter()
    
    start_time_binary = time.perf_counter()
    binary_results = binary_search(sorted_papers, search_keyword)
    end_time_binary = time.perf_counter()
    
    print(f"Binary Search: Found {len(binary_results)} matches in {end_time_binary - start_time_binary:.6f} seconds.")
    print(f"  (Note: Initial sort took {end_time_sort - start_time_sort:.6f} seconds.)")

    # Hash-based Search
    start_time_hash_build = time.perf_counter()
    title_map, author_map = build_hash_tables(papers_list)
    end_time_hash_build = time.perf_counter()

    start_time_hash_search = time.perf_counter()
    hash_results = hash_search(title_map, author_map, search_keyword)
    end_time_hash_search = time.perf_counter()
    
    print(f"Hash-based Search: Found {len(hash_results)} matches in {end_time_hash_search - start_time_hash_search:.6f} seconds.")
    print(f"  (Note: Initial hash table build took {end_time_hash_build - start_time_hash_build:.6f} seconds.)")
    
    # Displaying Results (optional, as they can be very long)
    if linear_results:
        print("\n--- First 5 Matches ---")
        for i, paper in enumerate(linear_results[:5]):
            print(f"  {paper}")

















            