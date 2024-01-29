from flask import Flask
import aiohttp
import asyncio
import json

app = Flask(__name__)

BASE_URL = "https://takehome.io";

api_extensions = ["twitter", "facebook", "instagram"]

@app.route("/")
async def social_network_activity():
    # TODO: your code here
    
    response = await fetch_all(api_extensions)

    return response;

async def fetch(s, url):
    '''
    Create an instance of aiohttp fetch to get a single endpoint.
    Exception handling also happens here on each individual isntance created.

    Parameters:
    -----------
    s: An aiohttp client session object
    url: The url extensions that we want to target 
    '''

    try:
        async with s.get(f'{BASE_URL}/{url}') as r:
            if r.status != 200:
                r.raise_for_status()
            return await r.text()
    except aiohttp.ClientResponseError as e:
        print('Response Error', str(e)) # A more in-depth logger would be implemented here
        return []
    except aiohttp.ClientConnectionError as e:
        print('Connection Error', str(e)) # A more in-depth logger would be implemented here
        return []

async def fetch_all(urls):
    '''
    Create a task for each API enpoint and call them concurrently 
    using asyncio.gather()

    Parameters:
    -----------
    urls: The url extensions that we want to target 
    '''
    async with aiohttp.ClientSession() as session:
        api_responses = []
        for url in urls:
            res = asyncio.create_task(fetch(session, url))
            api_responses.append(res)
        res = await asyncio.gather(*api_responses)
        
    return get_aggregate_data(urls, res)

def get_aggregate_data(urls, api_responses):
    '''
    Take the urls and API responses and combine them to produce 
    a count of responses per URL.

    Parameters:
    -----------
    urls: The url extensions that we are using
    api_responses: The responses that we want to combine with their original URL
    '''

    res = {}

    for url in urls:
        if(api_responses[urls.index(url)] != []): 
            res[url] = len(json.loads(api_responses[urls.index(url)]))
        else:
            res[url] = 0

    return res