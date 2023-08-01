import win32print
import win32con

def print_file(file_path, printer_name, pages_to_print=None, color_mode=None, orientation=None, pages_per_paper=None):
    # Open the file in binary mode
    file_handler = open(file_path, 'rb')

    # Open the printer
    printer_handler = win32print.OpenPrinter(printer_name)

    try:
        # Start a print job
        job_info = win32print.StartDocPrinter(printer_handler, 1, (file_path, None, "RAW"))

        # Start a page in the print job
        win32print.StartPagePrinter(printer_handler)

        # Specify the printer features
        if color_mode is not None:
            devmode = win32print.GetPrinter(printer_handler, 9)["pDevMode"]
            devmode.Orientation = orientation
            devmode.Color = color_mode
            win32print.SetPrinter(printer_handler, 9, devmode, 0)

        # Print specific pages if specified
        if pages_to_print is not None:
            current_page = 1
            for page in pages_to_print:
                if isinstance(page, int):
                    if page == current_page:
                        win32print.WritePrinter(printer_handler, file_handler.read())
                        current_page += 1
                elif isinstance(page, str):
                    range_pages = page.split('-')
                    start_page = int(range_pages[0])
                    end_page = int(range_pages[1]) if len(range_pages) > 1 else start_page
                    if start_page <= current_page <= end_page:
                        win32print.WritePrinter(printer_handler, file_handler.read())
                        current_page += 1

        # Print all pages if pages_to_print is not specified
        else:
            win32print.WritePrinter(printer_handler, file_handler.read())

        # End the page in the print job
        win32print.EndPagePrinter(printer_handler)

        # End the print job
        win32print.EndDocPrinter(printer_handler)

    finally:
        # Close the printer
        win32print.ClosePrinter(printer_handler)

        # Close the file
        file_handler.close()


# Example usage:
file_path = r'D:\Imprinter\Java_notes_valli.pdf'
printer_name = 'Virtual printer'

# Specify the pages to print as an array of numbers or ranges
pages_to_print = [1, 3, '4-9']

# Specify the color mode: 1 for colored, 2 for black and white
color_mode = 2

# Specify the orientation: 1 for portrait, 2 for landscape
orientation = 1

# Specify the number of pages per paper
pages_per_paper = 2

# Print the file with the specified settings
print_file(file_path, printer_name, pages_to_print, color_mode, orientation, pages_per_paper)
