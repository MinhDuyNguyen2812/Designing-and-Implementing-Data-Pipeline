class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        rows = []
        try: 
            filehandler = open(self.filepath, 'r', encoding='utf-8')
            row = filehandler.readline()
            while row != '':
                rows.append(row.rstrip('\n'))
                row = filehandler.readline()
            filehandler.close()
        except Exception:
            print(f"Failed to read file '{self.filepath}'")
            exit(-1)
        return rows