class ReviewRepository:
    def init(self):
        self.reviews = []

    def save_review(self, review):
        self.reviews.append(review)

    def find_review_by_id(self, review_id):
        for review in self.reviews:
            if review.review_id == review_id:
                return review
        return None