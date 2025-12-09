import os
import argparse
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from collections import namedtuple

Link = namedtuple("Link", ["url", "source_file", "line_no"])

class LinkFinder(HTMLParser):
    def __init__(self, source_file):
        super().__init__()
        self.source_file = source_file
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = None
        if tag in ("a", "link") and "href" in attrs:
            url = attrs["href"]
        elif tag in ("img", "script") and "src" in attrs:
            url = attrs["src"]

        if url:
            self.links.append(Link(url, self.source_file, self.getpos()[0]))

def check_links(directory):
    all_links = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    parser = LinkFinder(filepath)
                    parser.feed(content)
                    all_links.extend(parser.links)

    broken_links = []
    checked_urls = {}

    for link in all_links:
        if link.url in checked_urls:
            if checked_urls[link.url] is not None:
                 broken_links.append(f"BROKEN: {link.url} in {link.source_file} (Reason: {checked_urls[link.url]})")
            continue
        
        if link.url.startswith(("http://", "https://")):
            try:
                req = urllib.request.Request(link.url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.status >= 400:
                        reason = f"HTTP status {response.status}"
                        broken_links.append(f"BROKEN: {link.url} in {link.source_file} (Reason: {reason})")
                        checked_urls[link.url] = reason
            except Exception as e:
                reason = str(e)
                broken_links.append(f"BROKEN: {link.url} in {link.source_file} (Reason: {reason})")
                checked_urls[link.url] = reason
        elif not link.url.startswith(("#", "mailto:", "tel:")):
            path = link.url.split("#")[0].split("?")[0]
            if path:
                abs_path = os.path.join(os.path.dirname(link.source_file), path)
                if path.startswith("/"):
                    abs_path = os.path.join(directory, path.lstrip('/'))

                if not os.path.exists(abs_path):
                     # Check if it's a directory link without index.html
                    if os.path.isdir(abs_path) and not os.path.exists(os.path.join(abs_path, 'index.html')):
                        reason = f"File not found (directory link without index.html)"
                        broken_links.append(f"BROKEN: {link.url} in {link.source_file} (Reason: {reason})")
                        checked_urls[link.url] = reason
                    elif not os.path.isdir(abs_path):
                        reason = f"File not found"
                        broken_links.append(f"BROKEN: {link.url} in {link.source_file} (Reason: {reason})")
                        checked_urls[link.url] = reason
    
    return broken_links

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for broken links in a static website.")
    parser.add_argument("directory", help="The root directory of the website to check (e.g., 'docs').")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' not found.")
        exit(1)

    print(f"Checking links in '{args.directory}'...")
    broken = check_links(args.directory)

    if broken:
        print("\nFound broken links:")
        for link in broken:
            print(link)
        exit(1)
    else:
        print("\nNo broken links found.")
        exit(0)
