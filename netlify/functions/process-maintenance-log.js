const { Client } = require('pg');

exports.handler = async (event, context) => {
  // Only handle POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    // Parse form data
    const params = new URLSearchParams(event.body);
    const equipment = params.get('equipment') || 'unknown';
    const name = params.get('name') || 'Anonymous';
    const notes = params.get('notes') || 'No notes provided';

    // Log the received data for debugging
    console.log('Form submission received:', { equipment, name, notes });

    // Database configuration
    if (!process.env.NETLIFY_DATABASE_URL) {
      throw new Error('NETLIFY_DATABASE_URL environment variable not set');
    }
    
    console.log('NETLIFY_DATABASE_URL present:', !!process.env.NETLIFY_DATABASE_URL);
    console.log('NETLIFY_DATABASE_URL preview:', process.env.NETLIFY_DATABASE_URL?.substring(0, 20) + '...');
    
    const client = new Client({
      connectionString: process.env.NETLIFY_DATABASE_URL,
      ssl: process.env.NETLIFY_DATABASE_URL.includes('localhost') ? false : {
        rejectUnauthorized: false
      }
    });

    await client.connect();
    console.log('Connected to database');

    // Insert maintenance log entry
    const query = `
      INSERT INTO maintenance_logs (equipment, name, notes, created_at)
      VALUES ($1, $2, $3, NOW())
      RETURNING id, created_at
    `;
    
    const result = await client.query(query, [equipment, name, notes]);
    await client.end();
    
    console.log('Maintenance log entry saved:', result.rows[0]);

    return {
      statusCode: 302,
      headers: {
        Location: '/maintenance-form-success'
      }
    };

  } catch (error) {
    console.error('Error processing maintenance log:', error);
    
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to process maintenance log entry',
        details: error.message 
      })
    };
  }
};
