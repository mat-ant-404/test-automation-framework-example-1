import json
from dataclasses import dataclass
from json import JSONDecodeError

import requests
from typing import Optional, Dict

from pydantic import BaseModel
from conftest import get_logger


class ApiClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: int = 1):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.success_status_codes = [200, 201, 204]

        # Set default headers
        if api_key:
            self.session.headers.update({'api_key': f'{api_key}'})
        self.session.headers.update({'Content-Type': 'application/json'})

    def _request(
            self,
            method: str,
            endpoint: str,
            **kwargs
    ) -> requests.Response:
        """Make HTTP request with retry logic"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        logger = get_logger()

        logger.info("=" * 50)
        logger.info("REQUEST BEGIN")
        logger.info("=" * 50)
        logger.info(f"Sending {method} request to endpoint: {url}")
        request_body = kwargs.get('json') if kwargs.get('json') else None
        request_headers = json.dumps(dict(self.session.headers), indent=4)
        logger.info(f"Request headers {request_headers}")
        if request_body:
            request_body = json.dumps(request_body, indent=4)
        logger.info(f"Request data: {request_body}")

        response = self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            **kwargs
        )

        logger.info("=" * 50)
        logger.info("REQUEST END")
        logger.info("=" * 50)
        logger.info("=" * 50)
        logger.info("RESPONSE START")
        logger.info("=" * 50)
        logger.info(f"Response code: {response.status_code}")
        response_content = response.content if response.content else None
        if response_content:
            try:
                parsed = json.loads(response_content)
                response_content = json.dumps(parsed, indent=4)
            except JSONDecodeError:
                pass
        logger.info(f"Response content: {response_content}")
        logger.info("=" * 50)
        logger.info("RESPONSE END")
        logger.info("=" * 50)

        return response

    def _process_response(
            self,
            response: requests.Response,
            response_model,
            response_error_model
    ) -> 'ResponseModel':
        response_http_code = response.status_code
        response_body = response.json()
        if response_http_code in self.success_status_codes:
            response_body = response_model(**response_body)
        else:
            response_body = response_error_model(**response_body)
        return ResponseModel(code=response_http_code, body=response_body)

    def get(
            self,
            endpoint: str,
            response_model: Optional[type[BaseModel]],
            response_error_model: Optional[type[BaseModel]],
            params: Optional[Dict] = None,
    ) -> 'ResponseModel':
        """GET request"""
        raw_response = self._request(
            method='GET',
            endpoint=endpoint,
            params=params)
        parsed_response = self._process_response(
            response=raw_response,
            response_model=response_model,
            response_error_model=response_error_model)
        return parsed_response

    def post(
            self,
            endpoint: str,
            response_model: Optional[type[BaseModel]],
            response_error_model: Optional[type[BaseModel]],
            request_data: Optional[BaseModel] = None
    ) -> 'ResponseModel':
        """POST request"""
        request_data = request_data.model_dump()
        raw_response = self._request(
            method='POST',
            endpoint=endpoint,
            json=request_data)
        parsed_response = self._process_response(
            response=raw_response,
            response_model=response_model,
            response_error_model=response_error_model)
        return parsed_response

    def put(self,
            endpoint: str,
            response_model: Optional[type[BaseModel]],
            response_error_model: Optional[type[BaseModel]],
            request_data: Optional[BaseModel] = None
            ) -> 'ResponseModel':
        """PUT request"""
        request_data = request_data.model_dump()
        raw_response = self._request(
            method='PUT',
            endpoint=endpoint,
            json=request_data)
        parsed_response = self._process_response(
            response=raw_response,
            response_model=response_model,
            response_error_model=response_error_model)
        return parsed_response


@dataclass
class ResponseModel:
    code: int
    body: BaseModel
