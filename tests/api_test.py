import pytest
import random
import string
from pages.api_page import ApiPage

class TestBookStoreApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_page = ApiPage()
        self.test_user = {
            "userName": f"testUser{''.join(random.choices(string.ascii_letters, k=5))}",
            "password": "Test123!"
        }

    @pytest.fixture
    def authenticated_user(self):
        # Create new user
        create_response = self.api_page.create_user(
            self.test_user["userName"],
            self.test_user["password"]
        )
        
        # Generate token
        token_response = self.api_page.generate_token(
            self.test_user["userName"],
            self.test_user["password"]
        )
        
        yield  # This allows the test to run
        
        # Cleanup after test
        try:
            self.api_page.delete_user(self.api_page.user_id)
        except:
            pass

    def test_1_create_new_user(self):
        response = self.api_page.create_user(
            self.test_user["userName"],
            self.test_user["password"]
        )
        assert response.status_code == 201
        assert "userID" in response.json()
        assert response.json()["username"] == self.test_user["userName"]

    def test_2_generate_token(self):
        response = self.api_page.generate_token(
            self.test_user["userName"],
            self.test_user["password"]
        )
        assert response.status_code == 200
        assert "token" in response.json()
        assert "status" in response.json()
        assert "result" in response.json()

    def test_3_authorize_user(self, authenticated_user):
        response = self.api_page.authorize_user(
            self.test_user["userName"],
            self.test_user["password"]
        )
        assert response.status_code == 200

    def test_4_get_user_details(self, authenticated_user):
        response = self.api_page.get_user_details(self.api_page.user_id)
        assert response.status_code == 200
        assert "userId" in response.json()
        assert response.json()["username"] == self.test_user["userName"]
        assert "books" in response.json()

    def test_5_delete_user(self, authenticated_user):
        response = self.api_page.delete_user(self.api_page.user_id)
        assert response.status_code == 204

    def test_6_invalid_login(self):
        response = self.api_page.authorize_user("invalidUser", "invalidPass")
        assert response.status_code == 404
