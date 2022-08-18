#MOMUNOV IMRAN
#TP056103

import os           #Importing libraries
import datetime

def clear():            #Function will clear the screen
    os.system('cls')

def error():            #This function will be calling after wrong input
    print('Invalid input, please try again\n')

def mainmenu():         # Function of Main Menu page
    clear()
    print('========== Main Menu =========='.center(65))
    while True:         #This loop will be repeating until it gets right input, if so, this input will be returned from this function.
        try:
            menu = int(input('Select your role: \n1. Admin\n2. Registered User \n3. New User \n0. Exit \n'))
            clear()
            return menu
        except:
            clear()
            error()
            pass

def login():            # To get login from user
    log = input('Enter your login: ')
    log = log.lower()   #Make input lowercase to correct working of search further
    return log

def password():
    pas = input('Enter your password: ')
    return pas          #Passwords shoud be case sensitive, so no need to lower or upper it

def tran_cust():        #admin menu of customer transactions
    menu = int(input('Select: \n1. Specific Customer \n2. All Customers \n8. Go Back \n9. Log Out \n0. Exit  \n'))
    return menu

def menu_admin():       #main menu of admin
    menu = int(input('Select: \n1. Registration Requests \n2. Transactions \n9. Log Out \n0. Exit \n'))
    clear()
    return menu

def new_request():      #if there is new registration, this function will be called
    print('New Registration request detected!')
    print('UserID: ', current_user())
    req = int(input('1. Approve \n8. Go Back \n9. Log Out \n0. Exit \n'))
    clear()
    return req

def transactions():     #admin menu for all transactions, both customers and loan
    print('========== Transactions =========='.center(65))
    tran_act = int(input('Select which transactions you want to see: \n1. Customers \n2. Loans \n8. Go Back \n9. Log Out \n0. Exit  \n'))
    clear()
    return tran_act

def menu_newC():        #Main menu for New Users
    while True:         #This loop will be repeating until it gets right input, if so, this input will be returned from this function.
        try:
            menu = int(input('Select: \n1. Registration \n2. Check load detail \n3. Loan Calculator \n9. Log Out \n0. Exit \n'))
            clear()
            return menu
        except:
            clear()
            error()

def loan_menu():        #Admin menu for Loans
    menu = int(input('Select type of loan: \n1. Education Loan  \n2. Car Loan  \n3. Home Loan \n4. Personal Loan  \n8. Go back \n9. Log Out \n0. Exit \n'))
    clear()
    return menu

def back():             #Just waits fot enter to go back
    press = input('\nPress enter to go back \n')
    clear()

def calculator(rate):   #Calculator for New customers, to count their loans
    while True:
        try:
            LnAmnt = int(input('Enter Loan Amount: '))
            LnTrm = int(input('Enter Loan Term in Years: '))
            LnTrm *= 12
            PerIntR = rate/12
            mont_p = ((LnAmnt/(((1+PerIntR)**LnTrm)-1))*(PerIntR*(1+PerIntR)**LnTrm))
            print('Your Monthly payment is: ', round(mont_p, 2), 'RM')
            print('Your Total payment is:', round((mont_p*LnTrm), 2), 'RM')
            back()
            break
        except:
            error()

def calculator_auto():      #Calculator which will automatically calculate loan amount and loan payment per month
    LnType = int(user_loanInfo(10))
    if LnType == 1:
        rate = 0.045
    elif LnType == 2:
        rate = 0.07
    elif LnType == 3:
        rate = 0.06
    elif LnType == 4:
        rate = 0.075
    LnAmnt = int(user_loanInfo(12))
    LnTrm = int(user_loanInfo(11))
    LnTrm *= 12
    PerIntR = rate / 12
    mont_p = ((LnAmnt / (((1 + PerIntR) ** LnTrm) - 1)) * (PerIntR * (1 + PerIntR) ** LnTrm))
    return round(mont_p, 2)

def letter_check(str):      #Function will check if argument has allowed symbols. will be used to validate registration details input
    allowedsym = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0 -')
    check = True
    if str == '':
        error()
        return False
    for i in range(0, len(str)):
        if str[i] not in list(allowedsym):
            print('Invalid syntax, input can contain only: \nA-Z, a-z, and \'-\' , please try again')
            return False
    return check

def symbols_check(str):     #Function will check if argument has allowed symbols. will be used to validate registration details input
    allowedsym = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_/ .-+=!;@%^&*()')
    check = True
    if str == '':
        error()
        return False
    for i in range(0, len(str)):
        if str[i] not in list(allowedsym):
            print('Invalid syntax, input can contain only: \nA-Z, a-z, 0-9 and \'_/ .-+=!;@%^&*()\'\' symbols, please try again')
            return False
    return check

def num_check(x):           #Function will check if argument has only numbers. will be used to validate registration details input
    allowednum = ('1234567890')
    if x == '':
        error()
        return False
    for i in range(0, len(str(x))):
        if str(x)[i] not in list(allowednum):
            print('Invalid input, please try again')
            return False
    return True

def registration():     #Main logic of registration page. It has all validations inside. if anything wrong, will ask user again or stop functioning itself, not whole program.
    while True:
        print('====================Registration====================\nEnter 0 anywhere to go back\n\n')
        while True:
            username = input('Enter your First Name: ')
            if letter_check(username):
                break
            else:
                pass
        if username == '0':
            break
        while True:
            usersurname = input('Enter your Second Name: ')
            if letter_check(usersurname):
                break
        if usersurname == '0':
            break
        while True:
            useraddress = input('Enter your home Address: ')
            if symbols_check(useraddress):
                break
        if useraddress == '0':
            break
        while True:
            useremail = input('Enter your Email: ')
            if symbols_check(useremail):
                break
        if useremail == '0':
            break
        while True:
            usercontactnum = input('Enter your Contact Number: ')
            if symbols_check(usercontactnum):
                break
        if usercontactnum == '0':
            break
        while True:
            try:
                userGen = int(input('Choose your Gender: \n1. Male \n2. Female\n'))
                if userGen == 1 or userGen == 2 or userGen == 0:
                    break
                else:
                    error()
            except:
                error()
        if userGen == 0:
            break
        while True:
            userbirthday = input('Enter your birthday in YYYY-MM-DD format:')
            if symbols_check(userbirthday):
                break
        if userbirthday == '0':
            break
        while True:
            try:
                userloantype = int(input('Select your Loan Type: \n1. Education Loan  \n2. Car Loan  \n3. Home Loan \n4. Personal Loan\n'))
                allowedinp = ('12340')
                if str(userloantype) in list(allowedinp):
                    break
                else:
                    error()
            except:
                error()
        if userloantype == 0:
            break
        while True:
            try:
                userloanterms = int(input('Enter Loan Term in years: '))
                if userloanterms > 40:          #people not even live so many years
                    print('You cannot apply for a loan for more than 40 years')
                elif num_check(userloanterms):
                    break
                else:
                    pass
            except:
                error()
        if userloanterms == 0:
            break
        while True:
            try:
                useramount = int(input('Enter Installment Amount: '))
                if useramount > 10000000:           # application should has some limits
                    print('You cannot apply for a loan greater than 10,000,000 RM')
                elif num_check(useramount):
                    break
                else:
                    pass
            except:
                error()
        if useramount == 0:
            break
        while True:
            userID = input('Enter UserID: ')
            userID = userID.lower()
            allowedsym = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
            check = 1
            for i in range(0, len(userID)):
                if userID[i] not in list(allowedsym):
                    print('Invalid syntax, your UserID can contain only: \nA-Z, a-z, 0-9 and \'_\' , please try again')
                    check = 0
            if not log_similar(userID):
                print('This UserID is already taken, please try again')
            elif check == 0:
                pass
            else:
                break
        while True:
            userpass1 = input('Enter your password: ')
            userpass2 = input('Re-Enter your password: ')
            if userpass1 != userpass2:
                print('Passwords are not same, try again!')
            else:
                break
        print('Congratulations! Once Administrator approve your registration request, you can login as Registered User')
        file = open('userinfo.txt', 'a+')
        file.write(userID + '$' + userpass2 + '$' + username + '$' + usersurname + '$' + useraddress + '$' + useremail + '$' + usercontactnum + '$' + str(userGen) + '$' + userbirthday + '$' + str(userloantype) + '$' + str(userloanterms) + '$' + str(useramount) + '$' + ':' + '\n')
        file.close()
        back()
        clear()
        break

def current_user():     #Current user, will be used to take current user which is not approved yet.
    with open('userinfo.txt') as user:
        id = user.readlines()
    for i in range(0, len(id)):
        if ':' in id[i]:            #":" sign in userinfo means that user is not approved yet.
            return get_log(i)

def approve_user():       #will delete ":" sign from userinfo when account is approved, instead will put "!"
    userid = current_user()
    with open('userinfo.txt', 'r') as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        if userid in lines[i]:
            lines[i] = lines[i].replace(':', '!', 1)
    with open('userinfo.txt', 'w') as file:
        file.writelines(lines)

def notapproved_accounts():     #counter of how much not approved accounts are there
    count = 0
    with open('userinfo.txt') as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        if ':' in lines[i]:
            count += 1
    return count

def approve_check(num4):        #will check specific account on approving
    with open('userinfo.txt') as user:
        id = user.readlines()
    if ':' in id[num4]:
        passing = False
        return passing
    passing = True
    return passing

def logRegUs():         #menu for registered user
    print('========== User =========='.center(65))
    menu = int(input('Select one: \n1. Check Loan Details \n2. Pay Loan Installment \n3. Transactions \n4. Status of Loan \n9. Log Out \n0. Exit \n'))
    clear()
    return menu

def get_log(x):         #will get login from userinfo file from line number x
    with open('userinfo.txt') as fp:
        lines = fp.readlines()
    line = lines[x]
    num2 = 0
    num3 = line.find('$')
    out_string = str(line[num2:num3])
    return out_string

def num_line(num , log):       #will return number of line in userinfo file of specific user.
    for i in range(0, num):
        out_str = get_log(i)
        if log == out_str:
            return i
    return False

def num_line2(num, log):        #will return number of line in userinfo file of specific user.
    for i in range(0, num+1):
        out_str = get_log(i)
        if log == out_str:
            return i
    return False

def log_similar(log):       #check for similarity of login in file and argument log, which is input from user
    num = int(number_lines())
    for i in range(0, num):
        login_check = get_log(i)
        if log == login_check:
            return False
    return True

def user_info(num, i):      #will return user information, arguments is numbers of index and line of user information. for example index of name is 2
    with open('userinfo.txt') as fp:
        line = fp.readlines()
    lines = line[i]
    for i in range(0, num-1):
        lines = lines.replace('$', '!', 1)
    num2 = lines.find('$')
    lines = lines.replace('$', '!', 1)
    num3 = lines.find('$')
    out_string = str(lines[(num2+1):num3])
    return out_string

def get_pass(x):        #returns password of specific line, which number is x
    with open('userinfo.txt') as fp:
        lines = fp.readlines()
    line = lines[x]
    num2 = line.find('$')
    line = line.replace('$', '!', 1)
    num3 = line.find('$')
    out_string = str(line[(num2+1):num3])
    return out_string

def number_lines():     #counter of total numbers line. will be used in some functions
    with open('userinfo.txt') as fp:
        lines = fp.readlines()
    num = len(lines)
    return num

def loan_details(log):      #this function will be called when user click to show loan details.
    with open('loan_info.txt') as lines:  #opens file
        line = lines.readlines()
    for i in range(0, len(line)):       #searchs in which line login of user is located
        if log in line[i]:
            line = line[i]
            break
    num1 = line.find('$')               #takes all information from that user line
    line = line.replace('$', '!', 1)
    num2 = line.find('$')
    loanid = line[(num1+1):num2]

    line = line.replace('$', '!', 1)
    num1 = line.find('$')
    loan = line[(num2 + 1):num1]

    line = line.replace('$', '!', 1)
    num2 = line.find('$')
    loandate = line[(num1 + 1):num2]

    line = line.replace('$', '!', 1)
    num1 = line.find('$')
    loantype = line[(num2 + 1):num1]

    line = line.replace('$', '!', 1)
    num2 = line.find('$')
    loanterms = line[(num1 + 1):num2]

    line = line.replace('$', '!', 1)
    num1 = line.find('$')
    totalloan = line[(num2 + 1):num1]

    loantype = loantype_conv(loantype)

    print('Your LoanID: ', loanid)          #and here will print all information
    print('Your Loan Type: ', loantype)
    print('Your Loan Installment Date: ', loandate)
    print('Your Payment per month: ', loan, 'RM')
    print('Your Total Payment: ', totalloan, 'RM')
    print('Your Loan terms: ', loanterms, 'years')

    back()

def monthpay(log):          # will return monthly payment of particular user
    with open('loan_info.txt') as lines:        #opens file
        line = lines.readlines()                #reads all lines
    for i in range(0, len(line)):               #searchs in which line user's login
        if log in line[i]:                      #after found, take month payment from there
            line = line[i]
            line = line.replace('$', '!', 1)
            num1 = line.find('$')
            line = line.replace('$', '!', 1)
            num2 = line.find('$')
            out_string = str(line[(num1 + 1):(num2)])
            return out_string

def tran_made(log):         #will count all user's transactions made
    var = 0
    with open('transactions.txt') as lines:
        line = lines.read()
    while True:
        if log in line:
            line = line.replace(log, '!', 1)
            var += 1
        else:
            break
    return var

def remaining(log, num):        #will count how many transactions is remained to pay for particular user
    var = tran_made(log)
    return (int(user_info(10, num))*12 - var)

def pay_loans(log, num4):       #will be called when user wants to pay loan.
    print('Your Monthly Payment is: ', monthpay(log))           # function reduces payments remaining for 1 and writes new transaction to transaction file
    print('Payments remaining: ', remaining(log, num4))
    ans = input('Press Enter to confirm payment')
    trans = open('transactions.txt', 'a+')
    lower = log.lower()
    trans.write(lower + '$' + user_info(9, num4) + '$' + str(datetime.date.today()) + '$' + monthpay(log) + '\n')
    print('Successful!')
    back()

def user_loanInfo(x):       #will return informatino of current user , x is index of information is needed
    info_index = x
    log = current_user()
    user_line = num_line2(int(number_lines()), log)
    return user_info(info_index - 1, user_line)

def loantype_conv(var):     #converts integer of loan types to text
    var = int(var)
    if var == 1:
        return 'Educational'
    elif var == 2:
        return 'Car'
    elif var == 3:
        return 'Home'
    elif var == 4:
        return 'Personal'

def loantype_conv_x(str):      #works opposite to previous function
    if str == 'Educational':
        return 1
    elif str == 'Car':
        return 2
    elif str == 'Home':
        return 3
    elif str == 'Personal':
        return 4

def loanid_gen():       # this will generate loanID for user. it simply takes 2 characters the same as loan type
    LoanType = int(user_loanInfo(10))           #Then it adds number of line to this characters
    first_char = 'null'                         #if number is short, it will add 0 to make it 4 digit number
    if LoanType == 1:                           #at the end it shoud be like that: EL0001
        first_char = 'EL'
    elif LoanType == 2:
        first_char = 'CL'
    elif LoanType == 3:
        first_char = 'HL'
    elif LoanType == 4:
        first_char = 'PL'
    with open('loan_info.txt') as fp:
        lines = fp.readlines()
    num = 1 + len(lines)
    for i in range(1, 4):
        if len(str(num)) != 4:
            num = '0' + str(num)
    final_id = first_char + str(num)
    return final_id

def spec_tran():                # This is admin's functuion. will show specific user's transactions
    id = input('Enter specific user\'s ID: ')
    id = id.lower()
    with open('transactions.txt') as lines:
        line3 = lines.readlines()
    with open('transactions.txt') as lines:
        file = lines.read()
    if id in file:
        print('All transactions of', id, 'are shown: \nUserID\t\tPayment Amount\t\tDate of payment\t\tLoan Type')
        for i in range(0, len(line3)):
            var = line3[i]
            login = var[0:line3[i].find('$')]
            if id == login:
                line = line3[i]
                num1 = line.find('$')
                line = line.replace('$', '!', 1)
                num2 = line.find('$')
                loantype = line[(num1 + 1): num2]
                loantype = loantype_conv(loantype)
                line = line.replace('$', '!', 1)
                num1 = line.find('$')
                date = line[(num2 + 1): num1]
                payment = line[(num1 + 1): -1]
                print(id, '\t\t', payment, 'RM', '\t\t', date, '\t\t', loantype)
    else:
        print('This user have not made any transactions yet')

def own_trans(log):             #this function is for registered users, it will show all user transactions.
    with open('transactions.txt') as lines:
        line3 = lines.readlines()
    with open('transactions.txt') as lines:
        file = lines.read()
    if log in file:
        print('All your transactions are shown: \nUserID\t\tPayment amount\t\tDate of payment\t\tLoan Type')
        for i in range(0, len(line3)):
            var = line3[i]
            login = var[0:line3[i].find('$')]
            if log == login:
                line = line3[i]
                num1 = line.find('$')
                line = line.replace('$', '!', 1)
                num2 = line.find('$')
                loantype = line[(num1 + 1): num2]
                loantype = loantype_conv(loantype)
                line = line.replace('$', '!', 1)
                num1 = line.find('$')
                date = line[(num2 + 1): num1]
                payment = line[(num1 + 1): -1]
                print(log, '\t\t', payment, 'RM', '\t\t', date, '\t\t', loantype)
        back()
    else:
        print('You don\'t have any transactions yet')

def all_trans():        #simply will show all transaction of all users of all loan types
    clear()
    with open('transactions.txt') as lines:
        line = lines.readlines()
    with open('transactions.txt') as lines:
        file = lines.read()
    if '$' in file:
        print('All transactions are shown: \nUserID\t\tPayment Amount\t\tDate of payment\t\tLoan Type')
        for i in range(0, len(line)):
            transaction = line[i]
            num1 = transaction.find('$')
            transaction = transaction.replace('$', '!', 1)
            num2 = transaction.find('$')
            id = transaction[0:num1]
            loantype = transaction[(num1 + 1): num2]
            loantype = loantype_conv(loantype)
            transaction = transaction.replace('$', '!', 1)
            num1 = transaction.find('$')
            date = transaction[(num2 + 1): num1]
            payment = transaction[(num1 + 1): -1]
            print(id, '\t\t', payment, 'RM', '\t\t', date, '\t\t', loantype)
        back()
    else:
        print('Transactions not found')

def loan_type_trans(lntype):            #function which will show all transactions of one specific loan type. loan type  is paraneter here.
    lntypeint = int(loantype_conv_x(lntype))
    loanexist = False
    with open('transactions.txt') as lines:
        line3 = lines.readlines()
    for i in range(0, len(line3)):
        line4 = line3[i]
        num9 = line4.find('$')
        line4 = line4.replace('$', '!', 1)
        num8 = line4.find('$')
        if str(lntypeint) == line4[num9+1:num8]:
            loanexist = True
            break
    if loanexist:
        print('Transactions of all', str(lntype), 'Loans are shown: \nUserID\t\tPayment Amount\t\tDate of payment\t\tLoan Type')
        for i in range(0, len(line3)):
            line = line3[i]
            num1 = line.find('$')
            log = line[0: num1]
            line = line.replace('$', '!', 1)
            num2 = line.find('$')
            loantype = line[(num1 + 1): num2]
            line = line.replace('$', '!', 1)
            num1 = line.find('$')
            date = line[(num2 + 1): num1]
            payment = line[(num1 + 1): -1]
            if str(loantype_conv(loantype)) == str(lntype):
                print(log, '\t\t', payment, 'RM', '\t\t', date, '\t\t', loantype_conv(loantype))
    else:
        print('Transactions of ', lntype, 'Loans not found')

def loan_status(log, num4):         #will show loan status to registered user.
    with open('loan_info.txt') as lines:
        line = lines.readlines()
    try:
        line1 = line[num4]
    except:
        line1 = line[num4-1]
    line1 = line1.replace('$', '!', 1)
    num1 = line1.find('$')
    line1 = line1.replace('$', '!', 1)
    num2 = line1.find('$')
    loanamount = float(line1[num1+1:num2])
    rem_pay = int(remaining(log, num4))
    made_tr = tran_made(log)
    if rem_pay > 0:
        print('Loan not repaid yet, payments remaining: ', rem_pay)
        print('Total payments made:', made_tr)
        print('Month payment: ', loanamount, 'RM')
        print('Total Amount remaining: ', loanamount * rem_pay, 'RM')
    elif rem_pay == 0:
        print('Loan was repaid!')
    back()

def info_educ():    #just information about educational loan
    print('Educational loan')
    print('This loan applies if you want to pay university, college or school fees')
    print('Interest rate per year is 4.5% ')
    back()

def info_car():     #just information about car loan
    print('Car loan')
    print('This loan applies if you want to buy a car')
    print('Interest rate per year is 7% ')
    back()

def info_home():        #just information about home loan
    print('Home loan')
    print('This loan applies if you want to buy a home')
    print('Interest rate per year is 6% ')
    back()

def info_pers():        #just information about personal loan
    print('Personal loan')
    print('This loan applies if you want to buy a home')
    print('Interest rate per year is 7.5% ')
    back()

def admin_logic():      #main logic of admin menu.
    while True:
        print('Enter 0 to go back\n')
        log_a = login()
        if log_a == '0':
            return 9
        pas_a = password()
        if pas_a == '0':
            return 9
        log_a_chk = get_log(0)
        pas_a_chk = get_pass(0)
        if log_a == log_a_chk and pas_a == pas_a_chk:
            clear()
            print('========== Admin =========='.center(65))
            while True:
                menu_adm1 = admin_next_logic()
                if menu_adm1 == 1:
                    menu_adm1 = menu_admin_reqs(menu_adm1)
                elif menu_adm1 == 2:
                    menu_adm1 = menu_admin_tran(menu_adm1)
                if menu_adm1 == 9:
                    menu1 = 9
                    return menu1
                elif menu_adm1 == 8:
                    pass
                elif menu_adm1 == 0:
                    exit()
                elif menu_adm1 != 1 and menu_adm1 != 2 and menu_adm1 != None:
                    error()
        else:
            print('Login or Password is incorrect, try again:')

def admin_next_logic():     #logic of admin menu
    log = 1
    while log == 1:
        while True:
            while True:
                try:
                    menu_adm1 = menu_admin()
                    return menu_adm1
                except:
                    clear()
                    error()

def menu_admin_reqs(menu_adm1):     #logic of admin request approval page
    while menu_adm1 == 1:
        new_req = notapproved_accounts()
        if new_req > 0:
            while True:
                try:
                    new_req_act = new_request()
                    break
                except:
                    error()
            if new_req_act == 1:
                LoanType = user_loanInfo(10)
                LoanTerms = user_loanInfo(11)
                LoanAmount = user_loanInfo(12)
                InsDate = datetime.date.today()
                LoanID = str(loanid_gen())
                InsAmount = calculator_auto()
                LoanTotal = (InsAmount * 12 * int(LoanTerms))
                print('Automatically generated LoanID to', current_user(), ': ', LoanID)
                print('Installment Amount: ', LoanAmount, 'RM')
                print('Installment date: ', InsDate)
                print('Loan type: ', loantype_conv(LoanType))
                print('Loan Terms: ', LoanTerms, 'Year[s] (', int(LoanTerms) * 12, ' Months )')
                print('Automatically calculated Loan payment per month is: ', InsAmount, 'RM')
                print('Total Loan Payment with rate is: ', LoanTotal, 'RM')
                approve = input('\nPress Enter to confirm Loan and approve Account')
                file = open('loan_info.txt', 'a+')
                file.write(current_user() + '$' + LoanID + '$' + str(InsAmount) + '$' + str(
                    InsDate) + '$' + LoanType + '$' + LoanTerms + '$' + str(LoanTotal) + '$' + LoanAmount + '$' + '\n')
                file.close()
                approve_user()
                print('Approved')
                new_req -= 1
            elif new_req_act == 8:
                clear()
                menu_adm1 = 8
                return menu_adm1
            elif new_req_act == 9:
                clear()
                menu_adm1 = 9
                return menu_adm1
            elif new_req_act == 0:
                exit()
        if new_req == 0:
            print('No New Registration requests')
            break

def menu_admin_tran(menu_adm1):     #logic of admin menu of transactions
    while True:
        while True:
            try:
                tran_act = transactions()
                break
            except:
                clear()
                error()
        while tran_act == 1:
            clear()
            while True:
                try:
                    menu_cust = tran_cust()
                    break
                except:
                    error()
            if menu_cust == 1:
                clear()
                spec_tran()
                back()
            elif menu_cust == 2:
                clear()
                all_trans()
            elif menu_cust == 8:
                clear()
                break
            elif menu_cust == 9:
                clear()
                menu_adm1 = 9
                return menu_adm1
            elif menu_cust == 0:
                exit()
            else:
                error()
        while tran_act == 2:
            clear()
            while True:
                try:
                    loan_act = int(input(
                        'Select Loan Type: \n1. Educational Loan \n2. Car Loan \n3. Home Loan \n4. Personal Loan \n5. All Loans \n8. Go back \n9. Log Out(Main Menu) \n0. Exit  \n'))
                    break
                except:
                    clear()
                    error()
            if loan_act == 1:
                loan_type_trans('Educational')
                back()
            elif loan_act == 2:
                loan_type_trans('Car')
                back()
            elif loan_act == 3:
                loan_type_trans('Home')
                back()
            elif loan_act == 4:
                loan_type_trans('Personal')
                back()
            elif loan_act == 5:
                all_trans()
            elif loan_act == 8:
                clear()
                break
            elif loan_act == 9:
                clear()
                menu_adm1 = 9
                return menu_adm1
            elif loan_act == 0:
                exit()
        if tran_act == 9:
            menu_adm1 = 9
            return menu_adm1
        elif tran_act == 8:
            return menu_adm1
        elif tran_act == 0:
            exit()

def regisd_logic():     #registered user menu logic.
    while True:
        print('Enter 0 to go back\nNOTE! Password is case sensitive!!\n')
        log_us = login()
        if log_us == '0':
            break
        pas_us = password()
        if pas_us == '0':
            break
        num4 = num_line(int(number_lines()), log_us)
        if num4:
            log_us_chk = get_log(num4)
            pas_us_chk = get_pass(num4)
            if approve_check(num4):
                passing = 1
            elif not approve_check(num4):
                print('Your account is not approved yet by admin, please wait.')
                back()
                break
        else:
            log_us_chk = False
            pas_us_chk = False
            passing = 0
        while log_us == log_us_chk and pas_us == pas_us_chk and passing == 1:
            clear()
            while True:
                try:
                    menu_regus = logRegUs()
                    break
                except:
                    clear()
                    error()
            if menu_regus == 1:
                loan_details(log_us)
            elif menu_regus == 2:
                if remaining(log_us, num4) > 0:
                    while True:
                        try:
                            pay_loans(log_us, num4)
                            break
                        except:
                            error()
                elif remaining(log_us, num4) == 0:
                    print('Your Loan was repaid. No more payments are required.')
            elif menu_regus == 3:
                own_trans(log_us)
            elif menu_regus == 4:
                loan_status(log_us, num4)
            elif menu_regus == 9:
                menu1 = 9
                return menu1
            elif menu_regus == 0:
                exit()
            else:
                error()
        else:
            print('Wrong login or password, try again')

def new_logic():    #and new user menu logic
    while True:
        print('========== Welcome =========='.center(65))
        menu_newc = menu_newC()
        if menu_newc == 1:
            menu1 = newc_menu1()
        elif menu_newc == 2:
            menu1 = newc_menu2()
        elif menu_newc == 3:
            menu1 = newc_menu3()
        if menu_newc == 0:
            exit()
        elif menu_newc == 9:
            menu1 = 9
        elif menu_newc != 1 and menu_newc != 2 and menu_newc != 3:
            error()
        if menu1 == 9:
            return menu1

def newc_menu1():   #logic for opening menu of registration for new user
    while True:
        try:
            registration()
            break
        except:
            clear()
            print('Something went wrong, please try again')

def newc_menu2():   #loan information menu for new user
    while True:
        while True:
            try:
                loan_det = loan_menu()
                break
            except:
                clear()
                error()
        if loan_det == 1:
            info_educ()
        elif loan_det == 2:
            info_car()
        elif loan_det == 3:
            info_home()
        elif loan_det == 4:
            info_pers()
        elif loan_det == 0:
            exit()
        elif loan_det == 9:
            menu1 = 9
            return menu1
        elif loan_det == 8:
            break
        else:
            error()

def newc_menu3():   #loan calculator, can be accessed by new user.
    while True:
        print('Loan Calculator')
        while True:
            try:
                loan_calc = loan_menu()
                break
            except:
                clear()
                error()
        yearRate = 0
        if loan_calc == 1:
            yearRate = 0.045
        elif loan_calc == 2:
            yearRate = 0.07
        elif loan_calc == 3:
            yearRate = 0.06
        elif loan_calc == 4:
            yearRate = 0.075
        elif loan_calc == 0:
            exit()
        elif loan_calc == 8:
            break
        elif loan_calc == 9:
            menu1 = 9
            return menu1
        else:
            error()
        if yearRate > 0:
            calculator(yearRate)

def main_logic():       #and finally main logic of whole program
    while True:
        menu1 = mainmenu()
        if menu1 == 1:
            menu1 = admin_logic()
        elif menu1 == 2:
            menu1 = regisd_logic()
        elif menu1 == 3:
            menu1 = new_logic()
        if menu1 == 0:
            exit()
        elif menu1 == 9:
            pass
        elif menu1 != 1 and menu1 != 2 and menu1 != 3:
            error()

main_logic()
