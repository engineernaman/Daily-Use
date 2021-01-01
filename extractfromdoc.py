#! python3

import re, pyperclip
# TODO: Create regex for phone numbers.
phreg = re.compile(r'\d{10}',re.VERBOSE)

# TODO: Create regex for email addresses.
emailreg = re.compile(r'''


[a-zA-Z0-9.+_]+   #for name
@
[a-zA-Z0-9.+_]+    # for domain
[.]?
[a-zA-Z0-9.+_]+



''',re.VERBOSE)

# TODO: Get text off the clip board.
text = pyperclip.paste()

# TODO: Extract the email/ph no from this text file.
extractedph = phreg.findall(text)
extractedem = emailreg.findall(text)


print(extractedph)
print(extractedem)

#TODO: Copy the email and ph no to clipboard

results = '\n'.join(extractedph) + '\n\n\ns' + '\n'.join(extractedem)
pyperclip.copy(results)
