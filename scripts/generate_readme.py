import os
import json

data_dir = "C:/Users/aerki/.gemini/antigravity/scratch/silo-plugins-catalog/data"
readme_path = "C:/Users/aerki/.gemini/antigravity/scratch/silo-plugins-catalog/README.md"

categories_order = [
    "Metadata Providers",
    "Ratings & Critic Scores",
    "Media Requests & Integrations",
    "Live TV & IPTV",
    "Authentication & Security",
    "Notifications & Webhooks",
    "Markers & Skip Providers",
    "Utility & UI Integrations"
]

category_emojis = {
    "Metadata Providers": "📂",
    "Ratings & Critic Scores": "⭐",
    "Media Requests & Integrations": "🔄",
    "Live TV & IPTV": "📺",
    "Authentication & Security": "🔒",
    "Notifications & Webhooks": "🔔",
    "Markers & Skip Providers": "🔖",
    "Utility & UI Integrations": "🛠️"
}

status_badges = {
    "Active": "🟢 **Active**",
    "In Development": "🟡 **In Development**",
    "Deprecated": "🔴 *Deprecated*",
    "Archived": "📁 *Archived*",
    "Unverified": "⚪ *Unverified*"
}

def load_plugins():
    plugins = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(data_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    plugins.append(data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return plugins

def main():
    plugins = load_plugins()
    
    # Group by category
    by_category = {cat: [] for cat in categories_order}
    for p in plugins:
        cat = p.get("category", "Utility & UI Integrations")
        if cat in by_category:
            by_category[cat].append(p)
        else:
            by_category.setdefault(cat, []).append(p)
            
    # Start building README content
    content = []
    content.append("# Silo Server Plugin Catalog")
    content.append("")
    content.append("> A curated list of third-party plugins, metadata scrapers, and integrations for the [Silo Server](https://siloserver.org/) ecosystem.")
    content.append("")
    content.append("Silo Server is an open-source, high-performance, self-hosted media streaming server with a Go backend and a React-based web user interface. It features a modern, gRPC-based plugin system utilizing the [silo-plugin-sdk](https://github.com/Silo-Server/silo-plugin-sdk) with protobuf contracts.")
    content.append("")
    content.append("## Table of Contents")
    content.append("")
    for cat in categories_order:
        emoji = category_emojis.get(cat, "📁")
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("--", "-")
        content.append(f"- [{emoji} {cat}](#{anchor})")
    content.append("- [📱 Third-Party Client Compatibility](#-third-party-client-compatibility)")
    content.append("- [⚙️ How to Install Plugins](#-how-to-install-plugins)")
    content.append("- [🤝 Contributing](#-contributing)")
    content.append("")
    content.append("---")
    content.append("")
    
    # Render categories
    for cat in categories_order:
        emoji = category_emojis.get(cat, "📁")
        content.append(f"## {emoji} {cat}")
        content.append("")
        
        cat_plugins = by_category[cat]
        if not cat_plugins:
            content.append("*No plugins cataloged in this category yet. Be the first to contribute!*")
            content.append("")
            continue
            
        # Create Table
        content.append("| Plugin / Name | Developer | Description | Status | Compatibility | Verified |")
        content.append("| :--- | :--- | :--- | :--- | :--- | :---: |")
        
        # Sort plugins alphabetically by name
        cat_plugins.sort(key=lambda x: x.get("name", ""))
        for p in cat_plugins:
            name = p.get("name", "Unnamed Plugin")
            url = p.get("repo_url", "#")
            developer = p.get("developer", "Unknown")
            description = p.get("description", "No description provided.")
            status_str = p.get("status", "Active")
            status = status_badges.get(status_str, status_str)
            comp = p.get("compatibility", "Silo SDK (gRPC)")
            
            # Format verification badge
            verified_val = p.get("verified", False)
            if "Continuum" in comp and "Silo-Server" not in url:
                verified = "⚠️ Downstream"
            elif verified_val:
                verified = "✅ Yes"
            else:
                verified = "❓ No"
                
            content.append(f"| [{name}]({url}) | {developer} | {description} | {status} | `{comp}` | {verified} |")
            
        content.append("")
        content.append("---")
        content.append("")
        
    # Client Compatibility Section
    content.append("## 📱 Third-Party Client Compatibility")
    content.append("")
    content.append("Silo Server implements a **Jellyfin-compatible API**, enabling immediate out-of-the-box compatibility with existing Jellyfin ecosystem players. This eliminates the need to wait for custom native clients on some platforms.")
    content.append("")
    content.append("| Client Name | Platform | Type | Notes |")
    content.append("| :--- | :--- | :--- | :--- |")
    content.append("| [Findroid](https://github.com/jellyfin/findroid) | Android / Android TV | Open Source | Highly responsive native player for Android. Works natively with Silo API. |")
    content.append("| [Infuse](https://firecore.com/infuse) | iOS / tvOS / macOS | Proprietary | High-performance premium media player. Excellent support for direct playing all formats. |")
    content.append("| [Swiftfin](https://github.com/jellyfin/swiftfin) | iOS / tvOS | Open Source | Native Swift client for Apple devices. |")
    content.append("| [Jellyfin Media Player](https://github.com/jellyfin/jellyfin-media-player) | Windows / macOS / Linux | Open Source | Native desktop client supporting direct play and hardware decoding. |")
    content.append("| [Kodi (via JellyCon)](https://github.com/jellyfin/jellycon) | Cross-platform | Addon | Lightweight bridge to stream Silo libraries into Kodi media centers. |")
    content.append("")
    content.append("---")
    content.append("")
    
    # Installation Guide
    content.append("## ⚙️ How to Install Plugins")
    content.append("")
    content.append("Silo plugins are compiled as standalone Go/gRPC executable binaries. To install a plugin on your Silo Server instance:")
    content.append("")
    content.append("1. **Download/Build the Binary:** Obtain the compiled plugin executable matching your server operating system and architecture, or clone the repository and build it locally:")
    content.append("   ```bash")
    # Using simple command syntax to avoid windows vs unix confusion
    content.append("   go build -o my-plugin")
    content.append("   ```")
    content.append("2. **Place in Plugins Directory:** Move the plugin binary to the designated plugin directory on your host (e.g. `./plugins/`).")
    content.append("3. **Update Silo Config:** Register the plugin in your `silo.yaml` (or environment variables) by specifying the path to the executable binary and its configuration parameters:")
    content.append("   ```yaml")
    content.append("   plugins:")
    content.append("     - name: silo-plugin-metadata-sportarr")
    content.append("       path: /usr/local/bin/silo-plugin-metadata-sportarr")
    content.append("       config:")
    content.append("         api_key: \"your_sportarr_api_key\"")
    content.append("   ```")
    content.append("4. **Restart Silo Server:** Restart the Silo container or system service to spawn the plugin daemon process. Silo will handshake with the plugin over a secure local gRPC channel.")
    content.append("")
    content.append("---")
    content.append("")
    
    # Contributing Guide Link
    content.append("## 🤝 Contributing")
    content.append("")
    content.append("We welcome submissions of new community plugins! To submit a plugin to this catalog:")
    content.append("1. Read the submission guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).")
    content.append("2. Add a new JSON file to the `data/` directory with the metadata of your plugin.")
    content.append("3. Run the generator script to compile the README:")
    content.append("   ```bash")
    content.append("   python scripts/generate_readme.py")
    content.append("   ```")
    content.append("4. Open a Pull Request.")
    content.append("")
    
    # Save README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"Successfully generated {readme_path}!")

if __name__ == "__main__":
    main()
