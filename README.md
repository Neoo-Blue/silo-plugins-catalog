# Silo Server Plugin Catalog

> A curated list of third-party plugins, metadata scrapers, and integrations for the [Silo Server](https://siloserver.org/) ecosystem.

Silo Server is an open-source, high-performance, self-hosted media streaming server with a Go backend and a React-based web user interface. It features a modern, gRPC-based plugin system utilizing the [silo-plugin-sdk](https://github.com/Silo-Server/silo-plugin-sdk) with protobuf contracts.

## Table of Contents

- [📂 Metadata Providers](#metadata-providers)
- [⭐ Ratings & Critic Scores](#ratings-critic-scores)
- [🔄 Media Requests & Integrations](#media-requests-integrations)
- [📺 Live TV & IPTV](#live-tv-iptv)
- [🔒 Authentication & Security](#authentication-security)
- [🔔 Notifications & Webhooks](#notifications-webhooks)
- [🔖 Markers & Skip Providers](#markers-skip-providers)
- [🛠️ Utility & UI Integrations](#utility-ui-integrations)
- [📱 Third-Party Client Compatibility](#-third-party-client-compatibility)
- [⚙️ How to Install Plugins](#-how-to-install-plugins)
- [🤝 Contributing](#-contributing)

---

## 📂 Metadata Providers

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-aiometadata](https://github.com/drondeseries/silo-plugin-aiometadata) | drondeseries | Standalone Silo metadata provider backed by AIOMetadata | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-local-metadata](https://github.com/theramindex/silo-plugin-local-metadata) | theramindex | Community local metadata parser for reading local NFO files, poster assets, and sidecar media information. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-manga-metadata](https://github.com/RXWatcher/silo-plugin-manga-metadata) | RXWatcher | Community metadata provider plugin for scraping manga titles, chapters, cover images, and descriptions. | 🟢 **Active** | `Silo SDK / Continuum` | ⚠️ Downstream |
| [silo-plugin-metadata-audiobook](https://github.com/Silo-Server/silo-plugin-metadata-audiobook) | Silo-Server | First-party silo metadata provider for audiobook items (Audnexus / AudiMeta / iTunes / Audible / Storytel). | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-metadata-ebook](https://github.com/Silo-Server/silo-plugin-metadata-ebook) | Silo-Server | First-party plugin intended for ebook metadata scraper integration within the Silo ecosystem. | 🟡 **In Development** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-metadata-manga](https://github.com/Silo-Server/silo-plugin-metadata-manga) | Silo-Server | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-metadata-sportarr](https://github.com/Silo-Server/silo-plugin-metadata-sportarr) | Silo-Server (originally brettpetch) | Official fork of the community-developed sports metadata provider. Fetches sports league data via the Sportarr API, mapping leagues to TV series, seasons to seasons, and events to episodes. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-metadata-tmdb](https://github.com/Silo-Server/silo-plugin-metadata-tmdb) | Silo-Server | First-party Silo metadata provider plugin backed by The Movie Database (TMDB). Fetches movie and TV show titles, seasons, episodes, and poster artwork. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-metadata-tvdb](https://github.com/Silo-Server/silo-plugin-metadata-tvdb) | Silo-Server | First-party Silo metadata provider plugin backed by TheTVDB. Fetches TV series, seasons, episodes, and related artwork details. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |

---

## ⭐ Ratings & Critic Scores

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-mdblist](https://github.com/zerodayz1/silo-plugin-mdblist) | zerodayz1 | Silo metadata-provider plugin that fetches IMDb, Rotten Tomatoes, and Metacritic ratings/scores via the MDBList API. Serves as the modern successor to silo-plugin-omdb. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-omdb](https://github.com/zerodayz1/silo-plugin-omdb) | zerodayz1 | Legacy Silo plugin that fetches IMDb ratings and Rotten Tomatoes critic scores via the OMDb API. Succeeded by silo-plugin-mdblist. | 🔴 *Deprecated* | `Silo SDK (gRPC)` | ✅ Yes |

---

## 🔄 Media Requests & Integrations

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-autoscan-arr](https://github.com/Silo-Server/silo-plugin-autoscan-arr) | Silo-Server | Silo plugin for arr-autoscan | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-dispatcharr](https://github.com/theramindex/silo-plugin-dispatcharr) | theramindex | Silo request plugin that dispatches user movie/TV requests to downstream Radarr and Sonarr media stacks. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-sportarr](https://github.com/brettpetch/silo-plugin-sportarr) | brettpetch | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugins-request-riven](https://github.com/olivertgwalton/silo-plugins-request-riven) | olivertgwalton | Silo request router plugin that integrates content requests with Riven, a Debrid-based media download orchestrator. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugins-requests-arr](https://github.com/Silo-Community/silo-plugins-requests-arr) | Silo-Community | Approved Silo community request plugin that routes movie and series request calls from the Silo UI directly to Sonarr and Radarr queues. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugins-requests-seerr](https://github.com/Silo-Community/silo-plugins-requests-seerr) | Silo-Community | Approved Silo community request plugin that routes content requests through a Seerr or Jellyseerr API manager. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |

---

## 📺 Live TV & IPTV

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-livetv](https://github.com/RXWatcher/silo-plugin-livetv) | RXWatcher | IPTV / M3U live TV portal for Continuum/Silo, featuring XMLTV EPG guides, channel lists, search tools, favorites, and auth-gated streaming proxying. | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |
| [silo-plugin-xtream-library](https://github.com/theramindex/silo-plugin-xtream-library) | theramindex | IPTV library integration that maps Xtream Codes API stream structures directly into Silo Server media catalogs. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |

---

## 🔒 Authentication & Security

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-auth-ldap](https://github.com/Pfuenzle/silo-plugin-auth-ldap) | Pfuenzle | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-auth-oidc](https://github.com/Pfuenzle/silo-plugin-auth-oidc) | Pfuenzle | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-guest-pass](https://github.com/RXWatcher/silo-plugin-guest-pass) | RXWatcher | Generates secure guest-access tokens for sharing temporary media playback sessions without creating full accounts. | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |
| [silo-plugin-oidc-login](https://github.com/RXWatcher/silo-plugin-oidc-login) | RXWatcher | Authentication plugin enabling Single Sign-On (SSO) via OpenID Connect (OIDC) identity providers (e.g., Authelia, Keycloak, Authentik). | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |
| [silo-plugin-whmcs-login](https://github.com/RXWatcher/silo-plugin-whmcs-login) | RXWatcher | WHMCS login integration to authenticate server clients directly against billing records and subscriptions in WHMCS. | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |

---

## 🔔 Notifications & Webhooks

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-discord](https://github.com/thezak48/silo-plugin-discord) | thezak48 | Dispatches webhook notifications to Discord channels for server events like new library content additions or stream activity. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |

---

## 🔖 Markers & Skip Providers

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [silo-plugin-markers-introdb](https://github.com/RXWatcher/silo-plugin-markers-introdb) | RXWatcher | Community marker provider integration supporting skip markers from TheIntroDB, optimized for Continuum instances. | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |
| [silo-plugin-markers-theintrodb](https://github.com/Silo-Server/silo-plugin-markers-theintrodb) | Silo-Server | First-party Silo marker provider plugin that fetches TV show intro and outro skip markers from TheIntroDB. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |

---

## 🛠️ Utility & UI Integrations

| Plugin / Name | Developer | Description | Status | Compatibility | Verified |
| :--- | :--- | :--- | :--- | :--- | :---: |
| [KevlarSilos](https://github.com/KevlarProps/KevlarSilos) | KevlarProps | item silos mc plugin | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [PluginSilo](https://github.com/chinask5/PluginSilo) | chinask5 | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [Q-in-the-Wild](https://github.com/cloudstreet-dev/Q-in-the-Wild) | cloudstreet-dev | kdb+/q is powerful but lives in a silo. This book tears down the walls — integrating Q with Rust, Python, and R, finding the IDE plugins that actually work, and connecting kdb+/q to web frameworks and mainstream tooling. For the Q developer who refuses to be an island. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [SR_BiggerSilo](https://github.com/wledfor2/SR_BiggerSilo) | wledfor2 | Slime Rancher Mod for Unity Plugin Manager that increases silo storage size. Adjusts the maximum number of items any in game entity that uses Silo storage components. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [Semantic-Silo-Pro-Plugin-Development](https://github.com/bluesky0427/Semantic-Silo-Pro-Plugin-Development) | bluesky0427 | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [Silo-plugin](https://github.com/BhanuRathore21/Silo-plugin) | BhanuRathore21 | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [bea-silo](https://github.com/BeAPI/bea-silo) | BeAPI | Dev oriented plugin to add silo feature (IN DEVELOPMENT) | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [cortex](https://github.com/codexbt/cortex) | codexbt | We built Cortex 100% open-source because we believe the future of AI engineering belongs to the open developer community, not closed silos.  We are looking for developers, contributors, and builders to take Cortex to the next level (adding multi-modal terminal vision, local LLM optimizations, and custom agent plugins). | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [crowquillx-silo-plugins](https://github.com/crowquillx/crowquillx-silo-plugins) | crowquillx | Unofficial Silo plugin catalog maintained by crowquillx | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [cumulocity-silo-capacity-widget-plugin](https://github.com/Cumulocity-IoT/cumulocity-silo-capacity-widget-plugin) | Cumulocity-IoT | The Silo Capacity Widget displays a configurable silo capacity graphic with fill levels, foreground image, background image and thresholds. Created by Global Presales. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [dtg-claude-plugins](https://github.com/daikitigogo/dtg-claude-plugins) | daikitigogo | Claude Code plugin marketplace: runnel (task orchestrator) and silo (atomic knowledge skills) | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [flickrsilo](https://github.com/habari/flickrsilo) | habari | Core Plugin Flickr Silo | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [habaribox](https://github.com/habari-extras/habaribox) | habari-extras | PLUGIN: This plugin allows posts to be synced with Dropbox, providing an easy way to edit them anywhere. It also creates a media silo for Dropbox. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [peertube-plugin-siloytube-navigation](https://github.com/TRIALTA/peertube-plugin-siloytube-navigation) | TRIALTA | PeerTube plugin to hide the navigation for several usergroups | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [photozousilo](https://github.com/habari-extras/photozousilo) | habari-extras | PLUGIN: Photozou silo (<a href="http://photozou.jp/">http://photozou.jp</a>) | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [picasasilo](https://github.com/habari-extras/picasasilo) | habari-extras | PLUGIN: Picasa Silo plugin | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-anilist-sync](https://github.com/crowquillx/silo-anilist-sync) | crowquillx | Silo Server plugin that syncs watched anime progress to AniList | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-adult](https://github.com/RXWatcher/silo-plugin-adult) | RXWatcher | Continuum metadata plugin for adult content (ThePornDB, Stash) | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-aiostreams](https://github.com/drondeseries/silo-plugin-aiostreams) | drondeseries | AIOStreams provider for Silo with stable .strm playback-time resolution, caching, and stream failover | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-app-links](https://github.com/theramindex/silo-plugin-app-links) | theramindex | Generates native deep links and launcher shortcuts for external clients from the Silo dashboard. | 🟢 **Active** | `Silo SDK (gRPC)` | ✅ Yes |
| [silo-plugin-local-artwork](https://github.com/theramindex/silo-plugin-local-artwork) | theramindex | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-metadb](https://github.com/RXWatcher/silo-plugin-metadb) | RXWatcher | First-party Silo metadata provider plugin backed by MetaDB. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-public-catalog](https://github.com/RXWatcher/silo-plugin-public-catalog) | RXWatcher | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-sdk](https://github.com/Silo-Server/silo-plugin-sdk) | Silo-Server | Public Go SDK and protobuf contracts for building Silo plugins. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugin-support](https://github.com/RXWatcher/silo-plugin-support) | RXWatcher | Ticketing and utility integration shell providing speedtests, knowledgebase access, and support tickets in-app. | 🟢 **Active** | `Silo / Continuum` | ⚠️ Downstream |
| [silo-plugin-wisp](https://github.com/dreulavelle/silo-plugin-wisp) | dreulavelle | Thin Silo request_router.v1 plugin that delegates fulfillment to a Wisp server | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugins](https://github.com/theramindex/silo-plugins) | theramindex | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-plugins-catalog](https://github.com/Neoo-Blue/silo-plugins-catalog) | Neoo-Blue | No description provided. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-shoko-plugin](https://github.com/crowquillx/silo-shoko-plugin) | crowquillx | Shoko-backed virtual filesystem and metadata plugin for Silo Server | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-sonar-plugin](https://github.com/christian-willman/silo-sonar-plugin) | christian-willman | Silo identifies and helps remediate knowledge siloing in codebases shared across small- and medium-sized teams. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [silo-whmcs-module](https://github.com/RXWatcher/silo-whmcs-module) | RXWatcher | WHMCS billing provisioner module to automate creating and managing Silo Server user accounts and server instances. | 🟢 **Active** | `WHMCS Integration` | ✅ Yes |
| [silotek-plugin-marketplace](https://github.com/JOCOIN94/silotek-plugin-marketplace) | JOCOIN94 | Internal Claude Code plugin marketplace for Silotek workflows. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [smugmug-silo](https://github.com/lildude/smugmug-silo) | lildude | The SmugMug Media Silo plugin implements a Habari silo to access your SmugMug photos making it easy to include images in posts and pages and also upload images directly to SmugMug. | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [twittersilo](https://github.com/habari-extras/twittersilo) | habari-extras | PLUGIN: Simple Twitter Silo | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |
| [wp-silo](https://github.com/sharmashivanand/wp-silo) | sharmashivanand | This plugin helps you to establish a well-structured SILO architecture on your WordPress website | ⚪ *Unverified* | `Silo SDK (gRPC)` | ❓ No |

---

## 📱 Third-Party Client Compatibility

Silo Server implements a **Jellyfin-compatible API**, enabling immediate out-of-the-box compatibility with existing Jellyfin ecosystem players. This eliminates the need to wait for custom native clients on some platforms.

| Client Name | Platform | Type | Notes |
| :--- | :--- | :--- | :--- |
| [Findroid](https://github.com/jellyfin/findroid) | Android / Android TV | Open Source | Highly responsive native player for Android. Works natively with Silo API. |
| [Infuse](https://firecore.com/infuse) | iOS / tvOS / macOS | Proprietary | High-performance premium media player. Excellent support for direct playing all formats. |
| [Swiftfin](https://github.com/jellyfin/swiftfin) | iOS / tvOS | Open Source | Native Swift client for Apple devices. |
| [Jellyfin Media Player](https://github.com/jellyfin/jellyfin-media-player) | Windows / macOS / Linux | Open Source | Native desktop client supporting direct play and hardware decoding. |
| [Kodi (via JellyCon)](https://github.com/jellyfin/jellycon) | Cross-platform | Addon | Lightweight bridge to stream Silo libraries into Kodi media centers. |

---

## ⚙️ How to Install Plugins

Silo plugins are compiled as standalone Go/gRPC executable binaries. To install a plugin on your Silo Server instance:

1. **Download/Build the Binary:** Obtain the compiled plugin executable matching your server operating system and architecture, or clone the repository and build it locally:
   ```bash
   go build -o my-plugin
   ```
2. **Place in Plugins Directory:** Move the plugin binary to the designated plugin directory on your host (e.g. `./plugins/`).
3. **Update Silo Config:** Register the plugin in your `silo.yaml` (or environment variables) by specifying the path to the executable binary and its configuration parameters:
   ```yaml
   plugins:
     - name: silo-plugin-metadata-sportarr
       path: /usr/local/bin/silo-plugin-metadata-sportarr
       config:
         api_key: "your_sportarr_api_key"
   ```
4. **Restart Silo Server:** Restart the Silo container or system service to spawn the plugin daemon process. Silo will handshake with the plugin over a secure local gRPC channel.

---

## 🤝 Contributing

We welcome submissions of new community plugins! To submit a plugin to this catalog:
1. Read the submission guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).
2. Add a new JSON file to the `data/` directory with the metadata of your plugin.
3. Run the generator script to compile the README:
   ```bash
   python scripts/generate_readme.py
   ```
4. Open a Pull Request.
