import pyshorteners


def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)


if __name__ == "__main__":
    url = input("Enter link for sorting:")
    print(f"\n {shorten(url)}")

# https://github.com/urmil89
