class Validators:
    @staticmethod
    def is_valid_tweet_length(text, max_length=280):
        return len(text) <= max_length
