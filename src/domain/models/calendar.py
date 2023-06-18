class Calendar:

    def __init__(self, expiration):
        self.expiration = expiration

    def get_expiration(self):
        return self.expiration

    ## Implement a serialize method that returns this class as an object
    def serialize(self):
        return {
            'expiracao': self.expiration
        }

