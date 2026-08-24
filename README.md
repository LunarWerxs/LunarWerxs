<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b1d33,50:15304d,100:2e5f92&height=230&section=header&text=LunarWerx%20Studios&fontSize=48&fontAlignY=40&fontColor=ffffff&desc=Digital%20Dreams%20and%20AI%20Solutions&descSize=18&descAlignY=60&animation=fadeIn" width="100%" alt="LunarWerx Studios: digital dreams and AI solutions">
</div>

<div align="center">
  <a href="https://lunarwerx.com"><img src="https://img.shields.io/badge/Website-lunarwerx.com-15304D?style=for-the-badge&logo=safari&logoColor=white" alt="Website: lunarwerx.com"></a>
  <img src="https://img.shields.io/badge/Focus-AI%20and%20Developer%20Tools-2E5F92?style=for-the-badge" alt="Focus: AI and developer tools">
</div>

**LunarWerx Studios is an independent software studio that builds AI-powered developer
tools and desktop utilities.** Most of what we make is free, open source, and runs on your
own machine rather than ours. The sixteen shipped products below span a Windows shell
extension written in Rust, a mobile git client you self-host, and a control plane for local
AI coding agents. Everything listed is released and in use, not a demo. 🌙

## What LunarWerx makes

Every product is free. Most are MIT-licensed and self-hosted, so there is no account to
create and no data leaves your machine unless you point it somewhere yourself.

### AI and agent tooling

| Product | What it does | Links |
| --- | --- | --- |
| **AgentHydra** | Puts every local AI coding session in one tab (Claude Code, Codex, and OpenCode), with a schedulable queue and isolated Claude Desktop instances kept apart. Local, private, MCP-native. | [Site](https://agenthydra.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/AgentHydra) |
| **RēDesign** | Drop in a UI screenshot and it runs the image past many AI models at once, then gives you a browsable wall of self-contained HTML redesigns to compare. Runs locally on Bun. | [Site](https://redesign.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/ReDesign) |
| **DevWebUI** | A GUI *and* an MCP control plane for the dev servers already running on your machine. Humans click; agents automate the same daemon. | [Site](https://devwebui.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/DevWebUI) |
| **vsclaudefix** | Patches the Claude Code VS Code extension to add a persistent side-by-side session pane, pin/star/archive, filters, and live status dots. | [Repo](https://github.com/LunarWerxs/vsclaudefix) |
| **vscodexfix** | Patches the ChatGPT/Codex VS Code extension to add right-click rename/pin/star, a full-height task list, workspace grouping, and working chat search. | [Repo](https://github.com/LunarWerxs/vscodexfix) |

### Developer tools

| Product | What it does | Links |
| --- | --- | --- |
| **RepoYeti** | Run git from your phone, safely. A self-hosted daemon plus a mobile PWA: live repo grid, git-graph history, Monaco diffs, and AI Smart Commit. The dangerous operations are deliberately absent: no force-push, no `reset --hard`, and fast-forward-only pulls. | [Site](https://repoyeti.com) · [Repo](https://github.com/LunarWerxs/RepoYeti) |
| **NormWind** | Normalize Tailwind. A zero-config CLI and GitHub Action that rewrites bloated utility classes into their canonical short form: `px-4 py-4` → `p-4`, `w-6 h-6` → `size-6`. | [Site](https://normwind.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/NormWind) |
| **AnatomyOf** | An interactive, annotated tour of what is actually inside a source file, one language at a time, with colour-coded callouts over real code, for dozens of languages. | [Site](https://anatomyof.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/AnatomyOf) |
| **RoloDexter** | A universal contact field mapper for Python and JavaScript. Routes messy contact data from any CRM, CSV, or email platform into one clean canonical schema. | [Site](https://rolodexter.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/RoloDexter) |
| **Copilot Terminal Monitor** | Watches your VS Code terminal commands and alerts you when one stalls or overruns, with auto-terminate, snooze, and live status-bar timers. | [Marketplace](https://marketplace.visualstudio.com/items?itemName=LunarWerx.copilot-terminal-monitor) · [Repo](https://github.com/LunarWerxs/CopilotTerminalMonitor) |
| **FastColabCopy** | Transfers files inside Google Colab 10–50× faster by copying in parallel across threads instead of one file at a time. | [Repo](https://github.com/LunarWerxs/FastColabCopy) |

### Desktop and everyday utilities

| Product | What it does | Links |
| --- | --- | --- |
| **SageThumbs 2K** | A crash-isolated Rust shell extension that gives Windows 11 Explorer thumbnails for 316 file types it cannot show on its own: camera RAW, PSD, HEIC/AVIF, video, ebooks, comics, CAD. A clean-room revival of the long-abandoned SageThumbs. | [Site](https://sagethumbs.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/SageThumbs-2k) |
| **QuickDictate** | A tiny Windows tray app for voice dictation. Press a hotkey, talk, and your words type into whatever window has focus, using your own speech-to-text key. | [Site](https://quickdictate.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/QuickDictate) |
| **VectorMojo** | Converts design files to clean SVG entirely inside your browser: PSD, PSB, PDF, Illustrator AI, EPS, PNG, and JPEG. No upload step, no server that keeps your file. | [Site](https://vectormojo.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/VectorMojo) |
| **YTSort** | Sorts any YouTube playlist you own by video length, shortest or longest first, in seconds. Userscript plus Chrome extension. | [Site](https://ytsort.lunarwerx.com/) · [Repo](https://github.com/LunarWerxs/YTSort) |
| **IMDb Watcharr** | Turns a public IMDb watchlist or list into a Radarr RSS feed and a Sonarr custom list, so your *arr stack picks up the same titles automatically. | [Site](https://watcharr.lunarwerx.com) · [Repo](https://github.com/LunarWerxs/IMDBWatcharr) |

## What does LunarWerx software cost?

Nothing. Every product listed above is free to download and use. Most are MIT-licensed
open source; SageThumbs 2K is source-available under PolyForm Noncommercial, and YTSort is
GPL-2.0.

A few tools call a third-party AI or speech API, including RepoYeti's Smart Commit, RēDesign, and
QuickDictate. Those are **bring-your-own-key**: you supply your own provider
credentials and pay that provider directly at their rates, which is often nothing on a free
tier. LunarWerx never takes a cut and never resells API access.

## Is LunarWerx software self-hosted or cloud?

Self-hosted and local-first by default. RepoYeti, AgentHydra, DevWebUI, and RēDesign all
run as a daemon on your own machine. SageThumbs 2K and QuickDictate are native Windows
apps. VectorMojo does its work entirely inside the browser tab, with no upload step at all.
Where an optional cloud feature exists, such as RepoYeti's remote tunnel, it is off
until you turn it on.

## How do these tools work with AI agents?

Several are built for agents as first-class users, not just people. DevWebUI and AgentHydra
expose MCP servers so an agent can drive the same daemon a human clicks. RepoYeti's
`repoyeti mcp` exposes local repos plus guarded remote commit and sync, and publishes its
full HTTP API at `GET /api/openapi.json`. NormWind ships as a GitHub Action so it can run
unattended in CI.

## Toolbox

<p>
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Vue-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white" alt="Vue">
  <img src="https://img.shields.io/badge/Bun-000000?style=flat-square&logo=bun&logoColor=white" alt="Bun">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/AI%20%2F%20LLMs-15304D?style=flat-square&logo=anthropic&logoColor=white" alt="AI and LLMs">
</p>

## Elsewhere

**Web** · [lunarwerx.com](https://lunarwerx.com), the full product directory.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2e5f92,50:15304d,100:0b1d33&height=120&section=footer" width="100%" alt="">
