import requests
username = 'gledson'
token = '8e7efdf02b09380764f7288229ad51478f60f1bc'

response = requests.get(
  'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
      username=username
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('CPU quota info:')
  print(response.content)
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))