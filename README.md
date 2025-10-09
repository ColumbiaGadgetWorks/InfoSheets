# Columbia Gadget Works Info Sheets

A MkDocs-based documentation site with a custom QR code plugin that automatically generates QR codes for each page.
The site uses a custom plugin for automatic QR code generation

## Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

## Quick Start

### 1. Install dependencies

Using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

### 2. Start the development server

```bash
uv run mkdocs serve
```

Or if using pip:
```bash
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`

### 3. Build for production

```bash
uv run mkdocs build
```

## Project Structure

```
InfoSheets/
├── docs/                   # Documentation source files
│   ├── index.md           # Homepage
│   └── laser.md           # Laser documentation
├── plugins/               # Custom MkDocs plugins
│   └── qr_code/          # QR code plugin
├── mkdocs.yml            # MkDocs configuration
├── pyproject.toml        # Python project configuration
└── main.py               # Entry point script
```

## Features

- **Material Design Theme**: Modern, responsive documentation theme
- **QR Code Generation**: Automatically generates QR codes for each page
- **Live Reload**: Development server with automatic page refresh
- **GitHub Integration**: Configured for GitHub Pages deployment

## Development

The project uses:
- **MkDocs**: Static site generator for documentation
- **Material Theme**: Modern documentation theme
- **Custom QR Plugin**: Generates QR codes linking to each page
- **uv**: Fast Python package manager

## Deployment

### Netlify Deployment (Recommended)

This project is configured for Netlify deployment with automatic maintenance log processing.

#### Quick Deploy Steps:
1. **Sign up at [netlify.com](https://netlify.com)** using your GitHub account
2. **Import project**: "Add new site" → "Import an existing project" → "Deploy with GitHub"
3. **Select repository**: Choose `ColumbiaGadgetWorks/InfoSheets`
4. **Configure build settings**:
   - **Branch to deploy**: `master` (source code, not gh-pages)
   - **Build command**: `uv run mkdocs build` (auto-detected from netlify.toml)
   - **Publish directory**: `site` (auto-detected from netlify.toml)
5. **Deploy**: Click "Deploy site"
6. **Set environment variable**: 
   - Go to Site settings → Environment variables
   - Add `GITHUB_TOKEN` with a GitHub Personal Access Token (repo + workflow scopes)
7. **Update site URL**: Replace `your-site-name.netlify.app` in `mkdocs.yml` with your actual Netlify URL

#### GitHub Personal Access Token Setup (Fine-Grained - Recommended):
1. GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens**
2. Generate new token:
   - **Name**: "Netlify InfoSheets Maintenance"
   - **Repository access**: "Selected repositories" → Choose `InfoSheets` only
   - **Repository permissions**: Contents (Read/Write), Metadata (Read), Actions (Write)
3. Copy token to Netlify environment variables as `GITHUB_TOKEN`

#### Alternative: Classic Token Setup:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` and `workflow` scopes
3. Copy token to Netlify environment variables as `GITHUB_TOKEN`

### Features Enabled by Netlify:
- **Netlify Forms**: Unauthenticated maintenance log submissions
- **Serverless Functions**: Automatic GitHub integration for log processing
- **Continuous Deployment**: Auto-rebuild on GitHub pushes

### Alternative: GitHub Pages
The project can also deploy to GitHub Pages via GitHub Actions. See `.github/workflows/deploy-mkdocs.yml` for details. Note: Maintenance log functionality requires Netlify.

## Troubleshooting

If you encounter issues:

1. Ensure Python 3.12+ is installed: `python --version`
2. Install uv if not available: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Clear any cached files: `rm -rf site/`
4. Reinstall dependencies: `uv sync --force`

For more help, see the [MkDocs documentation](https://www.mkdocs.org).

## Project Purpose

This project produces a Netlify-hosted website with print-optimized pages for physical machines in the Columbia Gadget Works makerspace. Each page serves as a **Quick Start Guide** designed to be printed on a single 8.5x11" sheet and posted near equipment.

### Key Features:
- **Print-optimized layout**: Single-page format with compact styling for B&W printing
- **Equipment logging**: QR codes link to universal equipment log system
- **Easy editing**: GitHub integration for content updates
- **Database-driven logs**: PostgreSQL storage via Netlify Functions

## Lessons Learned

### Print Optimization
- **Single-page constraint**: All content must fit on one printed page
- **B&W styling**: Use pure black/white with thick borders for visibility
- **Compact typography**: 10-11px fonts with tight line spacing (1.1-1.2)
- **Minimal margins**: 0.2in page margins to maximize content area

### Equipment Page Structure
- **Safety first**: Prominent safety warnings with thick black borders
- **Essential info only**: Software, materials, startup/shutdown procedures, contact
- **Inline procedures**: Numbered steps in headers to save vertical space
- **Dual QR codes**: Equipment logging and page editing side-by-side

### Technical Architecture
- **Universal logging**: Single `equipment-log.md` with URL parameters instead of separate pages
- **Macro limitations**: Direct HTML more reliable than complex MkDocs macros
- **Database over files**: Netlify Functions + PostgreSQL more reliable than GitHub API
- **Environment variables**: Use `NETLIFY_DATABASE_URL` for database connections

### Deployment Gotchas
- **Empty directories**: Remove unused `custom_dir: overrides` from mkdocs.yml
- **Print CSS**: Use `@media print` with `!important` overrides for proper B&W rendering
- **QR code sizing**: Balance scanability with space constraints (80px equipment, 70px edit)

### Content Strategy
- **Equipment-specific contacts**: Each page has dedicated support person
- **Consistent terminology**: "Equipment Log" encourages routine usage logging
- **Placeholder text**: Equipment-specific form placeholders ("What did you cut/print/mill?")

## Build Instructions
   