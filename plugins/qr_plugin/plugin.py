import qrcode
import os
from urllib.parse import urljoin
from mkdocs.plugins import BasePlugin


class QRCodePlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        if not config.get('site_url'):
            return markdown

        page_url = urljoin(config['site_url'], page.url)
        qr_filename = f'qr_{page.file.name}.png'
        qr_output_dir = os.path.join(config['site_dir'], 'assets', 'qrcodes')
        qr_path = os.path.join(qr_output_dir, qr_filename)

        os.makedirs(qr_output_dir, exist_ok=True)

        img = qrcode.make(page_url)
        img.save(qr_path)

        qr_md = f'\n\n![QR Code for this page](/assets/qrcodes/{qr_filename})\n'
        return markdown + qr_md

