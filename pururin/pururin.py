import requests
import json

BASE_URL = 'https://scathach.redsplit.org/v4/pururin/'


class Client(object):
    """
    A class used to represent a doujin.

    """
    @staticmethod
    def better_object(parser):
        """Converts the json object to a more readable object.

        Parameters
        ----------
        parser : dict
            The json object.

        """
        return json.dumps(parser, sort_keys=True, indent=4)

    @staticmethod
    def auto_space(string):
        """Automatically adds spaces for GET requests

        Parameters
        ----------
        string : str
            The string to be formatted.

        """

        return string.replace(' ', '+')

    def __init__(self, api_key: str = ''):
        """Initializes the client.

        Parameters
        ----------
        api_key : str
            scathach.dev API key (optional)

        """
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}

    def get_book(self, book: int):
        """Get doujin API from Id

        path: https://pururin.to/gallery/61119

        Parameters
        ----------
        book : int
            The id number of the doujin.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific id response.
        """

        self.specs['g'] = book

        # handle if book not int, then throw error
        try:
            book = int(book)
        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(BASE_URL, params=self.specs)
        if data.json()['type'] is None:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_newest(self, query: str):
        """Search for doujin based on newest 

        path: https://pururin.to/search/most-popular?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "newest"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_most_popular(self, query: str):
        """Search doujins by most popular

        path: https://pururin.to/search/most-popular?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "most-popular"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_highest_rated(self, query: str):
        """Search for doujin based on the highest rated

        path: https://pururin.to/search/highest-rated?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "highest-rated"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_most_viewed(self, query: str):
        """Search for doujin based on the most viewed

        path: https://pururin.to/search/most-viewed?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "most-viewed"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_title(self, query: str):
        """Search for doujin based on title

        path: https://pururin.to/search/title?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "title"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def search_by_random(self, query: str):
        """Search for doujin based on random

        path: https://pururin.to/search/random?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "random"
        query = Client.auto_space(query)

        if query is '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Client.better_object(data.json())

    def get_random(self):
        """Gets random doujin on pururin

        Returns
        -------
        dict
            The book object that represents the doujin response.
        """
        data = requests.get(BASE_URL + 'random' + '/', params=self.specs)

        return Client.better_object(data.json())

    def get_random_with_query(self, query: str):
        """Gets doujin on pururin by query

        path: https://pururin.to/search?q=alter

        Parameters
        ----------
        query : str
            The query to search for.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the doujin response.
        """

        self.specs['p'] = query
        query = Client.auto_space(query)
        data = requests.get(BASE_URL + 'search.php', params=self.specs)

        # if result null, then throw error
        if data.json()['type'] is None:
            raise ValueError('No results found')

        return Client.better_object(data.json())

