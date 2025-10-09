import qrcode
from io import BytesIO
import base64
from markupsafe import Markup


def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """
    
    @env.macro
    def github_edit_qr():
        """Generate QR code for GitHub edit link"""
        # Get the current page info from the environment
        page = env.page
        if page:
            # Construct GitHub edit URL
            repo_url = env.conf['repo_url']
            edit_uri = env.conf.get('edit_uri', 'edit/master/')
            file_path = page.file.src_path
            github_url = f"{repo_url}/{edit_uri}{file_path}"
        else:
            github_url = env.conf['repo_url']
        
        # Generate QR code - compact for printing
        qr = qrcode.QRCode(version=1, box_size=6, border=2)
        qr.add_data(github_url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Return HTML img tag - very compact for printing
        return Markup(f'<div class="qr-code"><img src="data:image/png;base64,{img_str}" alt="QR Code for GitHub Edit" style="max-width: 70px;"></div>')
    
    @env.macro
    def equipment_log_qr():
        """Generate QR code for equipment log entry"""
        # Get the current page info from the environment
        page = env.page
        if page:
            # Extract equipment name from page filename (e.g., laser.md -> laser, 3d-printer.md -> 3d-printer)
            equipment_name = page.file.src_path.replace('.md', '').replace('docs/', '')
            # Create URL for universal log page with equipment parameter
            site_url = env.conf.get('site_url', 'https://cgwinfosheets.netlify.app')
            log_url = f"{site_url}/equipment-log?equipment={equipment_name}"
        else:
            log_url = env.conf.get('site_url', 'https://cgwinfosheets.netlify.app')
        
        # Generate QR code - smaller size for compact printing
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(log_url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Return HTML img tag - very compact for printing
        return Markup(f'<div class="qr-code"><img src="data:image/png;base64,{img_str}" alt="QR Code for Equipment Log" style="max-width: 80px;"></div>')
    
    @env.macro
    def equipment_header(name):
        """Generate styled equipment header"""
        html = f'''<div class="equipment-header">
    <h1>{name}</h1>
</div>'''
        return Markup(html)
    
    @env.macro
    def safety_warning(items):
        """Generate safety warning section"""
        item_list = "<br>".join([f"• {item}" for item in items])
        html = f'''<div class="safety-warning">
    <h4>⚠️ Safety Requirements</h4>
    {item_list}
</div>'''
        return Markup(html)
    
    @env.macro
    def info_section(title, content):
        """Generate info card section"""
        html = f'''<div class="info-card">
    <h3>{title}</h3>
    {content}
</div>'''
        return Markup(html)
    
    @env.macro
    def contact_section(person, description):
        """Generate contact info section"""
        html = f'''<div class="contact-info">
    <h3>Need Help?</h3>
    Contact <strong>{person}</strong> for {description}
</div>'''
        return Markup(html)
    
    @env.macro
    def qr_sections():
        """Generate both QR code sections side by side"""
        equipment_qr = equipment_log_qr()
        edit_qr = github_edit_qr()
        html = f'''<div style="display: flex; gap: 0.2rem;">
<div class="qr-section" style="flex: 1;">
    <h4>Equipment Log</h4>
    {equipment_qr}
</div>
<div class="edit-section" style="flex: 1;">
    <h4>Edit Page</h4>
    {edit_qr}
</div>
</div>'''
        return Markup(html)
