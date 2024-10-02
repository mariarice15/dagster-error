import time 
from typing import Iterator, List, Optional
from dlt.common.typing import StrAny
from dlt.sources.helpers import requests


def _get_auth_header(access_token: Optional[str]) -> StrAny:
    if access_token:
        return {"Authorization": f"Bearer {access_token}"}
    else:
        # REST API works without access token (with high rate limits)
        return {}


def get_github_issues(owner: str, repo: str, access_token: Optional[str] = None) -> Iterator[List[StrAny]]:
    def _request(page_url: str) -> requests.Response:
        headers = _get_auth_header(access_token)
        headers.update({"Accept": "application/vnd.github.raw+json"})
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        return response

    next_page_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    while next_page_url:
        response = _request(next_page_url)
        issues = response.json()
        if issues:
            yield issues
        if 'next' in response.links:
            next_page_url = response.links['next']['url']
        else:
            break
        time.sleep(2)  # Sleep for 2 seconds to respect rate limits

    
