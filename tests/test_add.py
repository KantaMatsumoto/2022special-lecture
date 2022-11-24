import unittest

from speciallecture.CSVFileWriterPrinter import CSVFileWriterPrinter

    
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