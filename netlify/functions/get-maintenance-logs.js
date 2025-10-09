const { Client } = require('pg');

exports.handler = async (event, context) => {
  // Only handle GET requests
  if (event.httpMethod !== 'GET') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const equipment = event.queryStringParameters?.equipment;
    
    if (!equipment) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Equipment parameter required' })
      };
    }

    // Database configuration
    const client = new Client({
      connectionString: process.env.NETLIFY_DATABASE_URL,
      ssl: {
        rejectUnauthorized: false
      }
    });

    await client.connect();
    console.log('Connected to database for log retrieval');

    // Fetch maintenance logs for equipment
    const query = `
      SELECT id, equipment, name, notes, created_at
      FROM maintenance_logs 
      WHERE equipment = $1 
      ORDER BY created_at DESC
      LIMIT 50
    `;
    
    const result = await client.query(query, [equipment]);
    await client.end();
    
    console.log(`Retrieved ${result.rows.length} logs for ${equipment}`);

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({
        equipment,
        logs: result.rows
      })
    };

  } catch (error) {
    console.error('Error fetching maintenance logs:', error);
    
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to fetch maintenance logs',
        details: error.message 
      })
    };
  }
};
