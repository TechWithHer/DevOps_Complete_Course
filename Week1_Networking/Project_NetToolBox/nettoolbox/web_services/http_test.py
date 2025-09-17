# NetToolBox/http_check.py
import requests
import time

def run(target):
    """
    Checks HTTP/HTTPS status for the given domain/IP.
    Returns status code, response time, and success.
    """
    urls = [f"http://{target}", f"https://{target}"]
    results = []

    for url in urls:
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            elapsed = round((time.time() - start) * 1000, 2)  # in ms
            success = response.status_code < 400

            results.append({
                "url": url,
                "status_code": response.status_code,
                "response_time_ms": elapsed,
                "success": success
            })
        except requests.exceptions.RequestException as e:
            results.append({
                "url": url,
                "status_code": None,
                "response_time_ms": None,
                "success": False,
                "error": str(e)
            })

    overall_success = any(r["success"] for r in results)

    return {
        "test": "HTTP/HTTPS Check",
        "target": target,
        "success": overall_success,
        "results": results
    }

