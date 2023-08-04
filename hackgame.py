# Hacking Version 2
# This is a text-based password guessing game that displays a
# list of potential computer passwords. The player is allowed
# 1 attempt to guess the password. The game indicates that the
# player failed to guess the password correctly.


# create window
print('HACKING')

# display header
print('DEBUG MODE')
print('1 ATTEMPT(S) LEFT')
print('')

# display password list
print('PROVIDE')
print('SETTING')
print('CANTINA')
print('COTTING')
print('HUNTERS')
print('SURVIVE')
print('HEARING')
print('HUNTING')
print('REALIZE')
print('NOTHING')
print('OVERLAP')
print('FINDING')
print('PUTTING')
print('')

guess = input('Enter password >')

# end game
#   clear window
#   display failure outcome
#       display guess
print(guess)

#       display blank line
print('')

#       display failure line 2
print('LOGIN FAILURE - TERMINAL LOCKED')

#       display blank line
print('')

#       display failure line 3
print('PLEASE CONTACT AN ADMINISTRATOR')

#       display blank line
print('')

#   prompt for end
input('PRESS ENTER TO EXIT')
