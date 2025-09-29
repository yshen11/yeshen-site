# Ye Shen — Personal Site (GitHub Pages)

A minimalist personal site. This site was originally made by and for Ye Shen, a researcher in **Health Policy (Decision Sciences)**. You are welcome to use this template, but be sure to update it if you do!

## About this template
Built for GitHub Pages (Jekyll). 
Includes pages: such as: Home, About, Research, Contact.

## Quick Start
1. Create a repo on GitHub (user site `your-username.github.io` or project site).
2. Upload these files or initialize from this template.
3. Edit `_config.yml`:
   - `url: "https://your-username.github.io"`
   - For project sites, set `baseurl: "/your-repo-name"`.
   - Update `social` links (Scholar, LinkedIn, X) as you see fit.
4. Once you have made your edits and want to make it public, go to: Enable Pages in **Settings → Pages** (GitHub Actions or Deploy from branch).
5. Customize the current text in `index.md`, `about.md`, `research.md`, `contact.md` if you are not Ye Shen. 

### Local Preview (optional)
```bash
gem install bundler jekyll
bundle init
echo 'gem "jekyll", "~> 4.3"' >> Gemfile
bundle install
bundle exec jekyll serve
```
Open http://127.0.0.1:4000 in suitable browser.


## Notes
- No form - email‑only contact.
- Styling controlled in `assets/css/style.css` (see CSS variables).
- You can add a `_posts/` folder later for news/updates.


---

## Publications Auto‑Update (Google Scholar)

This site can auto‑pull publications from **Google Scholar** using the SerpAPI Author API.

### Option A — Turn on auto-updates
1. Create a free/paid SerpAPI account to get an API key: https://serpapi.com/
2. In your GitHub repo, go to **Settings → Secrets and variables → Actions → New repository secret**:
   - Name: `SERPAPI_API_KEY`
   - Value: your key
3. The workflow at `.github/workflows/scholar.yml` will:
   - Run on every push to `main` and weekly on Mondays.
   - Fetch publications for author id `c3IRn-EAAAAJ` (Ye Shen). You can change `SCHOLAR_AUTHOR_ID` in the workflow env.
   - Write to `assets/data/publications.json`.
4. The **Publications** page (`/publications/`) renders from that JSON client‑side.

### Option B — Manual
Edit `assets/data/publications.json` directly to add/update items; no API key needed.
This is what I do.

> Note: Direct client‑side scraping of Google Scholar is not allowed, this repo uses a server-side build step (GitHub Action) to produce a static JSON that GitHub Pages can serve. We do not scrape Google Scholar. 
