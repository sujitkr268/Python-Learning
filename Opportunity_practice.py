Oppt = [
    {"title": "Python Internship", "category": "internship"},
    {"title": "PayPal Hackathon", "category": "hackathon"},
    {"title": "Web Development Internship", "category": "internship"},
    {"title": "AI Competition", "category": "competition"}
]


def search_opportunities(search_term):
    result = []

    for items in Oppt:
        if (
            search_term in items["title"].lower()
            or search_term in items["category"].lower()
        ):
            result.append(items)

    return result


search_item = input("Enter your search: ").lower()

matches = search_opportunities(search_item)

sorted_matches = sorted(
    matches,
    key=lambda item: item["title"]
)

if sorted_matches:
    for item in sorted_matches:
        print(f"Title: {item['title']}")
        print(f"Category: {item['category']}")
        print("-" * 30)
else:
    print("Not found")
