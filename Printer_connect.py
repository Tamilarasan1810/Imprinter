import win32print

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,None,1)

print("Available Printer: ")
for printer in printers:
    print(printer)

# file_path='D:\\Imprinter\\test_file.txt'
file_path='D:\Imprinter\Examination_Result.pdf'

printer_name='Virtual printer'

file_handler = open(file_path,'rb')

printer_handler = win32print.OpenPrinter(printer_name)

jop_info = win32print.StartDocPrinter(printer_handler,1,(file_path,None,"RAW"))

win32print.StartPagePrinter(printer_handler)


test = win32print.WritePrinter(printer_handler,file_handler.read())
print(test)

win32print.EndPagePrinter(printer_handler)

win32print.EndDocPrinter(printer_handler)



# Youtube video link:  https://www.youtube.com/watch?v=ii28Nn9WENQ

