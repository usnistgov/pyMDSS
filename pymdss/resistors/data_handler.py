from .models import Magnicon_CCC_Process, Thomas_Process, document


def delete_records(mymodel):
    try:
        record = Magnicon_CCC_Process.objects.get(date = '')
        print(record)
        record.delete()
        print("Record deleted successfully!")
    except:
        print("Record doesn't exists")

def build_search_query(table, columns, mydict):
    """
    Returns (query, params) for the filled-in search fields, or None if
    the table is missing one of the searched columns. 'Format' only picks
    the export file type, it is not a column.
    """
    search_terms = {key: val for key, val in mydict.items() if key != 'Format' and val}
    if not all(key in columns for key in search_terms):
        return None
    # A single field is an exact, case-sensitive match; several fields are ANDed with LIKE.
    if len(search_terms) == 1:
        conditions = ["BINARY `{}`=%s".format(key) for key in search_terms]
    else:
        conditions = ["`{}` LIKE %s".format(key) for key in search_terms]
    query = "SELECT * FROM `{}` WHERE ".format(table) + " AND ".join(conditions)
    params = tuple(f"{val}" for val in search_terms.values())
    return query, params
