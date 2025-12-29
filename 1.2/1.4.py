#oop for data science
class dataset:
    def __init__(self,name,size):
        self.name=name
        self.size=size
    def info(self):
        return f"Dataset:{self.name},size:{self.size}"
class CSVdata(dataset):
    def file_type(self):
        return "CSV file"

data=CSVdata("sales data", 5000)
print(data.info())
print(data.file_type())