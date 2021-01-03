from sys import exit

def check_upper(input):
    uppers = 0 
    upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for char in input:
        if char in upper_list:
            uppers += 1
    if uppers > 0:
        return True
    else:
        return False

def check_lower(input):
    lowers = 0
    lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for char in input:
        if char in lower_list:
            lowers += 1
    if lowers > 0:
        return True
    else:
        return False

def check_number(input):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0".split()
    for char in input:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False

def check_special(input):
    specials = 0
    special_list = "! @ $ % ^ & * ( ) _ - + = { } [ ] | \ , . > < / ? ~ ` \" ' : ;".split()
    for char in input:
        if char in special_list:
            specials += 1
    if specials > 0:
        return True
    else:
        return False

def check_len(input):
    if len(input) >= 8:
        return True
    else:
        return False


def validate_password(input):
    check_dict = {
        'upper': check_upper(input),
        'lower': check_lower(input),
        'number': check_number(input),
        'special': check_special(input),
        'len' : check_len(input)
    }
    if check_upper(input) & check_lower(input) & check_number(input) & check_special(input) & check_len(input):
        return True
    else:
        print "Invalid password! Review below and change your password accordingly!"
        print
        if check_dict['upper'] == False:
            print "Password needs at least one upper-case character."
        if check_dict['lower'] == False:
            print "Password needs at least one lower-case character."
        if check_dict['number'] == False:
            print "Password needs at least one number."
        if check_dict['special'] == False:
            print "Password needs at least one special character."
        if check_dict['len'] == False:
            print "Password needs to be at least 8 characters in length." 
        print                  

while True:
    password = raw_input("Enter desired password: ")
    print 
    if validate_password(password):
        print "Password meets all requirements and may be used."
        print 
        print "Exiting program..."
        print
        exit(0)
