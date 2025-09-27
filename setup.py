"""Setup script for news-mcp-server PyPI package."""

from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="news-mcp-server",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="AI-Ready Global News API & MCP Server for AI Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="News MCP Team",
    author_email="dev@newsmcp.com",
    url="https://github.com/yourorg/news-mcp-server",
    project_urls={
        "Documentation": "https://docs.newsmcp.com",
        "Source": "https://github.com/yourorg/news-mcp-server",
        "Tracker": "https://github.com/yourorg/news-mcp-server/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "httpx>=0.25.0",
        "pydantic>=2.4.0",
        "pydantic-settings>=2.0.0",
        "python-json-logger>=2.0.0",
        "anyio>=3.7.0",
        "click>=8.1.0",
    ],
    extras_require={
        "minimal": [],
        "full": [
            "redis>=5.0.0",
            "prometheus-client>=0.17.0",
            "psutil>=5.9.0",
        ],
        "frameworks": [
            "langchain>=0.1.0",
            "langchain-community>=0.0.10",
        ],
        "cloud": [
            "boto3>=1.26.0",
            "azure-identity>=1.12.0",
            "google-cloud-core>=2.3.0",
        ],
        "all": [
            "redis>=5.0.0",
            "prometheus-client>=0.17.0",
            "psutil>=5.9.0",
            "langchain>=0.1.0",
            "langchain-community>=0.0.10",
            "boto3>=1.26.0",
            "azure-identity>=1.12.0",
            "google-cloud-core>=2.3.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "news-mcp-server=news_mcp_server.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Text Processing :: Indexing",
        "Framework :: FastAPI",
        "Framework :: AsyncIO",
    ],
    keywords=[
        "news", "api", "mcp", "server", "ai", "agents", "llm", "langchain",
        "global news", "media monitoring", "real-time news", "news intelligence",
        "ai integration", "autonomous agents", "press monitor", "news search",
        "multilingual news", "news analysis", "media intelligence", "news data"
    ],
    license="MIT",
    zip_safe=False,
    include_package_data=True,
)