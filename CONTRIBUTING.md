# Contributing to the Silo Server Plugin Catalog

First of all, thank you for helping grow the Silo Server ecosystem! This repository is a community-driven catalog designed to index third-party plugins, custom metadata scrapers, and integrations.

To keep the catalog organized and machine-readable, we store plugin information in separate JSON files inside the `data/` directory and compile the main `README.md` dynamically using an automation script.

---

## How to Submit a Plugin

1. **Fork the Repository:** Create a personal copy of this repository on GitHub.
2. **Add a JSON Metadata File:** Navigate to the `data/` directory and create a new JSON file named after your plugin (e.g. `data/my-plugin-name.json`). Follow the schema below.
3. **Generate the README:** Run the compilation script from the repository root to regenerate `README.md`:
   ```bash
   python scripts/generate_readme.py
   ```
4. **Commit and Push:** Push your changes to your fork. Make sure to commit both your new `data/*.json` file and the updated `README.md`.
5. **Open a Pull Request:** Submit a PR back to our `main` branch. Provide a brief description of the plugin in the PR text.

---

## Metadata JSON Schema

Each plugin must be defined using the following JSON schema:

```json
{
  "name": "silo-plugin-my-extension",
  "repo_url": "https://github.com/developer/silo-plugin-my-extension",
  "category": "Metadata Providers",
  "description": "A concise description of the plugin's purpose and functionality.",
  "status": "Active",
  "verified": true,
  "developer": "developer-username",
  "compatibility": "Silo SDK (gRPC)",
  "citations": [
    "https://github.com/developer/silo-plugin-my-extension"
  ]
}
```

### Field Definitions

- **`name`** *(string, required)*: The exact repository or package name of your plugin.
- **`repo_url`** *(string, required)*: The absolute URL to the source code repository (GitHub, GitLab, etc.).
- **`category`** *(string, required)*: Must be one of the following taxonomies:
  - `"Metadata Providers"` (Scrapers for movies, TV, sports, books, anime, etc.)
  - `"Ratings & Critic Scores"` (Critic scores like IMDb, Rotten Tomatoes, Letterboxd)
  - `"Media Requests & Integrations"` (Integrations with request tools like Sonarr, Radarr, Seerr, Riven)
  - `"Live TV & IPTV"` (M3U players, XMLTV guides, Xtream Codes integrations)
  - `"Authentication & Security"` (SSO, LDAP, OIDC, guest access layers)
  - `"Notifications & Webhooks"` (Discord webhooks, Telegram, email notifications)
  - `"Markers & Skip Providers"` (Intro/outro detection databases, chapter skip utilities)
  - `"Utility & UI Integrations"` (Billing integrations, customer panels, UI widgets, app links)
- **`description`** *(string, required)*: A clear, concise description (max 250 characters) explaining what the plugin does. Do not include placeholders.
- **`status`** *(string, required)*: Must be one of:
  - `"Active"` (Actively maintained, builds, and works with current Silo versions)
  - `"In Development"` (Planned or partially complete, not yet stable)
  - `"Deprecated"` (Succeeded by another plugin; kept for historical reference)
  - `"Archived"` (Source repo is read-only, may not work with current versions)
  - `"Unverified"` (Discovered but operational status is unknown)
- **`verified`** *(boolean, required)*: Set to `true` if the plugin has been tested and verified to work with the standard `silo-plugin-sdk`.
- **`developer`** *(string, required)*: The name or GitHub handle of the developer or organization maintaining the plugin.
- **`compatibility`** *(string, required)*: The supported runtime environment. E.g. `"Silo SDK (gRPC)"` (standard plugins) or `"Silo / Continuum"` (for plugins specific to the Continuum fork).
- **`citations`** *(array of strings, required)*: URLs verifying the plugin's details (e.g. source repository, release page, or documentation).

---

## Verification Criteria

To maintain a high-quality catalog, all submissions are subject to the following validation checklist before they are merged:
- **Valid Repository:** The repository link must be public and accessible.
- **Relevant to Silo:** The repository must consume the `silo-plugin-sdk` or integrate directly with a Silo Server instance.
- **No Placeholders:** All fields must contain realistic, fully realized details.
- **No Syntax Errors:** The JSON file must be syntactically valid and match the schema.
- **README Matches:** Running `generate_readme.py` must not cause any errors, and the resulting table row must display correctly.
