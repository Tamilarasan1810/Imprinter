# import win32print

# printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)

# print("Available Printers:")
# for printer in printers:
#     print(printer)

# file_path = 'D:\Imprinter\Java_notes_valli.pdf'
# printer_name = 'Virtual printer'
# file_handler = open(file_path, 'rb')
# printer_handler = win32print.OpenPrinter(printer_name)
# job_info = win32print.StartDocPrinter(printer_handler, 1, (file_path, None, "RAW"))

# # Specify the number of pages to print
# num_pages_to_print = 5
# page_counter = 0

# while page_counter < num_pages_to_print:
#     win32print.StartPagePrinter(printer_handler)
#     data = file_handler.read()

#     if data:
#         test = win32print.WritePrinter(printer_handler, data)
#         print(test)

#     win32print.EndPagePrinter(printer_handler)
#     page_counter += 1

# win32print.EndDocPrinter(printer_handler)


#######################
#######################
import win32print

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)

print("Available Printers:")
for printer in printers:
    print(printer)

file_path = r'D:\Imprinter\Java_notes_valli.pdf'  # Use raw string to avoid escape characters
printer_name = 'Virtual printer'

file_handler = open(file_path, 'rb')
printer_handler = win32print.OpenPrinter(printer_name)
job_info = win32print.StartDocPrinter(printer_handler, 1, (file_path, None, "RAW"))

# Specify the number of pages to print
num_pages_to_print = 5
page_counter = 0

while page_counter < num_pages_to_print:
    win32print.StartPagePrinter(printer_handler)
    data = file_handler.read()

    if data:
        test = win32print.WritePrinter(printer_handler, data)
        print(test)

    win32print.EndPagePrinter(printer_handler)
    page_counter += 1

win32print.EndDocPrinter(printer_handler)

file_handler.close()
