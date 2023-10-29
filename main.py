import hashlib

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def shorten_url(self, original_url):
        # Generate a unique code for the URL using MD5 hash
        md5_hash = hashlib.md5(original_url.encode()).hexdigest()
        code = md5_hash[:6]  # Use the first 6 characters of the hash as the code

        if code not in self.code_to_url:
            # Store the mapping from code to original URL
            self.code_to_url[code] = original_url
            # Store the mapping from original URL to code
            self.url_to_code[original_url] = code

        return f"Your shortened URL: http://short.url/{code}"

    def expand_url(self, short_url):
        code = short_url.split("/")[-1]
        if code in self.code_to_url:
            return f"Original URL: {self.code_to_url[code]}"
        else:
            return "URL not found."

# Create an instance of the URLShortener
shortener = URLShortener()

# Shorten a URL
short_url = shortener.shorten_url("https://www.google.com/")

# Expand a short URL
original_url = shortener.expand_url(short_url)

print(short_url)
print(original_url)
