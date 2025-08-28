import datetime
import json

import pytz
import requests
from typing import Optional, Dict

from requests import Response


class ApiClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: int = 1):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()

        # Set default headers
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
        self.session.headers.update({'Content-Type': 'application/json'})

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make HTTP request with retry logic"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        separator = "===================================================================="

        print(f"\n{separator}")
        print(f"LOG:")
        print(f"{datetime.datetime.now(tz=pytz.utc)} Sending {method} request to endpoint: {url}")
        request_body = kwargs.get('json') if kwargs.get('json') else None
        if request_body:
            request_body = json.dumps(request_body, indent=4)
        print(f"{datetime.datetime.now(tz=pytz.utc)} Request data: {request_body}")
        response = self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            **kwargs
        )
        print(f"{datetime.datetime.now(tz=pytz.utc)} Response code: {response.status_code}")
        response_content = response.content if response.content else None
        if response_content:
            parsed = json.loads(response_content)
            response_content = json.dumps(parsed, indent=4)
        print(f"{datetime.datetime.now(tz=pytz.utc)} Response content: {response_content}")
        return response


    def get(self, endpoint: str, params: Optional[Dict] = None) -> Response:
        """GET request"""
        response = self._request('GET', endpoint, params=params)
        return response

    def post(self, endpoint: str, request_data: Optional[Dict] = None) -> Response:
        """POST request"""
        response = self._request('POST', endpoint, json=request_data)
        return response

    def put(self, endpoint: str, request_data: Optional[Dict] = None) -> Response:
        """PUT request"""
        response = self._request('PUT', endpoint, json=request_data)
        return response

    def delete(self, endpoint: str) -> bool:
        """DELETE request"""
        response = self._request('DELETE', endpoint)
        return response.status_code == 204