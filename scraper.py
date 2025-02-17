import requests, json, pdb

retries_code = [500, 502, 503, 504, 522, 524, 408, 429, 401, 403, 405, 307, 572, 573, 302]


def send_request(url: str, headers: dict={}, proxy: dict={}, retries=5):
  for i  in range(1, retries+1):
    print('*'*20, 'Sending request to', url , 'retry count ', i, '*'*20)
    proxy_dict = {'http': proxy, 'https': proxy}  or {}
    response = requests.get(url, headers=headers, proxies= proxy_dict)
    if response.status_code in retries_code:
      continue
    if response.status_code == '200':
      return None
    return response

source1_url = 'https://www.myfxbook.com/'
s1_response = send_request(source1_url)
print(s1_response)
s1_data = json.loads(s1_response.text) or {}
