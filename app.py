from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Endpoint to fetch JSON data
@app.route('/data', methods=['GET'])
def get_data():
    # Check for API key in headers
    api_key = request.headers.get('X-API-Key')
    expected_key = os.getenv('API_KEY')
    if not api_key or api_key != expected_key:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        # Fetch JSON from GitHub (public repo example)
        github_url = 'https://raw.githubusercontent.com/Nikki-reddy/chug-dashboard/blob/main/data/weekly_results/test_results_fri.json'
        # For private repo, add GitHub PAT
        headers = {'Authorization': 'token ' + os.getenv('GITHUB_PAT')}
        response = requests.get(github_url, headers=headers)
        response = requests.get(github_url)
        response.raise_for_status()  # Raise error for bad responses
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch data: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))