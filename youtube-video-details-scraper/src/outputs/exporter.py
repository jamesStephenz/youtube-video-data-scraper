thonfrom extractors.utils import save_to_json

def export_data(data, output_file='output.json'):
    """Export the data to a JSON file."""
    save_to_json(data, output_file)