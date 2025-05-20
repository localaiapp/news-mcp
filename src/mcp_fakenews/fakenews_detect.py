from typing import Any
import httpx
import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("fakenews")

# Constants
FAKENEWS_API_BASE = "https://a.localaiapp.com"
USER_AGENT = "fakenews-app/1.0"

async def make_search_request(url: str, text: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = json.dumps({
        "text": text
    })
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, content=payload, timeout=30.0)
            
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        

@mcp.tool()
async def fakenews_detection(text: str) -> str:
    """Get fakenews detection

    Args:
        text: text you want to detect
    """
    
    url = FAKENEWS_API_BASE
      
    forecast_data = await make_search_request(url, text)
    
    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["root"]["children"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
Title: {period['fields']['title']}
URL: {period['fields']['url']}
Domain: {period['fields']['domain']}
Content: {period['fields']['content']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)


    # async with httpx.AsyncClient() as client:
    #     try:
    #         async with client.stream("GET", url, headers=headers, timeout=100) as response:
    #             response.raise_for_status()
    #             async for chunk in response.aiter_bytes():
    #                 yield chunk
    #     except Exception as e:
    #         print("error", e)

# async def main():
#     async for chunk in fakenews_detection("Democrats are calling to redesign the American Flag to make it more inclusive" by featuring rainbow colored stripes."):
#         print(chunk.decode('utf-8'))

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    # import asyncio
    # asyncio.run(main())

