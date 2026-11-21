import arxiv

# Create the Arxiv client
client = arxiv.Client()

# Search arXiv
search = arxiv.Search(
    query="large language models",
    max_results=2,
    sort_by=arxiv.SortCriterion.Relevance
)

# Fetch papers
for i, paper in enumerate(client.results(search), start=1):
    print(f"\nResult {i}")
    print("Title:", paper.title)
    print("Authors:", ", ".join(author.name for author in paper.authors))
    print("Summary:", paper.summary[:500])
    print("URL:", paper.entry_id)