import requests


def splash_render(url):
    splash_url = "http://localhost:8050/render.html"

    args = {
        "url": url,
        "timeout": 5,
        "image": 0
    }

    response = requests.get(splash_url, params=args)
    return response.text


if __name__ == '__main__':
    url = "http://quotes.toscrape.com/js/"

    html = splash_render(url)
    print(html)
