import requests

class ApiActions:
    def __init__(self, base_url="https://demoqa.com"):
        self.base_url = base_url
        self.token = None
        
    def post_request(self, endpoint, payload, headers=None, allow_failures=True):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(
                url, 
                json=payload, 
                headers=headers,
                verify=False
            )
            return response
        except requests.exceptions.RequestException as e:
            if allow_failures:
                return type('Response', (), {'status_code': 404, 'text': str(e)})
            raise e

    def get_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def delete_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response

    def set_authorization_header(self, token):
        return {"Authorization": f"Bearer {token}"} 