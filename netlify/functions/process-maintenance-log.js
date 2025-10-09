const { Octokit } = require('@octokit/rest');

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

    // GitHub configuration
    const octokit = new Octokit({
      auth: process.env.GITHUB_TOKEN
    });

    const owner = 'ColumbiaGadgetWorks';
    const repo = 'InfoSheets';

    // Trigger GitHub Action via repository dispatch
    await octokit.rest.repos.createDispatchEvent({
      owner,
      repo,
      event_type: 'maintenance-log-entry',
      client_payload: {
        equipment,
        name,
        notes
      }
    });

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
