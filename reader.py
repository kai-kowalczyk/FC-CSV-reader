import sys
from pathlib import Path
from lib import CSVReader

source = sys.argv[1]
destination = sys.argv[2]
changes = sys.argv[3:]
print(len(changes))

'''changes "Y,X,wartosc" Y - wiersz(od 0), X - kolumna (od 0), wartosc - modyfikacja do wpisania w komórkę'''

reader = CSVReader(source, destination, changes)

if reader.validated == 'valid_csv':
    reader.validate_change()
    
else:
    reader.show_files_in_dir()

