class Review:
    def __init__(self, review_id, text, rating, master, appointmen):
        self.review_id = review_id
        self.text = text
        self.rating = rating
        self.master = master
        self.appointment = appointmen



    def __eq__(self, other):
        if isinstance(other, Review):
            return(self.review_id == other.review_id and self.text == other.text and self.rating == other.rating)
        return False