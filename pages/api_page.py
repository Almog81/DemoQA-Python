from utilities.api_actions import ApiActions

class ApiPage(ApiActions):
    def __init__(self):
        super().__init__()
        self.user_id = None

    def create_user(self, username, password):
        response = self.post_request(
            "/Account/v1/User",
            {"userName": username, "password": password}
        )
        if response.status_code == 201:
            self.user_id = response.json()["userID"]
        return response

    def generate_token(self, username, password):
        if not username or not password:
            raise ValueError("Username and password are required")
            
        response = self.post_request(
            "/Account/v1/GenerateToken",
            {"userName": username, "password": password}
        )
        if response.status_code == 200:
            self.token = response.json()["token"]
        return response

    def authorize_user(self, username, password):
        if not username or not password:
            raise ValueError("Username and password are required")
            
        return self.post_request(
            "/Account/v1/Authorized",
            {"userName": username, "password": password},
        )

    def get_user_details(self, user_id):
        if not self.token:
            raise ValueError("Token is required. Please generate token first")
        if not user_id:
            raise ValueError("User ID is required")
            
        headers = self.set_authorization_header(self.token)
        return self.get_request(
            f"/Account/v1/User/{user_id}",
            headers=headers
        )

    def delete_user(self, user_id):
        if not self.token:
            raise ValueError("Token is required. Please generate token first")
        if not user_id:
            raise ValueError("User ID is required")
            
        headers = self.set_authorization_header(self.token)
        return self.delete_request(
            f"/Account/v1/User/{user_id}",
            headers=headers
        ) 