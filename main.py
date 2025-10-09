import qrcode
import io
import base64
from urllib.parse import urljoin


def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    for the mkdocs-macros-plugin.
    """
    
    @env.macro
    def qr_code_for_page(page_url=None, edit_url=None):
        """
        Generate a QR code for the current page or edit URL
        Returns HTML img tag with base64 encoded QR code
        """
        # Use edit_url if provided, otherwise use page_url
        target_url = edit_url or page_url
        
        if not target_url:
            return "<!-- QR code: No URL provided -->"
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=2,
        )
        qr.add_data(target_url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Return HTML img tag
        return f'<img src="data:image/png;base64,{img_str}" alt="QR Code" style="max-width: 150px; height: auto;" />'
    
    @env.macro
    def github_edit_qr():
        """
        Generate QR code that links to the GitHub edit page for the current page
        """
        # Get the current page info from the environment
        page = env.variables.get('page', {})
        config = env.variables.get('config', {})
        
        # Build the GitHub edit URL
        repo_url = config.get('repo_url', '')
        edit_uri = config.get('edit_uri', 'edit/master/docs/')
        
        if repo_url and hasattr(page, 'file') and page.file:
            # Remove .git suffix if present
            if repo_url.endswith('.git'):
                repo_url = repo_url[:-4]
            
            # Build the edit URL
            edit_url = f"{repo_url}/{edit_uri}{page.file.src_path}"
            return qr_code_for_page(edit_url=edit_url)
        
        return "<!-- QR code: Could not generate GitHub edit URL -->"
    
    @env.macro
    def maintenance_log_qr(equipment_name=None):
        """
        Generate QR code that links to a maintenance log entry form
        """
        # Get the current page info
        page = env.variables.get('page', {})
        config = env.variables.get('config', {})
        
        # Use equipment name from parameter or derive from page
        if not equipment_name and hasattr(page, 'file') and page.file:
            # Extract equipment name from filename (e.g., laser.md -> laser)
            equipment_name = page.file.name.replace('.md', '').replace('.html', '')
        
        if not equipment_name:
            equipment_name = "unknown"
        
        # Build the maintenance log page URL
        site_url = config.get('site_url', 'https://cgwinfosheets.netlify.app/')
        if not site_url.endswith('/'):
            site_url += '/'
        log_url = f"{site_url}{equipment_name}-log"
        
        return qr_code_for_page(edit_url=log_url)


def main():
    print("Hello from is2!")


if __name__ == "__main__":
    main()
