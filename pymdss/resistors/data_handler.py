from .models import Magnicon_CCC_Process, Thomas_Process, document


def delete_records(mymodel):
    try:
        record = Magnicon_CCC_Process.objects.get(date = '')
        print(record)
        record.delete()
        print("Record deleted successfully!")
    except:
        print("Record doesn't exists")