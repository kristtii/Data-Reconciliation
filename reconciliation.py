import json
import argparse

class LocationMatcher:
    def __init__(self, primary_data, secondary_data, fields, primary_fields, secondary_fields):
        self.primary_data = primary_data
        self.secondary_data = secondary_data
        self.fields = fields
        self.primary_fields = primary_fields
        self.secondary_fields = secondary_fields
        self.matched_data = []

    def match_locations(self):
        for primary_record in self.primary_data:
            primary_values = [primary_record[field] for field in self.primary_fields]

            matched_records = self._find_matches(primary_values)
            if matched_records:
                for matched_record in matched_records:
                    matched_data = {**primary_record, **matched_record}
                    matched_data = self._convert_values_to_string(matched_data)
                    self.matched_data.append(matched_data)

    def _find_matches(self, primary_values):
        matches = []
        for secondary_record in self.secondary_data:
            secondary_values = [secondary_record[field] for field in self.secondary_fields]
            if primary_values == secondary_values:
                matches.append({k: secondary_record[k] for k in self.fields})
        return matches

    def _convert_values_to_string(self, data):
        converted_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                converted_data[key] = self._convert_values_to_string(value)
            else:
                converted_data[key] = str(value)
        return converted_data

def match_and_save_data(primary_file, secondary_file, output_file, fields, primary_fields, secondary_fields):
    # Load data from the primary JSON file
    with open(primary_file, "r") as f:
        primary_data = json.load(f)

    # Load data from the secondary JSON file
    with open(secondary_file, "r") as f:
        secondary_data = json.load(f)

    # Create an instance of LocationMatcher and perform matching
    matcher = LocationMatcher(primary_data, secondary_data, fields, primary_fields, secondary_fields)
    matcher.match_locations()

    # Access the matched data from the matcher object
    matched_data = matcher.matched_data

    # Save the matched data to the output JSON file
    with open(output_file, "w") as f:
        json.dump(matched_data, f, indent=4)

    print(f"Joined data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Location Matcher")
    parser.add_argument("primary_file", help="Path to the primary JSON file")
    parser.add_argument("secondary_file", help="Path to the secondary JSON file")
    parser.add_argument("output_file", help="Path to the output JSON file")
    parser.add_argument("--primary_fields", nargs="+", help="Fields to match from the primary file")
    parser.add_argument("--secondary_fields", nargs="+", help="Fields to match from the secondary file")
    parser.add_argument("fields", nargs="+", help="Fields to retrieve from the secondary file")
    args = parser.parse_args()

    match_and_save_data(args.primary_file, args.secondary_file, args.output_file, args.fields, args.primary_fields, args.secondary_fields)