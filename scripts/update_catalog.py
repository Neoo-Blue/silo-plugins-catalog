import os
import json
import urllib.request
import ssl
import generate_readme

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))

def get_existing_urls():
    urls = set()
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(data_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    url = data.get("repo_url", "").lower().strip()
                    if url:
                        urls.add(url)
            except Exception as e:
                print(f"Error reading local file {filename}: {e}")
    return urls

def main():
    existing_urls = get_existing_urls()
    
    # Query GitHub API
    url = "https://api.github.com/search/repositories?q=silo-plugin&per_page=100"
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Silo-Plugin-Catalog-Updater'}
    )
    context = ssl._create_unverified_context()
    
    print("Searching GitHub for new 'silo-plugin' repositories...")
    try:
        with urllib.request.urlopen(req, context=context) as response:
            res_data = json.loads(response.read().decode())
            items = res_data.get("items", [])
    except Exception as e:
        print(f"Error querying GitHub API: {e}")
        return
        
    new_plugins_added = 0
    
    for item in items:
        repo_url = item.get("html_url", "").strip()
        if not repo_url:
            continue
            
        # Check if already cataloged
        if repo_url.lower().strip() in existing_urls:
            continue
            
        # We found a new plugin!
        name = item.get("name", "")
        owner = item.get("owner", {}).get("login", "Unknown")
        description = item.get("description", "") or "No description provided."
        
        # Determine a reasonable default category based on name keywords
        category = "Utility & UI Integrations"
        name_lower = name.lower()
        if "metadata" in name_lower or "scraper" in name_lower or "tmdb" in name_lower or "tvdb" in name_lower:
            category = "Metadata Providers"
        elif "rating" in name_lower or "score" in name_lower:
            category = "Ratings & Critic Scores"
        elif "request" in name_lower or "seerr" in name_lower or "arr" in name_lower:
            category = "Media Requests & Integrations"
        elif "tv" in name_lower or "iptv" in name_lower:
            category = "Live TV & IPTV"
        elif "auth" in name_lower or "login" in name_lower or "oidc" in name_lower:
            category = "Authentication & Security"
        elif "discord" in name_lower or "notify" in name_lower or "webhook" in name_lower:
            category = "Notifications & Webhooks"
        elif "marker" in name_lower or "skip" in name_lower:
            category = "Markers & Skip Providers"
            
        plugin_data = {
            "name": name,
            "repo_url": repo_url,
            "category": category,
            "description": description,
            "status": "Unverified",
            "verified": False,
            "developer": owner,
            "compatibility": "Silo SDK (gRPC)",
            "citations": [repo_url]
        }
        
        # Save to a new JSON file
        safe_name = name.replace("silo-plugin-", "").replace("silo-plugins-", "").lower()
        filename = f"community-auto-{safe_name}.json"
        filepath = os.path.join(data_dir, filename)
        
        # Double check file does not exist
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(plugin_data, f, indent=2, ensure_ascii=False)
            print(f"[NEW] Added new unverified plugin: {name} ({repo_url})")
            new_plugins_added += 1
            existing_urls.add(repo_url.lower().strip())
            
    if new_plugins_added > 0:
        print(f"Added {new_plugins_added} new plugins. Regenerating README...")
        generate_readme.main()
    else:
        print("No new plugins found. Catalog is up to date.")

if __name__ == "__main__":
    main()
