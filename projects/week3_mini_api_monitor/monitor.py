from api import check_api

def monitor_apis(api_urls):
    report = []

    for url in api_urls:
        result = check_api(url)
        report.append(result)

    return report