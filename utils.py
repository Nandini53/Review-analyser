import time

def safe_api_call(func, *args, retries=3):
    for i in range(retries):
        try:
            return func(*args)
        except Exception:
            time.sleep(2 ** i)

    return "API Failed"