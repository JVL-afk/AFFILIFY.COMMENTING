import asyncio
from TikTokApi import TikTokApi

async def inspect():
    api = TikTokApi()
    await api.create_sessions(num_sessions=1, headless=True, browser='chromium')
    print(f"API instance: {api}")
    print(f"API dir: {dir(api)}")
    if hasattr(api, 'search'):
        print(f"API search: {api.search}")
        print(f"API search dir: {dir(api.search)}")
    
    # Try to search
    try:
        async for video in api.search.videos("test", count=1):
            print(f"Found video: {video}")
    except Exception as e:
        print(f"Search failed: {e}")

if __name__ == "__main__":
    asyncio.run(inspect())
