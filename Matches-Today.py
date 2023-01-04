import os
try:
  import requests
  from bs4 import BeautifulSoup
  from sty import fg, bg, ef, rs
  import colorama
  import random
  import time
except ImportError:
  print("Installing requirements to run.".capitalize)
  lis = ('requests', 'bs4', 'sty', 'colorama', 'random')
  for i in lis:
    os.system(f'py -m pip install {i}')

print(fg(0, 255, 51) + "'~ This Code Was Made By xMRV001" + fg.rs)
time.sleep(1.5)

colors = list(vars(colorama.Fore).values())

print(fg.red + 'Here all The matches of today : ' + '\n' + fg.rs)
url = "https://www.goal.com/en/live-scores"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

news = requests.get(url, headers=headers)

soup = BeautifulSoup(news.text, 'html.parser')

one = soup.find_all('div', class_='match-row status-fix')

for i in one:
    z = i.text
    x = z.replace('   0        ', '  >>  ')
    cleaned = x.replace('          ', '\n')
    colored_lines = [random.choice(colors) + line for line in cleaned.split('\n')]
    print('\n' .join(colored_lines))
    print('-' * 40)
