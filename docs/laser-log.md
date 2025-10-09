---
title: Laser Cutter Maintenance Log
---

# Laser Cutter Maintenance Log

## Current Log Entries

<div id="maintenance-logs">Loading maintenance logs...</div>

<script>
async function loadMaintenanceLogs() {
  try {
    const response = await fetch('/.netlify/functions/get-maintenance-logs?equipment=laser');
    const data = await response.json();
    
    if (data.logs && data.logs.length > 0) {
      const table = `
        <table>
          <thead>
            <tr><th>Date</th><th>Name</th><th>Notes</th></tr>
          </thead>
          <tbody>
            ${data.logs.map(log => `
              <tr>
                <td>${new Date(log.created_at).toLocaleDateString()}</td>
                <td>${log.name}</td>
                <td>${log.notes}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
      document.getElementById('maintenance-logs').innerHTML = table;
    } else {
      document.getElementById('maintenance-logs').innerHTML = '<p>No maintenance logs yet.</p>';
    }
  } catch (error) {
    console.error('Error loading logs:', error);
    document.getElementById('maintenance-logs').innerHTML = '<p>Error loading maintenance logs.</p>';
  }
}

// Load logs when page loads
document.addEventListener('DOMContentLoaded', loadMaintenanceLogs);
</script>

---

## Add New Entry

<form name="maintenance-log" method="POST" data-netlify="true" action="/.netlify/functions/process-maintenance-log">
  <input type="hidden" name="form-name" value="maintenance-log" />
  <input type="hidden" name="equipment" value="laser" />
  
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

---

[← Back to Laser Cutter Guide](laser.md) | [← Back to Equipment Documentation](index.md)
