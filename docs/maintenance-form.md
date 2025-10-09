# Equipment Maintenance Log Entry

<form name="maintenance-log" method="POST" data-netlify="true" action="/maintenance-form-success">
  <input type="hidden" name="form-name" value="maintenance-log" />
  
  <div style="margin-bottom: 20px;">
    <label for="equipment" style="display: block; font-weight: bold; margin-bottom: 5px;">Equipment:</label>
    <input type="text" id="equipment" name="equipment" readonly style="width: 100%; padding: 8px; border: 1px solid #ccc; background-color: #f5f5f5;" />
  </div>
  
  <div style="margin-bottom: 20px;">
    <label for="name" style="display: block; font-weight: bold; margin-bottom: 5px;">Your Name:</label>
    <input type="text" id="name" name="name" required style="width: 100%; padding: 8px; border: 1px solid #ccc;" placeholder="Enter your name" />
  </div>
  
  <div style="margin-bottom: 20px;">
    <label for="notes" style="display: block; font-weight: bold; margin-bottom: 5px;">Notes:</label>
    <textarea id="notes" name="notes" required style="width: 100%; padding: 8px; border: 1px solid #ccc; height: 100px;" placeholder="Enter maintenance notes, usage details, or issues encountered"></textarea>
  </div>
  
  <div style="margin-bottom: 20px;">
    <button type="submit" style="background-color: #007cba; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;">Submit Log Entry</button>
  </div>
</form>

<script>
// Pre-fill equipment field from URL parameter
document.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  const equipment = urlParams.get('equipment');
  if (equipment) {
    document.getElementById('equipment').value = equipment.charAt(0).toUpperCase() + equipment.slice(1);
  }
});
</script>

## How This Works

1. **Scan the QR code** from any equipment page
2. **Fill out the form** with your name and maintenance notes
3. **Submit** - your entry will be automatically added to the equipment's maintenance log
4. **No login required** - anyone can contribute to the maintenance logs

---

[← Back to Equipment Documentation](index.md)
