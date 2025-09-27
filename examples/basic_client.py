#!/usr/bin/env python3
"""
Basic News MCP Client Example

This example demonstrates how to use the News MCP Server with the Python package.
"""

import os
import asyncio
import httpx
from typing import Dict, List, Any

class NewsMCPClient:
    """Simple client for News MCP Server."""

    def __init__(self, server_url: str = "http://localhost:3000", api_key: str = None):
        self.server_url = server_url
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    async def call_method(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Call an MCP method."""
        payload = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": method,
            "params": params
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.server_url}/mcp",
                json=payload,
                headers=self.headers,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()

    async def search_headlines(self, query: str, country: str = None, count: int = 10) -> List[Dict]:
        """Search for news headlines."""
        params = {
            "query_text": query,
            "count": count,
            "sort": "latest"
        }
        if country:
            params["country_code"] = country

        result = await self.call_method("news_headlines", params)
        return result.get("result", {}).get("items", [])

    async def search_briefs(self, query: str, country: str = None, count: int = 10) -> List[Dict]:
        """Search for news briefs with summaries."""
        params = {
            "query_text": query,
            "count": count,
            "sort": "latest"
        }
        if country:
            params["country_code"] = country

        result = await self.call_method("news_briefs", params)
        return result.get("result", {}).get("items", [])

    async def search_fulltext(self, query: str, country: str = None, count: int = 5) -> List[Dict]:
        """Search for full-text articles."""
        params = {
            "query_text": query,
            "count": count,
            "sort": "relevance"
        }
        if country:
            params["country_code"] = country

        result = await self.call_method("news_fulltext", params)
        return result.get("result", {}).get("items", [])


async def main():
    """Main example function."""
    # Initialize client
    server_url = os.getenv("NEWS_MCP_SERVER_URL", "http://localhost:3000")
    api_key = os.getenv("NEWS_MCP_API_KEY")

    client = NewsMCPClient(server_url, api_key)

    print("🌍 News MCP Server - Basic Client Example")
    print("=" * 50)

    try:
        # Example 1: Search headlines
        print("\n📰 Latest AI Headlines:")
        headlines = await client.search_headlines("artificial intelligence", count=5)

        for i, article in enumerate(headlines[:3], 1):
            print(f"\n{i}. {article.get('title', 'No title')}")
            print(f"   Source: {article.get('source', 'Unknown')}")
            print(f"   URL: {article.get('url', 'No URL')}")

        # Example 2: Search briefs with summaries
        print(f"\n📄 Climate Change News Briefs:")
        briefs = await client.search_briefs("climate change", count=3)

        for i, article in enumerate(briefs[:2], 1):
            print(f"\n{i}. {article.get('title', 'No title')}")
            print(f"   Summary: {article.get('description', 'No summary')[:100]}...")
            print(f"   Source: {article.get('source', 'Unknown')}")

        # Example 3: Search by country
        print(f"\n🇺🇸 US Technology News:")
        us_tech = await client.search_headlines("technology", country="US", count=3)

        for i, article in enumerate(us_tech[:2], 1):
            print(f"\n{i}. {article.get('title', 'No title')}")
            print(f"   Source: {article.get('source', 'Unknown')}")

        # Example 4: Full-text search
        print(f"\n📖 Full-Text Search - Electric Vehicles:")
        fulltext = await client.search_fulltext("electric vehicles", count=2)

        for i, article in enumerate(fulltext[:1], 1):
            print(f"\n{i}. {article.get('title', 'No title')}")
            content = article.get('content', 'No content')
            print(f"   Content preview: {content[:200]}...")
            print(f"   Word count: ~{len(content.split())} words")

    except httpx.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

    print(f"\n✅ Example completed!")


if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

    # Run the example
    asyncio.run(main())