thonimport json

def save_to_json(data, filename):
    """Save extracted data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)