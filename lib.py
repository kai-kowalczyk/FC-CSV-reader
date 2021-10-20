from pathlib import Path
import csv

class CSVReader:

    ALLOWED_EXTENSIONS = ('csv')

    def __init__(self, path=None, destination=None, *changes):
        self.filename = Path(path).name
        print(self.filename)
        self.path = path
        self.parent_path = Path(self.path).parent  
        self.destination = destination
        self.changes = list(changes)
        self.cwd = Path.cwd()
        self.filetype = self.set_filetype()
        print(self.filetype)
        self.validated = self.validate_source()
              
        

    def validate_source(self):
        print(self.path)
        if Path(self.path).exists():
            if Path(self.path).is_file():
                if self.filetype not in self.ALLOWED_EXTENSIONS:
                    print('Nieobsługiwany format.')
                    return 'wrong_ext'
                else:
                    print('val - valid_csv')
                    return 'valid_csv'
            else:
                print('val - valid_path')
                #self.show_files(path)
                return 'valid_path'
        else:
            print('val - invalid_path')
            print(self.parent_path)
            if Path(self.parent_path).is_dir():
                return 'valid_parent_path'
            else:
                return 'invalid_path'
            #self.show_files(self.cwd)

    def set_filetype(self):
        print('*', Path(self.filename).suffix[1:])
        return Path(self.filename).suffix[1:]



    def show_files_in_dir(self):
        if self.validated == 'wrong_ext':
            print('show - wrong_ext')
            print(sorted(Path(self.parent_path).glob('*.csv')))
        elif self.validated == 'valid_path':
            print('show - valid path')
            print(sorted(Path(self.path).glob('*.csv')))
        elif self.validated == 'valid_parent_path':
            print('show - valid parent path')
            print(sorted(Path(self.parent_path).glob('*.csv')))
        else:
            print('show - invalid_path')
            print(sorted(Path(self.cwd).glob('*.csv')))

    def validate_change(self):
        pass
            
            
    def mod_file(self):
        pass