import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, users_url):
  headers = {
      'Authorization': token
  }
  payload = {
      'long_url': users_url
  }
  url = 'https://api-ssl.bitly.com/v4/shorten'
  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()
  shortened_link = response.json()['link'] 
  return shortened_link


def count_clicks(token, bitlink):
  headers = {
      'Authorization': token
  }
  payload = {
      'unit': 'month',
      'units': '-1'
  }
  parsed_link = urlparse(bitlink)
  homemade_bitly = f'{parsed_link.netloc}{parsed_link.path}'
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{homemade_bitly}/clicks/summary'
  response = requests.get(url, headers=headers, params=payload)
  response.raise_for_status()
  counted_clicks = response.json()["total_clicks"] 
  return counted_clicks


def get_estimated_bitlink_info(token, user_url):
  headers = {
      'Authorization': token
  }
  parsed_link = urlparse(user_url)
  homemade_bitly = f'{parsed_link.netloc}{parsed_link.path}'
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{homemade_bitly}'
  response = requests.get(url, headers=headers)
  response.raise_for_status()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('link', help='Корректная, обычная или bitly, ссылка')
  args = parser.parse_args()
  load_dotenv()
  token = os.getenv('BITLY_TOKEN')
  user_url = args.link
  try:
    try:
      get_estimated_bitlink_info(token, user_url)
      clicks = count_clicks(token, user_url)
      print('Количество кликов по Вашей ссылке:', clicks)
    except requests.exceptions.HTTPError:
      bitly_link = shorten_link(token, user_url)
      print('Ваш битлинк:', bitly_link)
  except requests.exceptions.HTTPError:
    print('Проверьте Вашу ссылку, вероятно, она содержит ошибку')