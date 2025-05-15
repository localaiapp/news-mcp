from setuptools import setup, find_packages

setup(
    name="fakenews",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "httpx>=0.28.1",
        "mcp[cli]>=1.6.0",
        "uvicorn",
    ],
    entry_points={
        "console_scripts": [
            "mcp-fakenews=mcp_fakenews.fakenews_detect:mcp.run",
        ],
    },
) 