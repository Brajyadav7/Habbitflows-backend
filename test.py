import urllib.request
import urllib.error

try:
    resp = urllib.request.urlopen("http://127.0.0.1:8000/auth/google/?platform=mobile")
    print("SUCCESS", resp.status)
except urllib.error.HTTPError as e:
    print("ERROR", e.code)
    print(e.read().decode('utf-8'))
