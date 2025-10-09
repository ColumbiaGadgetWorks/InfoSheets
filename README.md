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

This project is to produce a github hosted website with pages that correspond to physical machines in the 
Columbia Gadget Works makerspace.  

These pages are designed to be printed and posted near the equipment and give users essential information
on the use and care of the machines

The pages are to be formatted in a way that is easy to print and easy to read when printed.

Each page will include a QR code that points to the edit page on github.

The github workflow will automatically trigger and rebuild the site after editing the file

The site uses mkdocs and mkdocs-material.

It also assumes UV/UVX for managing virtual environment

# Build instructions for local build and testing

1. Install dependencies
   ```
   