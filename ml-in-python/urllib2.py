import urllib.request as req

def urlopen(url):
    url_response=req.urlopen(url)
    url_bytes=url_response.read()
    url_string=url_bytes.decode('utf-8')
    url_lines=url_string.strip().split('\n')
    return url_lines
