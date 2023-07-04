from .cards_object import CardsObject


class RandomSearch(CardsObject):
    """
    cards/random
    Get a single random card from a search query.

    Args:
        q (string):
            The query to search. 
        format (string, optional):
            Defaults to 'json'.
            Returns data in the specified method.
        face (string, optional):
            Defaults to empty string.
            If you're using the `image` format,
            this will specify if you want the front or back face.
        version (string, optional):
            Defaults to empty string.
            If you're using the `image` format, this will specify
            if you want the small, normal, large, etc version of the image.
        pretty (string, optional): 
            Defaults to empty string.
            Returns a prettier version of the json object. 
            Note that this may break functionality with Scrython.

    Returns:
        N/A

    Raises:
        Exception: If the object returned is an error.
        Exception: If the 'q' parameter is not provided.

    Examples:
        >>> card = scrython.cards.RandomSearch(q="t:creature mv=3")
        >>> card.card_name()
    """
    def __init__(self, **kwargs):
        if kwargs.get('q') is None:
          raise Exception('No query is specified')
        self.dict = {'q':kwargs.get('q'),}
        self.args = urllib.parse.urlencode(self.dict)
        self.url = 'cards/random?' + self.args
        super(RandomSearch, self).__init__(self.url)
