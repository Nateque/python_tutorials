# Function caching

import time
from functools import lru_cache

@lru_cache(maxsize=2)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print('Wait 3 secs')
    some_work(3)
    print('almost done, lets do again')
    some_work(3)
    print('Done without delay because of \"lru_cache\"')