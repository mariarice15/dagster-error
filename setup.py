from setuptools import find_packages, setup

setup(
    name="dagster_tutorial_proj",
    packages=find_packages(exclude=["dagster_tutorial_proj_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster_embedded_elt",
        "dlt",
        "requests"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)