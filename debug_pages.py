from app import app, flatpages

print("Iterating pages...")
count = 0
found = False
for p in flatpages:
    count += 1
    if "relationship" in p.path:
        print(f"Found: {p.path}")
        print(f"Meta: {p.meta}")
        found = True

print(f"Total pages iterated: {count}")
if not found:
    print("Page NOT found in flatpages collection.")
