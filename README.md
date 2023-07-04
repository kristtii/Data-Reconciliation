# Data-Reconciliation

Perform data reconciliation using Python

This script, `reconciliation.py`, allows you to reconcile data from two JSON files (`file1.json` and `file2.json`) based on specified fields and generate an output JSON file (`file_output.json`). The script also provides the flexibility to add additional fields from `file2.json` to the output file. Here's how you can use the script:

## Usage

```shell
python3 reconciliation.py file1.json file2.json file_output.json fields_to_be_added_from_file2 --primary_fields match_field1_1 match_field1_2 --secondary_fields match_field2_1 matchfield2_2
```

### Arguments

-   `file1.json`: The path to the first input JSON file.
-   `file2.json`: The path to the second input JSON file.
-   `file_output.json`: The path to the output JSON file that will be generated.
-   `fields_to_be_added_from_file2`: A list of fields from `file2.json` that you want to include in the output file. You can specify as many fields as desired, and they should be listed here.
-   `--primary_fields`: Specify the primary fields from `file1.json` that will be used for matching.
    -   `match_field1_1`: The first primary field from `file1.json` for matching.
    -   `match_field1_2`: The second primary field from `file1.json` for matching.
-   `--secondary_fields`: Specify the secondary fields from `file2.json` that will be used for matching.
    -   `match_field2_1`: The first secondary field from `file2.json` for matching.
    -   `matchfield2_2`: The second secondary field from `file2.json` for matching.

Match fields can be as many as you wish but they should be in order they need to be matched.

## Example

match_field1_1 will match match_field2_1
match_field1_2 will match match_field2_2
