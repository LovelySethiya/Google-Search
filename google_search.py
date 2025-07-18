from googlesearch import search

def simple_google_search(query):
    print(f"\n🔍 Search results for: {query}\n")
    results = search(query, num_results=10)
    for idx, link in enumerate(results, start=1):
        print(f"{idx}. {link}")

if __name__ == "__main__":
    user_query = input("Enter your Google search query: ")
    simple_google_search(user_query)
