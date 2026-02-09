from monitor import monitor_apis

API_URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/comments/1"
]

def main():
    report = monitor_apis(API_URLS)

    print("\n=== API MONITOR REPORT ===")
    for item in report:
        print(item)

main()