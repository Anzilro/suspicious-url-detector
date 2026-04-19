import re

def check_url(url):
    print("\n🔍 Analyzing URL...\n")

    score = 0

    # Rule 1: Check HTTP
    if url.startswith("http://"):
        print("[!] Not secure (HTTP used)")
        score += 1

    # Rule 2: Check IP address in URL
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        print("[!] URL uses IP address instead of domain")
        score += 2

    # Rule 3: Long URL
    if len(url) > 75:
        print("[!] URL is too long (suspicious)")
        score += 1

    # Rule 4: Suspicious keywords
    keywords = ["login", "verify", "update", "bank", "secure", "account"]
    matches = [word for word in keywords if word in url.lower()]
    if matches:
        print(f"[!] Suspicious keywords: {', '.join(matches)}")
        score += len(matches)

    # Final Result
    print("\n--- Result ---")
    if score >= 3:
        print("⚠️ High Risk URL")
    elif score == 2:
        print("⚠️ Medium Risk URL")
    else:
        print("✅ Low Risk URL")

    print("\n✅ Scan completed.\n")


# Input
target_url = input("Enter URL: ")
check_url(target_url)