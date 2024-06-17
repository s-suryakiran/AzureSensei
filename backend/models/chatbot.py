class Query:
    def __init__(self, user_id: int, role: str, query: str):
        self.user_id = user_id
        self.role = role
        self.query = query