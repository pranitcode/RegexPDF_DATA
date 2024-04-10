from pdf2image import convert_from_path
from pytesseract import image_to_string
import re
import pycountry
import os

mastertext=""
eh_reference_regex = r'\bEH reference number\s*:\s*(\d{10})\b'
euler_regex = r'\bEuler N°\s*:\s*(\d{10})\b'
telephone_regex = r'Telephone\s*:\s*\((\d{3})\) (\d{1,2} \d{3} \d{4})'
speed = ""

def extract_info_from_file(file_text):
    
    mastertext = file_text
    st = [line for line in mastertext.strip().split('\n') if line.strip()]
    # print(st)
    target_string1 = 'EH reference number'
    speed = get_next_index(st, target_string1)
    # print(speed)
    
    target_string2 = "Telephone :"
    telephone_number = get__telephone(st, target_string2) 
   
    target_string3 = "We would like to receive information about the company below"
    company_name = get__req_company_name(st, target_string3)
   
   
    # EH reference number
    eh_reference_number = re.search(eh_reference_regex, file_text)
    eh_reference_number = eh_reference_number.group(1) if eh_reference_number else None

    # Euler number
    euler_number = re.search(euler_regex, file_text)
    euler_number = euler_number.group(1) if euler_number else None

    # # Telephone number
    # telephone_number = re.search(telephone_regex, file_text)
    # telephone_number = telephone_number.group(0) if telephone_number else None
    
    # Date
    date_regex = r'\b(\d{1,2}(?:st|nd|rd|th)?(?:\s+\w+)?(?:\s+\d{4})?)\b'
    date_match = re.search(date_regex, file_text)
    date = date_match.group(1).strip() if date_match else None

    # Address
    address_regex = r"We would like to receive information about the company below:(.*?)(?:Telephone|\b\w+\s*:(?! \d))"
    address_match = re.search(address_regex, file_text, re.DOTALL)
    address = address_match.group(1).strip() if address_match else None

    return eh_reference_number, euler_number, telephone_number, address, date, speed, company_name

# Define function to convert PDF to text
def convert_pdf_to_text(pdf_file):
    images = convert_from_path(pdf_file)
    text = ""
    for img in images:
        text += image_to_string(img)
    # print(text)    
    return text

# Define function to extract information from a PDF file

def extract_info_from_pdf(pdf_file):
    text = convert_pdf_to_text(pdf_file)
    return extract_info_from_file(text)
    
# Define function to find country in address lines
def countryfind(address_lines):
    for country in pycountry.countries:
        if country.name in address_lines:
            return country.name  
    return None

def get_next_index(lst, target_string):
    for i in range(len(lst)):
        if target_string in lst[i]:
             return lst[i+1] if i+1 < len(lst) else None
    return None


def get__telephone(lst, target_string):
    for i in range(len(lst)):
        if target_string in lst[i]:
             return lst[i] if i < len(lst) else None
    return None

def get__req_company_name(lst, target_string):
    for i in range(len(lst)):
        if target_string in lst[i]:
             return lst[i+2] if i+2 < len(lst) else None
    return None


# Directory containing PDF files
pdf_directory = './'

# Iterate over all PDF files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_file = os.path.join(pdf_directory, filename)
        eh_reference, euler_number, telephone_number, address, date, speed, company_name = extract_info_from_pdf(pdf_file)
        address_lines = address.strip().split('\n')
        
        # Check if the first index is empty or contains only a colon
        clearAddress = ""
        if address_lines[0].strip() == '' or ':' in address_lines[0]:
          joined_address = '\n'.join(address_lines[1:])
          clearAddress = joined_address
            
        # print(address_lines)
        country = countryfind(address_lines)
        
        address_combined = " ".join(line.strip() for line in address_lines[1:] if line.strip())
        # Print extracted information
  
        print("---------File:", filename, "------------")
        print("Date:", date)
        print("EH reference number:", eh_reference)
        print("Euler number:", euler_number)
        print("Tel:", telephone_number)
        print("Address:", address_combined)
        print("Country:", country)
        print(address_lines[0])
        print("Requested company Name:", company_name )
        print("Speed:", speed)
        



