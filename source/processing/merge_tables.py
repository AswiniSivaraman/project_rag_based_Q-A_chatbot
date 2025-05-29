from source.processing.process_data import get_merged_all_tables


def get_final_merged_list():
    """
    Combines all table row strings into a single list.

    Returns:
        list: A single list containing all rows from all tables as formatted strings.
    """
    merged_tables = get_merged_all_tables()

    # Flatten all lists from each table into one final list
    final_list = []
    for table_name, row_list in merged_tables.items():
        final_list.extend(row_list)

    return final_list
