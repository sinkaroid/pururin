import pururin
data = pururin.Client()

print(data.get_book(61119))
print(data.get_random())
print(data.get_random_with_query("tomoe gozen"))
print(data.search_by_highest_rated("jeanne alter"))
print(data.search_by_most_viewed("succubus"))
print(data.search_by_newest("gangbang"))
print(data.search_by_random("yuri"))
print(data.search_by_title("futanari"))