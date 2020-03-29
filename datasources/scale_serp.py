import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("SCALE_SERP_API")
base_params = {
  'api_key': os.getenv("SCALE_SERP_KEY"),
  'search_type': 'news'
}

def get_news(query):
  params = base_params
  params['q'] = query
  response = requests.get(base_url, params).json()
  if response['request_info']['success']:
    return response['news_results']
  return None