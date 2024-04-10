def get_next_index(lst, target_string):
    for i in range(len(lst)):
        if target_string in lst[i]:
            return lst[i+1] if i+1 < len(lst) else None
    return None

# Example usage
address_lines = ['Allianz @i) “ede', '12th February 2024', 'Enquiry request', 'Euler N° : 0122013391 Business Information Report Normal', 'EH reference number : 0003708126', '3', '0178341997', 'Madan, Sir,', 'We would like to receive information about the company below:', 'RN Saudi Arabia : 2055102557', 'Lamsat Al Asaar Trading Co. Limited', 'Liability Company', 'LLC', 'Lamsat Al Asaar Building, Riyadh', 'Hay Al Safa, Jubail City Center', 'Jubail', 'EPR', '31951', '30285', 'SA', 'Saudi Arabia', 'Telephone : (966) 13 362 0667', 'Yours faithfully,', 'Euler Hermes Services GCC Ltd.', 'Acompany incorporated at Dubai International Finance Centre under Register Company number 1494', 'www.allianz-trade.ae', '1/1', 'Allianz Trade is the trademark used to designate a range of services provided by Euler Hermes.']


target_string = 'EH reference number'

speed = get_next_index(address_lines, target_string)
print(next_index)





