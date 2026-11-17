# Day 5: Capture a Django login on loopback

Tools: Django (`runserver`), Wireshark. Interface: `lo` (loopback).
Goal: run my Django app locally, capture a login, find the username in the packet.

## Setup

```
cd ~/Projects/full_backend
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Problem met: `ModuleNotFoundError: No module named 'django'`. The virtual environment was active, but the packages were not installed in it. Fix: `python -m pip install -r requirements.txt` (`python -m pip` installs into the Python that is running).

## Capture

1. Start Wireshark on the `lo` interface (local traffic never goes through Wi-Fi or Ethernet).
2. Log in on `http://127.0.0.1:8000/admin/` and on the API endpoint `/api/token/` with a test user.
3. Stop the capture and filter:

```
tcp.port == 8000 && http.request.method == "POST"
```

## Result

| Request | Content type | What I saw |
|---|---|---|
| `POST /admin/login/` | `application/x-www-form-urlencoded` | username and password in the HTML Form URL Encoded section |
| `POST /api/token/` | `application/json` | `"username"` and `"password"` in the JSON section |

Where to look: click the POST packet, then **Hypertext Transfer Protocol**, then **HTML Form URL Encoded** or **JavaScript Object Notation**. Or right-click, then **Follow -> HTTP Stream**.

## Conclusion

`runserver` uses plain HTTP, so credentials travel in clear text and anyone who can capture the traffic can read them. In production, the site must use HTTPS (TLS), which encrypts the request body. Only the TLS handshake and encrypted data would be visible (see the TLS capture planned for day 33).

## Lessons

- Use `python -m pip` to be sure packages go into the active virtual environment.
- Use test accounts with fake passwords for captures, and blur passwords in screenshots.
- Weak test credentials (`admin` / `admin123`) are exactly what brute-force attacks try first. This comes back in week 6 (authentication and throttling).
- Never publish captures or screenshots that contain real credentials.
