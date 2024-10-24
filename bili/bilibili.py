import json
import requests


def read_cookies_file(filename):
    """read cookie txt file

    :param filename: (str) cookies file path
    :return: (dict) cookies
    """
    with open(filename, 'r') as fp:
        cookies = fp.read()
        return cookies


def get_header(filename):
    cookie = read_cookies_file(filename)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'api.bilibili.com',
        'Referer': 'https://www.bilibili.com/account/history',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    return headers


import json
import requests


def read_cookies_file(filename):
    """read cookie txt file

    :param filename: (str) cookies file path
    :return: (dict) cookies
    """
    with open(filename, 'r') as fp:
        cookies = fp.read()
        return cookies


def get_header(filename):
    cookie = read_cookies_file(filename)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'api.bilibili.com',
        'Referer': 'https://www.bilibili.com/account/history',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    return headers


def req_get(headers, url):
    resp = requests.get(url, headers=headers)
    # 检查响应体是否为空
    if resp.text.strip():  # 使用strip()函数移除可能的空白字符
        try:
            return json.loads(resp.text)
        except json.JSONDecodeError as e:
            print("JSONDecodeError:", e)
            print("Response text:", resp.text)
            return None
    else:
        print("Empty response from url:", url)
        return None  # 返回None表示响应体为空
