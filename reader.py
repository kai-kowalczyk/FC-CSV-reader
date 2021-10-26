import sys
from pathlib import Path
from lib import CSVReader

source = sys.argv[1]
destination = sys.argv[2]
changes = sys.argv[3:]

'''changes "Y,X,wartosc" Y - wiersz(od 0), X - kolumna (od 0), wartosc - modyfikacja do wpisania w komórkę'''

reader = CSVReader(source, destination, changes)

if reader.validated == 'valid_csv':
    file_data = reader.get_file_data()
    for element in reader.changes:
        row_index, column_index, change_value = reader.validate_change(element)
        reader.mod_file(file_data, row_index, column_index, change_value)
    reader.create_output(file_data)
    
else:
    reader.show_files_in_dir()

