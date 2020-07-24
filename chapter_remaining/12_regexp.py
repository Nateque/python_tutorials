import re

# mystr = '''Tata Motors Limited, formerly Tata Engineering and Locomotive Company, is an Indian multinational automotive manufacturing company headquartered in Mumbai, Maharashtra, India. It is a part of Tata Group, an Indian conglomerate. Wikipedia
# Stock price: TATAMOTORS (NSE) ₹106.00 +0.85 (+0.81%)
# 23 Jul, 3:30 pm IST - Disclaimer
# Customer service: 18002-7979
# CEO: Guenter Butschek (15 Feb 2016–)
# Parent organization: Tata Group
# Divisions: Tata Motors Cars
# Headquarters: Mumbai'''

# patt = re.compile(r'1800')
# patt = re.compile(r'.Limited') # any characters
# patt = re.compile(r'^Tata') # starts with
# patt = re.compile(r'bai$') # ends with
# patt = re.compile(r'But*') # zero or more occurance
# patt = re.compile(r'But+') # one or more
# patt = re.compile(r'Tata{1}') # exactly one
# patt = re.compile(r'.Limited|Tata{1}') # Either or

# special sequences
# patt = re.compile(r'\ATata') # beginning
# patt = re.compile(r'Tata\b') # beginning or end
# patt = re.compile(r'\d{5}-\d{4}') 

# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# indian phone numbers 
phone_numbers = ''' +91-8959685748
+91-8959684568
+91-8959687596
+91-8959681243
+91-8959689564
+91-8959689856
+91-8959681236
+91-8959687532
+91-8959684596
+91-8959681237
+91-8959687934
+91-8959689761
+91-8959685496
+91-8959685256'''

num = re.compile(r'\d{2}-\d{10}')

matches = num.finditer(phone_numbers)
for match in matches:
    print(match)