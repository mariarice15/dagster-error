"""Source that load github issues, pull requests and reactions for a specific repository via customizable graphql query. Loads events incrementally."""

import dlt
from typing import Optional, Sequence
from dlt.sources import DltResource
from .helpers import get_github_issues

@dlt.source 
def github_data(
    owner: str,
    name: str,
    access_token: str = dlt.secrets.value,
) -> Sequence[DltResource]:
    return(
        dlt.resource(
            get_github_issues(
                owner,
                name,
                access_token,
            ),
            name="issues",
            write_disposition="replace",
        )
    )


