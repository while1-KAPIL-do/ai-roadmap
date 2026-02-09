import requests
import time

def check_api(url):

    startTime = time.time()
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        endTime = time.time()
        responseTime = round(endTime - startTime, 2)
        return {
            "url"               :   url,
            "response_time"     :   responseTime,
            "status"            :   "UP"
        }
    except requests.exceptions.RequestException as e:
        return {
            "url"               :   url,
            "response_time"     :   None,
            "status"            :   "DOWN",
            "has_error"         :   True,
            "error"             :   str(e),
        }
