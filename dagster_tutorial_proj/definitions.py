from dagster import Definitions

from .assets import dagster_github_assets, dlt_resource

defs = Definitions(
    assets=[
        dagster_github_assets,
    ],
    resources={
        "dlt": dlt_resource,
    },
)