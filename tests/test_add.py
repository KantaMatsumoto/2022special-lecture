import unittest
#from test_CSVPrinter import CSVFileWriterPrinter
import csv

class CSVFileWriterPrinter:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines
    
class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVFileWriterPrinter("sample.csv")
        l = printer.read()
        print(l)
        self.assertEqual(3, len(l))
    
    def test_read2(self):
        printer = CSVFileWriterPrinter("sample.csv")
        l = printer.read()
        print(l[1][1])
        self.assertEqual('bbb2', l[1][1])
    
    def test_read3(self):
        # try:
        #     printer = CSVFileWriterPrinter("notsample.csv")
        #     printer.read()
        #     unittest.TestCase.fail('This line should be invoked')
        # except:
        #     print("error")
        with self.assertRaises(FileNotFoundError) as e:
            printer = CSVFileWriterPrinter("notsample.csv")
            printer.read()
        raise FileNotFoundError(e)  ## 例外を上げる処理（メソッド）をここに書く


test = TestCSVPrinter()
test.test_read1()
test.test_read2()
test.test_read3()