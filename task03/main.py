import requests
from get_content import get_content
from timeit import timeit
from bm_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

url1 = "https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
url2 = "https://drive.google.com/file/d/18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"
pattern1 = "Взаємодія з відповідною платформою"  # real string from text url1, not present in url2
pattern2 = "Для досягнення поставленої мети"  # real string from text url2, not present in url1


def compare_algorithms(url, pattern):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            content = response.text

            time_boyer_moore = timeit(lambda: boyer_moore_search(content, pattern), number=100)
            time_kmp = timeit(lambda: kmp_search(content, pattern), number=100)
            time_rabin_karp = timeit(lambda: rabin_karp_search(content, pattern), number=100)

            # Print the results
            print(f"Boyer-Moore search time: {time_boyer_moore:.5f} seconds")
            print(f"KMP search time: {time_kmp:.5f} seconds")
            print(f"Rabin-Karp search time: {time_rabin_karp:.5f} seconds")
            print("-" * 40)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    print('pattern1 is found in url1')
    compare_algorithms(url1, pattern1)

    print('pattern2 is not found in url1')
    compare_algorithms(url1, pattern2)

    print('pattern1 is not found in url2')
    compare_algorithms(url2, pattern1)

    print('pattern2 is found in url2')
    compare_algorithms(url2, pattern2)
