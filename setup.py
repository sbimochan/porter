from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="porter-sbimochan",  # Replace with your own username
    version="2.0.1",
    author="Bimochan shrestha",
    author_email="bmochan@gmail.com",
    description="Checks if your desired services are running or not.",
    long_description="""  # Porter

    Checks if your desired services are running or not. Default ports are used as an example here

    Contributions welcome for:

    - .env.example for port and message so that ports are not revealed in forks.
    - Exact finding strings instead of whitespaces


    """,
    long_description_content_type="text/markdown",
    url="https://github.com/sbimochan/porter",
    entry_points={
        "console_scripts": [
            "porter = porter:check_status"
        ]
    },
    python_requires='>=3.6',
)
