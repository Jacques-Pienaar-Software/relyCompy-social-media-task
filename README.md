# **RelyComply Social Media Coding Task Solution**

#### Problem

Our client, Morgain Stainley, needs an API with live data on the activity levels of different social networks to serve as an input to their AI trading bots. Specifically, they need an endpoint they can query to get a numeric indicator of the amount of content posted on each social network. This should be a quick little task, but the client is paying us a billion dollars so your implementation needs to be robust and fast.

#### Solution

I chose to implement the async flask library with asyncio and aiohttp to ensure that the API calls can be made concurrently.
Then I added the necessary functions to call the various API's while keeping in mind that the list of API's being called might
expand over time.

(If a separate endpoint will be called there will only be minor refactoring done to meet the need).

#### Quickstart

```
pip install -r requirements.txt
flask --debug run
```
