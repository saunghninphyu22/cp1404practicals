import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    print("Welcome to Wikipedia search!")
    while True:
        search_phrase = input("Enter page title: ").strip()
        if not search_phrase:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_phrase)
            print(f"\n{page.title}\n{page.summary}\n{page.url}\n")
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
