import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "384870914958892",  # Step 1
    "access_token" : "EAAV4Xu5ATIsBAFXzWJKVoZCREX7H0ytTpWgmxUhUsU36VmPhLjuNv5SPnBCBHZBZCwFEZCdd7YHaKcyDBXrMPwBZBttZCFy8OgMg4G1pZC2LZADX7ZB0mZBiQBtgKlvB0H62RG0zlHOZCJ7ovoHsKaifTZBtUE7QLWXoo6jRO5zxD9LvFQZDZD"   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()