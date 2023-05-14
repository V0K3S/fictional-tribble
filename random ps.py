import random
import re


variables = '0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm~!@#$%^&*()_-+=|\}]{[]}",<.>?/'
variables_numbers = '0123456789'
variables_alphabetscaps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
variables_alphabetssmall = 'qwertyuiopasdfghjklzxcvbnm'
variables_symbols = '~!@#$%^&*()_-+|\}]{[]}",<.>?/'


new_password = random.choice(variables_alphabetscaps) + random.choice(variables_numbers) + random.choice(variables_numbers) + random.choice(variables_alphabetssmall) + random.choice(variables_symbols) + random.choice(variables_alphabetssmall) + random.choice(variables_alphabetscaps) + random.choice(variables_symbols)

decision = input('Press G to generate a random complex password ')

if decision.upper() == 'G':
    print('your new password is ' + str(new_password))
else:
    print('Gerrarahere mehn!!!')
