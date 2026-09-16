# LunarWerx GitHub profile

> LunarWerx's GitHub org README: a badge-topped, category-grouped directory of its 14 shipped products.

<!-- odin:about HAND-OWNED above the GENERATED marker. Edit freely; `odin codex about --ingest` carries it back into Odin's Codex. -->

## What it is

The LunarWerxs GitHub organization profile repository - essentially one README.md plus an icons/ folder of SVG/PNG assets - that GitHub renders as the org's public landing page. It is a curated product directory: a hero banner and badge row, then three category tables (AI and agent tooling, developer tools, desktop and everyday utilities) listing all 14 shipped LunarWerx products with a one-line description and website/source/marketplace links each, followed by a Discord community callout, a public MCP server pitch for AI agents, and an FAQ answering cost, hosting model, and AI-agent integration questions.

## Things not to forget

_The intricacies worth remembering: the gotchas, the half-built parts, the decisions whose
reason lives nowhere else. Odin never overwrites this section._

- _(nothing recorded yet - the gotchas, the half-built parts, the decisions worth remembering)_

<!-- odin:about GENERATED BEGIN - rewritten by `odin codex about --publish`; edit the Codex, not this -->

## What Odin knows about this project

Everything from here down is generated from this project's Codex dossier
(`codex/projects/profile.md` in the Odin clone) and is **rewritten on every publish** -
edit the dossier, not this block. Everything ABOVE the marker is yours.

### At a glance

- **Ships as:** static site - GitHub org profile README (rendered by GitHub itself as the LunarWerxs org landing page, no build step, no deploy pipeline)
- **Domain:** software studio, product directory, GitHub org profile, AI and agent tooling, developer tools, desktop utilities, MCP server, badges/shields
- **Remote:** https://github.com/LunarWerxs/LunarWerxs.git

### Architecture

- `README.md` - the entire org profile page: hero banner, badge row, three product-category tables, community section, public MCP server pitch, and FAQ - GitHub renders this file directly as the org landing page
- `icons/` - 22 SVG/PNG assets: the hero and footer banners, three legend glyphs (_site.svg/_code.svg/_store.svg used as inline link icons in every table row), and one logo per product referenced inline in the tables

### Features

8 recorded - 8 shipped, 0 partial, 0 planned. Each path is where the feature is DEFINED; the exact lines live in the Codex entry, which `odin codex check` re-verifies and repairs.

**Shipped**

- **Hero banner and brand badge row** - Full-width hero image linking to lunarwerx.com, followed by website/Discord/live-GitHub-stars badges, a shipped-product-count badge, an all-free badge, an MCP-server-live badge, and a row of tech-stack badges (Rust, TypeScript, Vue, Bun, Python, Cloudflare, MCP). - `README.md`
- **AI and agent tooling table** - Category table listing AgentHydra, RēDesign and DevWebUI, each with an icon, one-line description, and website/source link icons. - `README.md`
- **Developer tools table** - Category table listing RepoYeti, NormWind, AnatomyOf, RoloDexter, Copilot Terminal Monitor and FastColabCopy, each with an icon, one-line description, and website/source/marketplace link icons. - `README.md`
- **Desktop and everyday utilities table** - Category table listing SageThumbs 2K, QuickDictate, VectorMojo, YTSort and IMDb Watcharr, each with an icon, one-line description, and website/source link icons. - `README.md`
- **Community callout** - Centered Discord invite badge and copy inviting questions, bug reports and feature ideas, noting every product has its own channel staffed by its author. - `README.md`
- **Public MCP server pitch for AI agents** - Announces the free, keyless MCP server at lunarwerx.com/mcp with a one-line claude mcp add install command, describes the tailwind_canonicalize and lunarwerx_find_tool tools plus a plain-HTTP fallback, and links the org's listings on the official MCP Registry, Smithery and Glama. - `README.md`
- **FAQ (cost, hosting model, AI-agent integration, support)** - Four collapsible Q&A entries: what the software costs (free, mostly MIT/PolyForm/GPL, bring-your-own-key for AI/speech APIs), self-hosted vs cloud, which products ship their own MCP server and what each exposes (including a Connections Studio mention with no public repo), and where to ask non-bug questions (Discord vs GitHub issues). - `README.md`
- **Footer directory link** - Closing centered callout pointing to lunarwerx.com as the full product directory, above a full-width footer banner image. - `README.md`

### Where to add a new one

- **a new product row in an existing category table** - add a table row following the existing pattern (icon img from icons/, bold product name, one-line description, website/source/marketplace link icons via icons/_site.svg, icons/_code.svg, icons/_store.svg), add the product's logo to icons/, and bump the shipped-product-count badge anchors: `README.md`
- **a new product category** - add a `## <emoji> <Category>` heading followed by a `| | Product | What it does | |` table with the same header/alignment row as the existing three category tables anchors: `README.md`
- **a new FAQ entry** - add a `<details><summary><b>Question</b></summary>...</details>` block under the Questions section, following the existing four entries anchors: `README.md`
- **a new top-of-page badge** - add a shields.io badge image wrapped in a link inside the centered badge div, alongside the existing Website/Discord/stars or product-count/price/MCP badge rows anchors: `README.md`

### Gaps and wants

_Withheld: this repository is public, and the gap list is not published outside the private index._
_Read it with `python odin.py codex brief profile` in the Odin clone._

---

_Generated by `odin codex about --publish profile` on 2026-09-16 from a Codex dossier stamped 2026-09-14. Regenerate after the product moves; `odin codex about` reports drift._
<!-- odin:about GENERATED END sha=fdb55e8c5dab -->
