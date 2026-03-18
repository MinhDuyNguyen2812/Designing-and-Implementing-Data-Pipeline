class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        rows = []
        try: 
            filehandle = open(self.filepath, 'r', encoding='utf-8')
            row = filehandle.readline()
            while row != '':
                rows.append(row.rstrip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f"Failed to read file '{self.filepath}'")
            exit(-1)
        return rows
    
    def write(self, rows):
        try:
            filehandle = open(self.filepath, 'w', encoding='utf-8')
            for row in rows:
                filehandle.write(f"{row}\n")
            filehandle.close()
        except Exception:
            print(f"Failed to write file '{self.filepath}.")
            exit(-1)
        return None
