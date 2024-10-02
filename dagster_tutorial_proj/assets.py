import dlt
from dagster import AssetExecutionContext, AssetKey
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets, DagsterDltTranslator
from dlt_sources.github import github_data
from collections.abc import Iterable

dlt_resource = DagsterDltResource()

class CustomDagsterDltTranslator(DagsterDltTranslator):
    def get_asset_key(self, resource: DagsterDltResource) -> AssetKey:
        """Overrides asset key to be the dlt resource name."""
        return AssetKey(f"{resource.name}")

    def get_deps_asset_keys(self, resource: DagsterDltResource) -> Iterable[AssetKey]:
        """Overrides upstream asset key to be a single source asset."""
        return [AssetKey("common_upstream_dlt_dependency")]


@dlt_assets(
    name="bigquery",
    group_name="bigquery",
    dlt_source=github_data(
        "dagster-io", 
        "dagster"
        ),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="github_issues",
        dataset_name="github_issues_data",
        destination="bigquery",
        progress="log",
    ),
    dlt_dagster_translator=CustomDagsterDltTranslator(),
)
def dagster_github_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)