try:
    # Define two dictionaries
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    # Merging dictionaries using the unpacking method
    merged_dict = {**dict1, **dict2}

    # Print the merged dictionary
    print("Merged Dictionary:", merged_dict)

except (KeyError, TypeError) as e:
    # Catch multiple exceptions and display an error message
    print(f"An error occurred: {e}")
