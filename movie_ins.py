class MovieIns:
    def __init__(self, title, release_year, ticket_price, stars_rating):
        self.title = title
        self.release_year = release_year
        self.ticket_price = ticket_price
        self.stars_rating = stars_rating

    def __str__(self):
        return f'title: {self.title} release_year: {self.release_year} ' \
               f'ticket_price: {self.stars_rating} stars_rating: {self.stars_rating}'