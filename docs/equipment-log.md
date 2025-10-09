# Equipment Log

<script>
// Get equipment from URL parameter
const urlParams = new URLSearchParams(window.location.search);
const equipment = urlParams.get('equipment') || 'unknown';

// Equipment display names
const equipmentNames = {
    'laser': 'Laser Cutter',
    'vinyl-cutter': 'Vinyl Cutter', 
    '3d-printer': '3D Printer',
    'shapeoko-cnc': 'Shapeoko CNC'
};

// Update page title and form
document.addEventListener('DOMContentLoaded', function() {
    const equipmentName = equipmentNames[equipment] || equipment;
    document.title = `${equipmentName} Equipment Log`;
    document.querySelector('h1').textContent = `${equipmentName} Equipment Log`;
    document.querySelector('input[name="equipment"]').value = equipment;
    
    // Update placeholder text based on equipment
    let placeholder;
    if (equipment.includes('laser')) {
        placeholder = 'What did you cut? Any issues or maintenance performed?';
    } else if (equipment === 'vinyl-cutter') {
        placeholder = 'What did you cut? Any issues or maintenance performed?';
    } else if (equipment === '3d-printer') {
        placeholder = 'What did you print? Any issues or maintenance performed?';
    } else if (equipment === 'shapeoko-cnc') {
        placeholder = 'What did you mill? Any issues or maintenance performed?';
    } else {
        placeholder = 'What did you use? Any issues or maintenance performed?';
    }
    document.querySelector('#notes').placeholder = placeholder;
    
    loadLogEntries();
});
</script>

**Scan to log usage or maintenance**

<form name="equipment-log" method="POST" action="/.netlify/functions/process-maintenance-log" netlify>
  <input type="hidden" name="equipment" value="" />
  
  <p>
    <label for="name">Your Name:</label><br>
    <input type="text" id="name" name="name" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; background: white; color: black;">
  </p>
  
  <p>
    <label for="notes">Usage/Maintenance Notes:</label><br>
    <textarea id="notes" name="notes" rows="4" required style="width: 100%; padding: 8px; margin: 4px 0;" placeholder="What did you use? Any issues or maintenance performed?"></textarea>
  </p>
  
  <p>
    <button type="submit" style="background: #37474f; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Submit Log Entry</button>
  </p>
</form>

---

## Recent Log Entries

<div id="log-entries">
Loading recent entries...
</div>

<script>
// Auto-refresh after form submission
if (window.location.search.includes('success')) {
    setTimeout(() => {
        window.location.href = window.location.pathname + '?equipment=' + equipment;
    }, 2000);
}

// Load log entries
async function loadLogEntries() {
    try {
        const response = await fetch(`/.netlify/functions/get-maintenance-logs?equipment=${equipment}`);
        const data = await response.json();
        
        const container = document.getElementById('log-entries');
        
        // Check if response has error
        if (!response.ok || data.error) {
            container.innerHTML = `<p><em>Error: ${data.error || 'Failed to load entries'}</em></p>`;
            return;
        }
        
        // Get logs from the response data structure
        const logs = data.logs || data;
        
        if (!logs || logs.length === 0) {
            container.innerHTML = '<p><em>No log entries yet.</em></p>';
            return;
        }
        
        const entriesHtml = logs.map(log => `
            <div style="border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 4px;">
                <strong>${log.name}</strong> - ${new Date(log.created_at || log.timestamp).toLocaleDateString()}
                <p>${log.notes}</p>
            </div>
        `).join('');
        
        container.innerHTML = entriesHtml;
    } catch (error) {
        console.error('Error loading log entries:', error);
        document.getElementById('log-entries').innerHTML = '<p><em>Error loading entries.</em></p>';
    }
}
</script>
