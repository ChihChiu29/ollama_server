from httpx import ReadTimeout
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

import ollama

# Remember to start the server using the command line; using GUI sometimes makes the server undiscoverable on lan.
OLLAMA_HOST = '192.168.1.244:11434'

_CACHE = {}

def client():
  key = 'CLIENT'
  if key not in _CACHE:
    _CACHE[key] = ollama.Client(
      host=OLLAMA_HOST,
      timeout=30,
    )
  
  return _CACHE[key]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1), retry=retry_if_exception_type(ReadTimeout))
def quickchat(model: str, messages: list) -> str:
  response = client().chat(
    model=model,
    messages=messages,
  )
  return response['message']['content']
