import mysql.connector
import sys

COLOURS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def colortext(text):
    for colour in COLOURS:
        text = text.replace("[[" + colour + "]]", COLOURS[colour])
    return text


def main():
    mdb = mysql.connector.connect(host='localhost', user='root', passwd="1234")
    mc = mdb.cursor()

    mc.execute('CREATE DATABASE IF NOT EXISTS corona;')
    mc.execute('use corona;')
    mc.execute("""create table if not exists user( Userid int not null primary key , 
        Password varchar(3000), 
        Name varchar(50) , 
        Gender varchar(10) , 
        Age varchar(50), 
        Profession varchar(40) , 
        Phone varchar(50), 
        Address varchar(5000), 
        TOI varchar(50) , 
        TOS varchar(50),
        Welfare varchar(8),
        Cough varchar(3),
        Fever varchar(3),
        Difficult_in_breathing varchar(3),
        Loss_of_senses_of_smell_and_taste varchar(3),
        Diabetes varchar(3),
        Hypertension varchar(3),
        Lung_disease varchar(3),
        Heart_disease varchar(3),
        Kidney_disorder varchar(3),
        Interaction varchar(3),
        Infection_Status varchar(150));""")

    mc.execute("""create table if not exists admin ( Adminid integer(10) not null primary key,
        Password varchar(3000),
        Name varchar(50),
        Gender varchar(10),
        Age varchar(50),
        Profession varchar(40),
        Phone varchar(50),
        Address varchar(5000),
        TOI varchar(50),
        TOS varchar(50),
        Welfare varchar(8),
        Cough varchar(3),
        Fever varchar(3),
        Difficult_in_breathing varchar(3),
        Loss_of_senses_of_smell_and_taste varchar(3),
        Diabetes varchar(3),
        Hypertension varchar(3),
        Lung_disease varchar(3),
        Heart_disease varchar(3),
        Kidney_disorder varchar(3),
        Interaction varchar(3),
        Infection_Status varchar(150));""")
    mdb.commit()

    s = '1'
    while s == '1':

        z = input('DO YOU WANT TO RUN THIS PROGRAM AGAIN? {ENTER 1 TO DO SO or ENTER ANY KEY TO EXIT }  :')

        if z == '1':

            pgm(mc, mdb)

        else:

            sys.exit("THANK YOU FOR USING THIS SOFTWARE")


def uupdateprofile(userid1, mc, mdb):
    f = 1
    while f == 1:
        b7 = input(
            'What do you want to change or update?\n1.Change name\n2.Change age\n3.Change gender\n4.Change '
            'profession\n5.Change phone number\n6.Change address\n7.Go back\n:')

        if b7 == '1':
            f = 2
            newname = input('Enter new name : ')
            mc.execute('''update user
            set name = %s
            where userid=%s;''', (newname, userid1))
            mdb.commit()
            print('New name updated')

        elif b7 == '2':
            f = 2
            newage = input('Enter new age : ')
            mc.execute('''update user
            set age = %s
            where userid = %s;''', (newage, userid1))
            mdb.commit()
            print('New age updated')

        elif b7 == '3':
            f = 2
            j = 1
            while j == 1:
                newgender = input('Enter new gender : 1.MALE  2.FEMALE  :')
                if newgender == '1':
                    j = 2
                    newgender = 'male'
                elif newgender == '2':
                    j = 2
                    newgender = 'female'
                else:
                    j = 1
                    print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]]'))

            mc.execute('''update user
                        set gender = %s
                        where userid = %s;''', (newgender, userid1))
            mdb.commit()
            print('New gender updated')

        elif b7 == '4':
            f = 2
            h = 1
            while h == 1:
                newprof = input('''What is your new proffession?
                1. Doctor / Nurse / Paramedic
                2. Police / Officers / Law Enforcement
                3. Delivery
                4. Chemist / Pharmacy
                5. Wholesaler / Retailer / Groceries
                6. Industry / Manufactures
                7. Teaching / Non teaching ( education related)
                8. Student
                9. Unemployed
                0. None of the above
                {enter only the number infront of each related profession}''')

                if newprof == '1':
                    h = 2
                    newprof = 'Doctor / Nurse / Paramedic'

                elif newprof == '2':
                    h = 2
                    newprof = 'Police / Officers / Law Enforcement'

                elif newprof == '3':
                    h = 2
                    newprof = 'Delivery'

                elif newprof == '4':
                    h = 2
                    newprof = 'Chemist / Pharmacy'

                elif newprof == '5':
                    h = 2
                    newprof = 'Wholesaler / Retailer / Groceries'

                elif newprof == '6':
                    h = 2
                    newprof = 'Industry / Manufactures'

                elif newprof == '7':
                    h = 2
                    newprof = 'Teaching / Non teaching ( education related)'

                elif newprof == '8':
                    h = 2
                    newprof = 'Student'

                elif newprof == '9':
                    h = 2
                    newprof = 'Unemployed'

                elif newprof == '0':
                    h = 2
                    newprof = 'None of the above'

                else:
                    h = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))

            mc.execute('''update user
            set profession = %s
            where userid = %s;''', (newprof, userid1))
            mdb.commit()
            print('New profession updated')



        elif b7 == '5':
            f = 2
            newph = input('Enter new phone number : ')
            mc.execute('''update user
            set phone = %s
            where userid = %s;''', (newph, userid1))
            mdb.commit()
            print('New phone number updated')

        elif b7 == '6':
            f = 2
            newad = input('Enter new address : ')
            mc.execute('''update user
            set address = %s
            where userid = %s;''', (newad, userid1))
            mdb.commit()
            print('New address updated')

        elif b7 == '7':
            f = 2


        else:
            f = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))


def uhealthcheck(userid1, mc, mdb):
    st = 0
    a1 = 1
    while a1 == 1:
        toi12 = input('Did you travel outside India in the last 30 days? {1.Yes   2.No} :')
        if toi12 == '1':
            a1 = 2
            toi1 = input('Name the country or countries you have visited in the last 30 days :')
        elif toi12 == '2':
            a1 = 2
            toi1 = 'nil'
        else:
            a1 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
    mc.execute('''update user
                set TOI = %s
                where userid = %s;''', (toi1, userid1))
    mdb.commit()

    a2 = 1
    while a2 == 1:
        tos12 = input('Did you travel outside Kerala in the last 30 days? {1.Yes   2.No} :')
        if tos12 == '1':
            a2 = 2
            tos1 = input('Name the state or states you have visited in the last 30 days :')
        elif tos12 == '2':
            a2 = 2
            tos1 = 'nil'
        else:
            a2 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
    mc.execute('''update user
                    set TOS = %s
                    where userid = %s;''', (tos1, userid1))
    mdb.commit()

    a3 = 1
    while a3 == 1:
        wel1 = input('Are you feeling well? {1.Yes   2.No}')
        if wel1 == '1':
            a3 = 2
            wel = 'fine'
        elif wel1 == '2':
            a3 = 2
            st = st + 2
            wel = 'notfine'
        else:
            a3 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
    mc.execute('''update user
                        set Welfare = %s
                        where userid = %s;''', (wel, userid1))
    mdb.commit()

    a4 = 1
    while a4 == 1:
        sym = input(
            'Are you experiencing any of the following symptoms?\nCough,fever,difficulty in breathing,loss of senses '
            'ofsmell and taste {1.Yes   2.No}')
        if sym == '1':
            a4 = 2
            b1 = 1
            print('What all symptoms are you experiencing? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:
                c12 = input('Cough? {1.yes  2. no}')
                if c12 == '1':
                    st = st + 1
                    b1 = 2
                    c1 = 'yes'
                elif c12 == '2':
                    b1 = 2
                    c1 = 'no'
                else:
                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
            set Cough = %s
            where userid = %s;''', (c1, userid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:
                c22 = input('Fever? {1.yes  2. no}')
                if c22 == '1':
                    st = st + 1
                    b2 = 2
                    c2 = 'yes'
                elif c22 == '2':
                    b2 = 2
                    c2 = 'no'
                else:
                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
            set Fever = %s
            where userid = %s;''', (c2, userid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:
                c32 = input('Difficulty in breathing? {1.yes  2. no}')
                if c32 == '1':
                    st = st + 2
                    b3 = 2
                    c3 = 'yes'
                elif c32 == '2':
                    b3 = 2
                    c3 = 'no'
                else:
                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
            set  Difficult_in_breathing= %s
            where userid = %s;''', (c3, userid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c42 = input('Loss of senses of smell and taste? {1.yes  2. no}')
                if c42 == '1':
                    st = st + 2
                    b4 = 2
                    c4 = 'yes'
                elif c42 == '2':
                    b4 = 2
                    c4 = 'no'
                else:
                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
            set  Loss_of_senses_of_smell_and_taste = %s
            where userid = %s;''', (c4, userid1))
            mdb.commit()


        elif sym == '2':
            a4 = 2
            mc.execute('''update user
            set  cough = %s
            where userid = %s;''', ('no', userid1))
            mc.execute('''update user
            set  fever = %s
            where userid = %s;''', ('no', userid1))
            mc.execute('''update user
            set  Difficult_in_breathing = %s
            where userid = %s;''', ('no', userid1))
            mc.execute('''update user
            set  Loss_of_senses_of_smell_and_taste = %s
            where userid = %s;''', ('no', userid1))
            mdb.commit()

        else:

            a4 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))

    a5 = 1
    while a5 == 1:
        sym1 = input(
            'Have you ever had any of the following?\nDiabetes, hypertension, lung disease, heart disease, '
            'kidney disease {1.Yes   2.No}')
        if sym1 == '1':
            a5 = 2
            b1 = 1
            print('Which all you had? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:
                c12 = input('Diabetes? {1.yes  2. no}')
                if c12 == '1':
                    st = st + 2
                    b1 = 2
                    c1 = 'yes'
                elif c12 == '2':
                    b1 = 2
                    c1 = 'no'
                else:
                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
                set Diabetes = %s
                where userid = %s;''', (c1, userid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:
                c22 = input('Hypertension? {1.yes  2. no}')
                if c22 == '1':
                    st = st + 2
                    b2 = 2
                    c2 = 'yes'
                elif c22 == '2':
                    b2 = 2
                    c2 = 'no'
                else:
                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
                set Hypertension = %s
                where userid = %s;''', (c2, userid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:
                c32 = input('Lung disease? {1.yes  2. no}')
                if c32 == '1':
                    st = st + 2
                    b3 = 2
                    c3 = 'yes'
                elif c32 == '2':
                    b3 = 2
                    c3 = 'no'
                else:
                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
                set  Lung_disease = %s
                where userid = %s;''', (c3, userid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c42 = input('Heart disease? {1.yes  2. no}')
                if c42 == '1':
                    st = st + 2
                    b4 = 2
                    c4 = 'yes'
                elif c42 == '2':
                    b4 = 2
                    c4 = 'no'
                else:
                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
                set  Heart_disease = %s
                where userid = %s;''', (c4, userid1))
            mdb.commit()

            b5 = 1
            while b5 == 1:
                c52 = input('Kidney disease? {1.yes  2. no}')
                if c52 == '1':
                    st = st + 2
                    b5 = 2
                    c5 = 'yes'
                elif c52 == '2':
                    b5 = 2
                    c5 = 'no'
                else:
                    b5 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
            mc.execute('''update user
                            set  Kidney_disorder = %s
                            where userid = %s;''', (c5, userid1))
            mdb.commit()


        elif sym1 == '2':
            a5 = 2
            mc.execute('''update user
            set  Diabetes = %s
            where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set  Hypertension = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set  Lung_disease = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set  Heart_disease = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set  Kidney_disorder = %s
                where userid = %s;''', ('no', userid1))
            mdb.commit()

        else:

            a5 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))

    a6 = 1
    while a6 == 1:
        intera2 = input(
            'Have you recently interacted or lived with someone who has tested positive for COVID-19? {1.Yes   2.No} :')
        if intera2 == '1':
            st = st + 10
            a6 = 2
            intera = 'yes'
        elif intera2 == '2':
            a6 = 2
            intera = 'no'
        else:
            a6 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.[[yellow]]'))
    mc.execute('''update user
                set Interaction = %s
                where userid = %s;''', (intera, userid1))
    mdb.commit()

    if st == 0:
        istatus = 'very low risk'
        print('YOUR COVID-19 AFFECTION RISK IS VERY LOW  :). \n STAY HOME STAY SAFE')
    elif 0 < st < 4:
        istatus = 'low risk'
        print('YOUR COVID-19 AFFECTION RISK IS LOW  :). \n STAY HOME STAY SAFE')
    elif 3 < st < 8:
        istatus = 'intermediate risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS INTERMEDIATE  :|. YOU NEED TO BE MORE CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS.\n STAY HOME STAY SAFE')
    elif 7 < st < 16:
        istatus = 'high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS HIGH  :(. YOU NEED TO BE VERY CAREFUL. FOLLOW GOVERNMENT INSTRUCTIONS '
            'AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')
    else:
        istatus = 'very high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS VERY HIGH  :(. YOU NEED TO BE EXTREMELY CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    mc.execute('''update user
    set Infection_Status = %s
    where userid = %s;''', (istatus, userid1))
    mdb.commit()


def udelacc(userid1, mc):
    a7 = 1
    while a7 == 1:
        conf = eval(input('Are you sure that you want to delete your account? {1.yes  2.no}:'))

        if conf == 1:

            a7 = 2
            mc.execute("delete from user where userid = %s" % (userid1))
            print('ACCOUNT DELETED')

        elif conf == 2:

            a7 = 2
            print('ACCOUNT DELETION CANCELED')

        else:

            a7 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))


def upswdchange(userid1, mc, mdb):
    z4 = 1
    mc.execute('''select phone from user where userid = %s''' % (userid1))
    z1 = mc.fetchone()

    while z4 == 1:

        z = input('Enter your phone number that you have registered in your account :')

        if z == z1[0]:
            z4 = 2
            z3 = input('Create your password..\n Enter password :')
            mc.execute('''update user
            set password = %s
            where userid= %s''', (z3, userid1))
            mdb.commit()

        else:
            z4 = 1
            print(colortext('[[red]]INCORRECT PHONE NUMBER!!! PLEASE TRY AGAIN.'))


def aupdateprofile(adminid1, mc, mdb):
    f = 1
    while f == 1:
        b = input(
            'What do you want to change or update?\n1.Change name\n2.Change age\n3.Change gender\n4.Change '
            'profession\n5.Change phone number\n6.Change address\n7.Go back\n:')

        if b == '1':
            f = 2
            newname = input('Enter new name : ')
            mc.execute('''update admin
                set name = %s
                where adminid = %s ;''', (newname, adminid1))
            mdb.commit()
            print('New name updated')

        elif b == '2':
            f = 2
            newage = eval(input('Enter new age : '))
            mc.execute('''update admin
                set age = %s
                where adminid = %s;''', (newage, adminid1))
            mdb.commit()
            print('New age updated')

        elif b == '3':
            f = 2
            j = 1
            while j == 1:
                newgender = eval(input('Enter new gender : 1.MALE  2.FEMALE  :'))
                if newgender == 1:
                    j = 2
                    newgender = 'male'
                elif newgender == 2:
                    j = 2
                    newgender = 'female'
                else:
                    j = 1
                    print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN'))

            mc.execute('''update admin
                            set gender = %s 
                            where adminid = %s ;''', (newgender, adminid1))
            mdb.commit()
            print('New gender updated')



        elif b == '4':
            f = 2
            h = 1
            while h == 1:
                newprof = input('''What is your new profession?
                    1. Doctor / Nurse / Paramedic
                    2. Police / Officers / Law Enforcement
                    3. Delivery
                    4. Chemist / Pharmacy
                    5. Wholesaler / Retailer / Groceries
                    6. Industry / Manufactures
                    7. Teaching / Non teaching ( education related)
                    8. Student
                    9. Unemployed
                    0. None of the above
                    {enter only the number infront of each related profession}''')

                if newprof == '1':
                    h = 2
                    newprof = 'Doctor / Nurse / Paramedic'

                elif newprof == '2':
                    h = 2
                    newprof = 'Police / Officers / Law Enforcement'

                elif newprof == '3':
                    h = 2
                    newprof = 'Delivery'

                elif newprof == '4':
                    h = 2
                    newprof = 'Chemist / Pharmacy'

                elif newprof == '5':
                    h = 2
                    newprof = 'Wholesaler / Retailer / Groceries'

                elif newprof == '6':
                    h = 2
                    newprof = 'Industry / Manufactures'

                elif newprof == '7':
                    h = 2
                    newprof = 'Teaching / Non teaching ( education related)'

                elif newprof == '8':
                    h = 2
                    newprof = 'Student'

                elif newprof == '9':
                    h = 2
                    newprof = 'Unemployed'

                elif newprof == '0':
                    h = 2
                    newprof = 'None of the above'

                else:
                    h = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                set profession = %s
                where adminid = %s;''', (newprof, adminid1))
            mdb.commit()
            print('New profession updated')



        elif b == '5':
            f = 2
            newph = input('Enter new phone number : ')
            mc.execute('''update admin
                set phone = %s
                where adminid = %s ;''', (newph, adminid1))
            mdb.commit()
            print('New phone number updated')

        elif b == '6':
            f = 2
            newad = input('Enter new address : ')
            mc.execute('''update admin
                set address = %s
                where adminid = %s;''', (newad, adminid1))
            mdb.commit()
            print('New address updated')

        elif b == '7':
            f = 2

        else:
            f = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))


def ahealthcheck1(adminid1, mc, mdb):
    st = 0
    a1 = 1
    while a1 == 1:
        toi1 = input('Did you travel outside India in the last 30 days? {1.Yes   2.No} :')
        if toi1 == '1':
            a1 = 2
            toi12 = input('Name the country or countries you have visited in the last 30 days :')
        elif toi1 == '2':
            a1 = 2
            toi12 = 'nil'
        else:
            a1 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
    mc.execute('''update admin
                    set TOI = %s
                    where adminid = %s;''', (toi12, adminid1))
    mdb.commit()

    a2 = 1
    while a2 == 1:
        tos1 = input('Did you travel outside Kerala in the last 30 days? {1.Yes   2.No} :')
        if tos1 == '1':
            a2 = 2
            tos13 = input('Name the state or states you have visited in the last 30 days :')
        elif tos1 == '2':
            a2 = 2
            tos13 = 'nil'
        else:
            a2 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
    mc.execute('''update admin
                        set TOS = %s
                        where adminid = %s;''', (tos13, adminid1))
    mdb.commit()

    a3 = 1
    while a3 == 1:
        wel = input('Are you feeling well? {1.Yes   2.No}')
        if wel == '1':
            a3 = 2
            wel1 = 'fine'
        elif wel == '2':
            a3 = 2
            st = st + 2
            wel1 = 'notfine'
        else:
            a3 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
    mc.execute('''update admin
                            set Welfare = %s
                            where adminid = %s;''', (wel1, adminid1))
    mdb.commit()

    a4 = 1
    while a4 == 1:
        sym = input(
            'Are you experiencing any of the following symptoms?\nCough,fever,difficulty in breathing,loss of senses '
            'of smell and taste {1.Yes   2.No}')
        if sym == '1':
            a4 = 2
            b1 = 1
            print('What all symptoms are you experiencing? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:
                c1 = input('Cough? {1.yes  2. no}')
                if c1 == '1':
                    st = st + 1
                    b1 = 2
                    c12 = 'yes'
                elif c1 == '2':
                    b1 = 2
                    c12 = 'no'
                else:
                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                set Cough = %s
                where adminid = %s ;''', (c12, adminid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:
                c2 = input('Fever? {1.yes  2. no}')
                if c2 == '1':
                    st = st + 1
                    b2 = 2
                    c22 = 'yes'
                elif c2 == '2':
                    b2 = 2
                    c22 = 'no'
                else:
                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                set Fever = %s
                where adminid = %s;''', (c22, adminid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:
                c3 = input('Difficulty in breathing? {1.yes  2. no}')
                if c3 == '1':
                    st = st + 2
                    b3 = 2
                    c32 = 'yes'
                elif c3 == '2':
                    b3 = 2
                    c32 = 'no'
                else:
                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                set  Difficult_in_breathing= %s
                where adminid = %s;''', (c32, adminid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c4 = input('Loss of senses of smell and taste? {1.yes  2. no}')
                if c4 == '1':
                    st = st + 2
                    b4 = 2
                    c42 = 'yes'
                elif c4 == '2':
                    b4 = 2
                    c42 = 'no'
                else:
                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                set  Loss_of_senses_of_smell_and_taste = %s
                where adminid = %s;''', (c42, adminid1))
            mdb.commit()


        elif sym == '2':
            a4 = 2
            mc.execute('''update admin
                set  cough = %s
                where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                set  fever = %s
                where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                set  Difficult_in_breathing = %s
                where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                set  Loss_of_senses_of_smell_and_taste = %s
                where adminid = %s;''', ('no', adminid1))
            mdb.commit()

        else:

            a4 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a5 = 1
    while a5 == 1:
        sym1 = input(
            'Have you ever had any of the following?\nDiabetes, hypertension, lung disease, heart disease, '
            'kidney disease {1.Yes   2.No}:')
        if sym1 == '1':
            a5 = 2
            b1 = 1
            print('Which all you had? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:
                c1 = input('Diabetes? {1.yes  2. no}')
                if c1 == '1':
                    st = st + 2
                    b1 = 2
                    c12 = 'yes'
                elif c1 == '2':
                    b1 = 2
                    c12 = 'no'
                else:
                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                    set Diabetes = %s
                    where adminid = %s;''', (c12, adminid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:
                c2 = input('Hypertension? {1.yes  2. no}')
                if c2 == '1':
                    st = st + 2
                    b2 = 2
                    c22 = 'yes'
                elif c2 == '2':
                    b2 = 2
                    c22 = 'no'
                else:
                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                    set Hypertension = %s
                    where adminid = %s;''', (c22, adminid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:
                c3 = input('Lung disease? {1.yes  2. no}')
                if c3 == '1':
                    st = st + 2
                    b1 = 2
                    c32 = 'yes'
                elif c3 == '2':
                    b3 = 2
                    c32 = 'no'
                else:
                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                    set  Lung_disease = %s
                    where adminid = %s;''', (c32, adminid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c4 = input('Heart disease? {1.yes  2. no}')
                if c4 == '1':
                    st = st + 2
                    b4 = 2
                    c42 = 'yes'
                elif c4 == '2':
                    b4 = 2
                    c42 = 'no'
                else:
                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                    set  Heart_disease = %s
                    where adminid = %s;''', (c42, adminid1))
            mdb.commit()

            b5 = 1
            while b5 == 1:
                c5 = input('Kidney disease? {1.yes  2. no}')
                if c5 == '1':
                    st = st + 2
                    b5 = 2
                    c52 = 'yes'
                elif c5 == '2':
                    b5 = 2
                    c52 = 'no'
                else:
                    b5 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update admin
                                set  Kidney_disorder = %s
                                where adminid = %s;''', (c52, adminid1))
            mdb.commit()


        elif sym1 == '2':
            a5 = 2
            mc.execute('''update admin
                set  Diabetes = %s
                where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                    set  Hypertension = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                    set  Lung_disease = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                    set  Heart_disease = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                    set  Kidney_disorder = %s
                    where adminid = %s;''', ('no', adminid1))
            mdb.commit()

        else:

            a5 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a6 = 1
    while a6 == 1:
        intera = input(
            'Have you recently interacted or lived with someone who has tested positive for COVID-19? {1.Yes   2.No} :')
        if intera == '1':
            st = st + 10
            a6 = 2
            intera1 = 'yes'
        elif intera == '2':
            a6 = 2
            intera1 = 'no'
        else:
            a6 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
    mc.execute('''update admin
                    set Interaction = %s
                    where adminid = %s;''', (intera1, adminid1))
    mdb.commit()

    if st == 0:
        istatus1 = 'very low risk'
        print('YOUR COVID-19 AFFECTION RISK IS VERY LOW  :). \n STAY HOME STAY SAFE')
    elif 0 < st < 4:
        istatus1 = 'low risk'
        print('YOUR COVID-19 AFFECTION RISK IS LOW  :). \n STAY HOME STAY SAFE')
    elif 3 < st < 8:
        istatus1 = 'intermediate risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS INTERMEDIATE  :|. YOU NEED TO BE MORE CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS.\n STAY HOME STAY SAFE')
    elif 7 < st < 16:
        istatus1 = 'high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS HIGH  :(. YOU NEED TO BE VERY CAREFUL. FOLLOW GOVERNMENT INSTRUCTIONS '
            'AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')
    else:
        istatus1 = 'very high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS VERY HIGH  :(. YOU NEED TO BE EXTREMELY CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    mc.execute('''update admin
        set Infection_Status = %s
        where adminid = %s;''', (istatus1, adminid1))
    mdb.commit()


def adelacc1(adminid1, mc, mdb):
    a7 = 1
    while a7 == 1:
        conf = eval(input('Are you sure that you want to delete your account? {1.yes  2.no}:'))

        if conf == 1:

            a7 = 2
            mc.execute("delete from admin where adminid = %s" % (adminid1))
            mdb.commit()
            print('ACCOUNT DELETED')

        elif conf == 2:

            a7 = 2
            print('ACCOUNT DELETION CANCELED')

        else:

            a7 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))


def apswdchange1(adminid1, mc, mdb):
    z4 = 1
    mc.execute('''select phone from admin where adminid = %s''' % adminid1)
    z1 = mc.fetchone()

    while z4 == 1:

        z = input('Enter your phone number that you have registered in your account :')

        if z == z1[0]:

            z4 = 2
            z3 = input('Create your password..\n Enter password :')
            mc.execute('''update admin
                set password = %s
                where adminid= %s''', (z3, adminid1))
            mdb.commit()

        else:
            z4 = 1
            print(colortext('[[red]]INCORRECT PHONE NUMBER!!! PLEASE TRY AGAIN.'))


def yuhealthcheck(userid1, mc, mdb):
    st = 0
    a1 = 1
    while a1 == 1:

        toi1 = input('Did you travel outside India in the last 30 days? {1.Yes   2.No} :')

        if toi1 == '1':

            a1 = 2
            toi12 = 'yes'
            w1 = 'update user set TOI ="' + toi12 + '" where userid = ' + str(userid1) + ';'
            mc.execute(w1)
            mdb.commit()

        elif toi1 == '2':

            a1 = 2
            toi12 = 'nil'
            mc.execute('''update user set TOI = %s where userid = %s;''', (toi12, userid1))
            mdb.commit()
        else:
            a1 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a2 = 1
    while a2 == 1:
        tos1 = input('Did you travel outside Kerala in the last 30 days? {1.Yes   2.No} :')

        if tos1 == '1':

            a2 = 2
            tos12 = 'yes'
            mc.execute('''update user
                                    set TOS = %s
                                    where userid = %s;''', (tos12, userid1))
            mdb.commit()

        elif tos1 == '2':

            a2 = 2
            tos12 = 'no'
            mc.execute('''update user
                                    set TOS = %s
                                    where userid = %s;''', (tos12, userid1))
            mdb.commit()

        else:
            a2 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a3 = 1
    while a3 == 1:

        wel = input('Are you feeling well? {1.Yes   2.No}')

        if wel == '1':

            a3 = 2
            wel1 = 'fine'
            mc.execute('''update user set Welfare = %s
                                        where userid = %s;''', (wel1, userid1))
            mdb.commit()

        elif wel == '2':

            a3 = 2
            st = st + 2
            wel1 = 'notfine'
            mc.execute('''update user 
            set Welfare = %s
            where userid = %s;''', (wel1, userid1))
            mdb.commit()

        else:

            a3 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a4 = 1
    while a4 == 1:
        sym = input(
            'Are you experiencing any of the following symptoms?\nCough,fever,difficulty in breathing,loss of senses '
            'ofsmell and taste {1.Yes   2.No}')

        if sym == '1':

            a4 = 2
            b1 = 1
            print('What all symptoms are you experiencing? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:

                c1 = input('Cough? {1.yes  2. no}')

                if c1 == '1':

                    st = st + 1
                    b1 = 2
                    c12 = 'yes'

                elif c1 == '2':

                    b1 = 2
                    c12 = 'no'

                else:

                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user set Cough = %s where userid = %s;''', (c12, userid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:

                c2 = input('Fever? {1.yes  2. no}')

                if c2 == '1':
                    st = st + 1
                    b2 = 2
                    c22 = 'yes'
                elif c2 == '2':
                    b2 = 2
                    c22 = 'no'
                else:
                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user set Fever = %s
                where userid = %s;''', (c22, userid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:

                c3 = input('Difficulty in breathing? {1.yes  2. no}')

                if c3 == '1':

                    st = st + 2
                    b3 = 2
                    c32 = 'yes'

                elif c3 == '2':

                    b3 = 2
                    c32 = 'no'

                else:

                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            mc.execute('''update user set  Difficult_in_breathing  = %s where userid = %s;''', (c32, userid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:

                c4 = input('Loss of senses of smell and taste? {1.yes  2. no}')

                if c4 == '1':

                    st = st + 2
                    b4 = 2
                    c42 = 'yes'

                elif c4 == '2':

                    b4 = 2
                    c42 = 'no'

                else:

                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                 set Loss_of_senses_of_smell_and_taste = %s
                where userid = %s;''', (c42, userid1))
            mdb.commit()


        elif sym == '2':

            a4 = 2
            mc.execute('''update user
                 set cough  = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set fever = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                  set Difficult_in_breathing = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                set Loss_of_senses_of_smell_and_taste = %s
                where userid = %s;''', ('no', userid1))
            mdb.commit()

        else:

            a4 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a5 = 1
    while a5 == 1:

        sym1 = input(
            'Have you ever had any of the following?\nDiabetes, hypertension, lung disease, heart disease, '
            'kidney disease {1.Yes   2.No}')
        if sym1 == '1':
            a5 = 2
            b1 = 1
            print('Which all you had? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:

                c1 = input('Diabetes? {1.yes  2. no}')

                if c1 == '1':

                    st = st + 2
                    b1 = 2
                    c13 = 'yes'

                elif c1 == '2':

                    b1 = 2
                    c13 = 'no'

                else:

                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                    set  Diabetes = %s
                    where userid = %s;''', (c13, userid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:
                c2 = input('Hypertension? {1.yes  2. no}')
                if c2 == '1':

                    st = st + 2
                    b2 = 2
                    c23 = 'yes'

                elif c2 == '2':

                    b2 = 2
                    c23 = 'no'

                else:

                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                    set Hypertension = %s
                    where userid = %s;''', (c23, userid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:
                c3 = input('Lung disease? {1.yes  2. no}')
                if c3 == '1':

                    st = st + 2
                    b3 = 2
                    c33 = 'yes'

                elif c3 == '2':

                    b3 = 2
                    c33 = 'no'

                else:

                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                    set  Lung_disease = %s
                    where userid = %s;''', (c33, userid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c4 = input('Heart disease? {1.yes  2. no}')

                if c4 == '1':

                    st = st + 2
                    b4 = 2
                    c43 = 'yes'

                elif c4 == '2':

                    b4 = 2
                    c43 = 'no'

                else:

                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                    set Heart_disease = %s
                    where userid = %s;''', (c43, userid1))
            mdb.commit()

            b5 = 1
            while b5 == 1:
                c5 = input('Kidney disease? {1.yes  2. no}')

                if c5 == '1':

                    st = st + 2
                    b5 = 2
                    c53 = 'yes'

                elif c5 == '2':

                    b5 = 2
                    c53 = 'no'

                else:

                    b5 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update user
                                set  Kidney_disorder = %s
                                where userid = %s;''', (c53, userid1))
            mdb.commit()


        elif sym1 == '2':

            a5 = 2
            mc.execute('''update user
              set Diabetes = %s
                where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                      set Hypertension = %s
                    where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                    set Lung_disease = %s
                    where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                      set Heart_disease = %s
                    where userid = %s;''', ('no', userid1))
            mc.execute('''update user
                    set Kidney_disorder = %s
                    where userid = %s;''', ('no', userid1))
            mdb.commit()

        else:

            a5 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a6 = 1
    while a6 == 1:
        intera = input(
            'Have you recently interacted or lived with someone who has tested positive for COVID-19? {1.Yes   2.No} :')

        if intera == '1':

            st = st + 10
            a6 = 2
            intera3 = 'yes'
            mc.execute('''update user
                                set Interaction = %s
                                where userid = %s;''', (intera3, userid1))
            mdb.commit()

        elif intera == '2':

            a6 = 2
            intera3 = 'no'
            mc.execute('''update user
                                set Interaction = %s
                                where userid = %s;''', (intera3, userid1))
            mdb.commit()

        else:

            a6 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    if st == 0:

        istatus = 'very low risk'
        print('YOUR COVID-19 AFFECTION RISK IS VERY LOW  :). \n STAY HOME STAY SAFE')

    elif st > 0 and st < 4:

        istatus = 'low risk'
        print('YOUR COVID-19 AFFECTION RISK IS LOW  :). \n STAY HOME STAY SAFE')

    elif st > 3 and st < 8:

        istatus = 'intermediate risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS INTERMEDIATE  :|. YOU NEED TO BE MORE CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS.\n STAY HOME STAY SAFE')

    elif st > 7 and st < 16:

        istatus = 'high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS HIGH  :(. YOU NEED TO BE VERY CAREFUL. FOLLOW GOVERNMENT INSTRUCTIONS '
            'AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    else:

        istatus = 'very high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS VERY HIGH  :(. YOU NEED TO BE EXTREMELY CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    mc.execute('''update user
        set Infection_Status = %s
        where userid = %s;''', (istatus, userid1))
    mdb.commit()


def crtperm():
    permission = input('''CREATOR AUTHORISATION REQUIRED TO PERFORM THIS FUNCTION\n\nPLEASE ENTER CREATOR PASSWORD: ''')
    a = 'arjun'
    if permission == a:
        permission = '1'
    else:
        permission = '2'

    return permission


def yahealthcheck(adminid1, mc, mdb):
    st = 0
    a1 = 1

    while a1 == 1:

        toi1 = input('Did you travel outside India in the last 30 days? {1.Yes   2.No} :')

        if toi1 == '1':

            a1 = 2
            toi12 = 'yes'
            mc.execute("update admin set TOI = %s where adminid = %s;", (toi12, adminid1))
            mdb.commit()

        elif toi1 == '2':

            a1 = 2
            toi12 = 'no'
            mc.execute("update admin set TOI = %s where adminid = %s;", (toi12, adminid1))
            mdb.commit()

        else:

            a1 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a2 = 1

    while a2 == 1:

        tos1 = input('Did you travel outside Kerala in the last 30 days? {1.Yes   2.No} :')

        if tos1 == '1':

            a2 = 2
            tos12 = 'yes'
            mc.execute(''' update admin set TOS = %s where adminid = %s;''', (tos12, adminid1))
            mdb.commit()

        elif tos1 == '2':

            a2 = 2
            tos12 = 'no'
            mc.execute(''' update admin set TOS = %s where adminid = %s;''', (tos12, adminid1))
            mdb.commit()

        else:

            a1 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a3 = 1
    while a3 == 1:

        wel = input('Are you feeling well? {1.Yes   2.No}')

        if wel == '1':

            a3 = 2
            wel1 = 'fine'

        elif wel == '2':

            a3 = 2
            st = st + 2
            wel1 = 'notfine'

        else:

            a3 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    mc.execute('''update admin
                              set  Welfare = %s
                                where adminid = %s;''', (wel1, adminid1))
    mdb.commit()

    a4 = 1
    while a4 == 1:

        sym = input('Are you experiencing any of the following symptoms?\nCough,fever,difficulty in breathing,'
                    'loss of senses of smell and taste {1.Yes   2.No}')

        if sym == '1':

            a4 = 2
            b1 = 1
            print('What all symptoms are you experiencing? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:

                c1 = input('Cough? {1.yes  2. no}')

                if c1 == '1':

                    st = st + 1
                    b1 = 2
                    c12 = 'yes'

                elif c1 == '2':

                    b1 = 2
                    c12 = 'no'

                else:

                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                   set Cough = %s
                    where adminid = %s;''', (c12, adminid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:

                c2 = input('Fever? {1.yes  2. no}')

                if c2 == '1':

                    st = st + 1
                    b2 = 2
                    c22 = 'yes'

                elif c2 == '2':

                    b2 = 2
                    c22 = 'no'

                else:

                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                   set Fever = %s
                    where adminid = %s;''', (c22, adminid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:

                c3 = input('Difficulty in breathing? {1.yes  2. no}')

                if c3 == '1':

                    st = st + 2
                    b3 = 2
                    c32 = 'yes'

                elif c3 == '2':

                    b3 = 2
                    c32 = 'no'

                else:

                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                   set Difficult_in_breathing = %s
                    where adminid = %s;''', (c32, adminid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:
                c4 = input('Loss of senses of smell and taste? {1.yes  2. no}')

                if c4 == '1':

                    st = st + 2
                    b4 = 2
                    c42 = 'yes'

                elif c4 == '2':

                    b4 = 2
                    c42 = 'no'

                else:

                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                   set Loss_of_senses_of_smell_and_taste = %s
                    where adminid = %s;''', (c42, adminid1))
            mdb.commit()


        elif sym == '2':

            a4 = 2
            mc.execute('''update admin
                   set cough = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                   set fever = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                   set Difficult_in_breathing = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                   set Loss_of_senses_of_smell_and_taste = %s
                    where adminid = %s;''', ('no', adminid1))
            mdb.commit()

        else:

            a4 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a5 = 1
    while a5 == 1:

        sym1 = input(
            'Have you ever had any of the following?\nDiabetes, hypertension, lung disease, heart disease, '
            'kidney disease {1.Yes   2.No}')

        if sym1 == '1':

            a5 = 2
            b1 = 1
            print('Which all you had? Type 1 for yes and 2 for no for each of the following.')

            while b1 == 1:

                c1 = input('Diabetes? {1.yes  2. no}')

                if c1 == '1':

                    st = st + 2
                    b1 = 2
                    c12 = 'yes'

                elif c1 == '2':

                    b1 = 2
                    c12 = 'no'

                else:

                    b1 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                      set  Diabetes = %s
                        where adminid = %s;''', (c12, adminid1))
            mdb.commit()

            b2 = 1
            while b2 == 1:

                c2 = input('Hypertension? {1.yes  2. no}')

                if c2 == '1':

                    st = st + 2
                    b2 = 2
                    c22 = 'yes'

                elif c2 == '2':

                    b2 = 2
                    c22 = 'no'

                else:

                    b2 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                      set  Hypertension = %s
                        where adminid = %s;''', (c22, adminid1))
            mdb.commit()

            b3 = 1
            while b3 == 1:

                c3 = input('Lung disease? {1.yes  2. no}')

                if c3 == '1':

                    st = st + 2
                    b3 = 2
                    c32 = 'yes'

                elif c3 == '2':

                    b3 = 2
                    c32 = 'no'

                else:

                    b3 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                      set  Lung_disease = %s
                        where adminid = %s;''', (c32, adminid1))
            mdb.commit()

            b4 = 1
            while b4 == 1:

                c4 = input('Heart disease? {1.yes  2. no}')

                if c4 == '1':

                    st = st + 2
                    b4 = 2
                    c42 = 'yes'

                elif c4 == '2':

                    b4 = 2
                    c42 = 'no'

                else:

                    b4 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                       set Heart_disease = %s
                        where adminid = %s;''', (c42, adminid1))
            mdb.commit()

            b5 = 1
            while b5 == 1:

                c5 = input('Kidney disease? {1.yes  2. no}')

                if c5 == '1':

                    st = st + 2
                    b5 = 2
                    c52 = 'yes'

                elif c5 == '2':

                    b5 = 2
                    c52 = 'no'

                else:

                    b5 = 1
                    print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

            mc.execute('''update admin
                                   set Kidney_disorder = %s
                                    where adminid = %s;''', (c52, adminid1))
            mdb.commit()


        elif sym1 == '2':

            a5 = 2
            mc.execute('''update admin
                   set Diabetes = %s
                    where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                       set Hypertension = %s
                        where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                       set Lung_disease = %s
                        where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                    set Heart_disease = %s
                        where adminid = %s;''', ('no', adminid1))
            mc.execute('''update admin
                       set Kidney_disorder = %s
                        where adminid = %s;''', ('no', adminid1))
            mdb.commit()

        else:

            a5 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    a6 = 1
    while a6 == 1:

        intera = input('Have you recently interacted or lived with someone who has tested positive for COVID-19? {'
                       '1.Yes   2.No} :')

        if intera == '1':

            st = st + 10
            a6 = 2
            intera2 = 'yes'
            mc.execute('''update admin
                                    set Interaction = %s
                                    where adminid = %s;''', (intera2, adminid1))
            mdb.commit()

        elif intera == '2':

            a6 = 2
            intera2 = 'no'
            mc.execute('''update admin
            set Interaction = %s
             where adminid = %s;''', (intera2, adminid1))
            mdb.commit()

        else:

            a6 = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

    if st == 0:

        istatus = 'very low risk'
        print('YOUR COVID-19 AFFECTION RISK IS VERY LOW  :). \n STAY HOME STAY SAFE')

    elif st > 0 and st < 4:

        istatus = 'low risk'
        print('YOUR COVID-19 AFFECTION RISK IS LOW  :). \n STAY HOME STAY SAFE')

    elif st > 3 and st < 8:

        istatus = 'intermediate risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS INTERMEDIATE  :|. YOU NEED TO BE MORE CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS.\n STAY HOME STAY SAFE')

    elif st > 7 and st < 16:

        istatus = 'high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS HIGH  :(. YOU NEED TO BE VERY CAREFUL. FOLLOW GOVERNMENT INSTRUCTIONS '
            'AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    else:

        istatus = 'very high risk'
        print(
            'YOUR COVID-19 AFFECTION RISK IS VERY HIGH  :(. YOU NEED TO BE EXTREMELY CAREFUL. FOLLOW GOVERNMENT '
            'INSTRUCTIONS AND CONTACT GOV.HELPLINE FOR INSTRUCTIONS.\n STAY HOME STAY SAFE')

    mc.execute('''update admin
           set Infection_Status = "%s"
            where adminid = %s;''', (istatus, adminid1))
    mdb.commit()


def datasearch(mc, mdb):

    m = 1

    while m == 1:

        wb = "What do you want to search in user database?\n\n1.Show full user database\n2.Search for a specific " \
             "user using Userid\n3.Filter and display user database\n4.Go Back "

        req = input(wb)

        if req == '1':

            m = 2
            mc.execute('select * from user;')
            da = mc.fetchall()
            print('================================================================================================')

            for i in da:
                print('\n\n----------General Details----------\n')
                print('Userid: ', i[0])
                print('Password: ', i[1])
                print('Name: ', i[2])
                print('Gender: ', i[3])
                print('Age: ', i[4])
                print('Profession: ', i[5])
                print('Phone: ', i[6])
                print('Address: ', i[7])
                print('\n\n----------Health Details----------\n')
                print('Travel Outside India: ', i[8])
                print('Travel Outsude Kerala: ', i[9])
                print('Welfare: ', i[10])
                print('Cough: ', i[11])
                print('Fever: ', i[12])
                print('Difficult_in_breathing: ', i[13])
                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                print('Diabetes: ', i[15])
                print('Hypertension: ', i[16])
                print('Lung_disease: ', i[17])
                print('Heart_disease: ', i[18])
                print('Kidney_disorder: ', i[19])
                print('\n\n----------Covid Related Details----------\n')
                print('Interaction: ', i[20])
                print('Infection_Status: ', i[21], '\n\n\n')
                print(
                    '================================================================================================')

        elif req == '2':

            m = 2
            n = 1

            n = 2
            q = input('Enter Userid to search : ')
            mc.execute('select * from user where userid = %s' % q)
            w = mc.fetchall()
            e = mc.rowcount

            if e == 0:

                print(colortext('[[red]]The Userid you have entered does not exist :[[yellow]]'))

            else :

                print('================================================================================================')
                print('\n\n----------General Details----------\n')
                print('Userid: ', w[0][0])
                print('Password: ', w[0][1])
                print('Name: ', w[0][2])
                print('Gender: ', w[0][3])
                print('Age: ', w[0][4])
                print('Profession: ', w[0][5])
                print('Phone: ', w[0][6])
                print('Address: ', w[0][7])
                print('\n\n----------Health Details----------\n')
                print('Travel Outside India: ', w[0][8])
                print('Travel Outsude Kerala: ', w[0][9])
                print('Welfare: ', w[0][10])
                print('Cough: ', w[0][11])
                print('Fever: ', w[0][12])
                print('Difficult_in_breathing: ', w[0][13])
                print('Loss_of_senses_of_smell_and_taste: ', w[0][14])
                print('Diabetes: ', w[0][15])
                print('Hypertension: ', w[0][16])
                print('Lung_disease: ', w[0][17])
                print('Heart_disease: ', w[0][18])
                print('Kidney_disorder: ', w[0][19])
                print('\n\n----------Covid Related Details----------\n')
                print('Interaction: ', w[0][20])
                print('Infection_Status: ', w[0][21], '\n\n\n')
                print('================================================================================================')

        elif req == '3':

            b = 1

            while b == 1:

                ert = input('How do you want to filter?\nFilter by :\n1.Profession\n2.Travel outside India\n3.Travel outside Kerala\n4.Interaction with COVID-19 positive person\n5.Infection Status\n6.Go Back')

                if ert == '1':

                    r = 1
                    b = 2

                    while r == 1:

                        y = '''By which profession do you want to filter?
                        1. Doctor / Nurse / Paramedic
                        2. Police / Officers / Law Enforcement
                        3. Delivery
                        4. Chemist / Pharmacy
                        5. Wholesaler / Retailer / Groceries
                        6. Industry / Manufactures
                        7. Teaching / Non teaching ( education related)
                        8. Student
                        9. Unemployed
                        0. None of the above'''

                        x = input(y)

                        if x == '1':

                            r = 2
                            mc.execute('select * from user where profession = "Doctor / Nurse / Paramedic"')
                            t = mc.fetchall()
                            print('================================================================================================')

                            for i in t:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print('================================================================================================')

                        elif x == '2':

                            r = 2
                            mc.execute('select * from user where profession = "Police / Officers / Law Enforcement"')
                            t = mc.fetchall()
                            print('================================================================================================')

                            for i in t:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print('================================================================================================')

                        elif x == '3':

                            r = 2
                            mc.execute('select * from user where profession = "Delivery"')
                            t = mc.fetchall()
                            print('================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print('================================================================================================')

                        elif x == '4':

                            r = 2
                            mc.execute('select * from user where profession = "Chemist / Pharmacy"')
                            t = mc.fetchall()
                            print('================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '5':

                            r = 2
                            mc.execute('select * from user where profession = "Wholesaler / Retailer / Groceries"')
                            t = mc.fetchall()
                            print('================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '6':

                            r = 2
                            mc.execute('select * from user where profession = "Industry / Manufactures"')
                            t = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '7':

                            r = 2
                            mc.execute('select * from user where profession = "Teaching / Non teaching ( education related)"')
                            t = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '8':

                            r = 2
                            mc.execute('select * from user where profession = "Student"')
                            t = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '9':

                            r = 2
                            mc.execute('select * from user where profession = "Unemployed"')
                            t = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif x == '0':

                            r = 2
                            mc.execute('select * from user where profession = "None of the above"')
                            t = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t:

                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        else:

                            r = 1
                            print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]].'))

                elif ert == '2':

                    b = 2
                    mc.execute('select * from user where TOI = "yes";')
                    ty = mc.fetchall()
                    print('================================================================================================')

                    for i in ty:

                        print('\n\n----------General Details----------\n')
                        print('Userid: ', i[0])
                        print('Password: ', i[1])
                        print('Name: ', i[2])
                        print('Gender: ', i[3])
                        print('Age: ', i[4])
                        print('Profession: ', i[5])
                        print('Phone: ', i[6])
                        print('Address: ', i[7])
                        print('\n\n----------Health Details----------\n')
                        print('Travel Outside India: ', i[8])
                        print('Travel Outsude Kerala: ', i[9])
                        print('Welfare: ', i[10])
                        print('Cough: ', i[11])
                        print('Fever: ', i[12])
                        print('Difficult_in_breathing: ', i[13])
                        print('Loss_of_senses_of_smell_and_taste: ', i[14])
                        print('Diabetes: ', i[15])
                        print('Hypertension: ', i[16])
                        print('Lung_disease: ', i[17])
                        print('Heart_disease: ', i[18])
                        print('Kidney_disorder: ', i[19])
                        print('\n\n----------Covid Related Details----------\n')
                        print('Interaction: ', i[20])
                        print('Infection_Status: ', i[21], '\n\n\n')
                        print('================================================================================================')

                elif ert == '3':

                    b = 2
                    mc.execute('select * from user where TOS = "yes";')
                    ty1 = mc.fetchall()
                    print('================================================================================================')

                    for i in ty1:

                        print('\n\n----------General Details----------\n')
                        print('Userid: ', i[0])
                        print('Password: ', i[1])
                        print('Name: ', i[2])
                        print('Gender: ', i[3])
                        print('Age: ', i[4])
                        print('Profession: ', i[5])
                        print('Phone: ', i[6])
                        print('Address: ', i[7])
                        print('\n\n----------Health Details----------\n')
                        print('Travel Outside India: ', i[8])
                        print('Travel Outsude Kerala: ', i[9])
                        print('Welfare: ', i[10])
                        print('Cough: ', i[11])
                        print('Fever: ', i[12])
                        print('Difficult_in_breathing: ', i[13])
                        print('Loss_of_senses_of_smell_and_taste: ', i[14])
                        print('Diabetes: ', i[15])
                        print('Hypertension: ', i[16])
                        print('Lung_disease: ', i[17])
                        print('Heart_disease: ', i[18])
                        print('Kidney_disorder: ', i[19])
                        print('\n\n----------Covid Related Details----------\n')
                        print('Interaction: ', i[20])
                        print('Infection_Status: ', i[21], '\n\n\n')
                        print('================================================================================================')

                elif ert == '4':

                    b = 2
                    mc.execute('select * from user where Interaction = "yes";')
                    ty2 = mc.fetchall()
                    print(
                        '================================================================================================')

                    for i in ty2:

                        print('\n\n----------General Details----------\n')
                        print('Userid: ', i[0])
                        print('Password: ', i[1])
                        print('Name: ', i[2])
                        print('Gender: ', i[3])
                        print('Age: ', i[4])
                        print('Profession: ', i[5])
                        print('Phone: ', i[6])
                        print('Address: ', i[7])
                        print('\n\n----------Health Details----------\n')
                        print('Travel Outside India: ', i[8])
                        print('Travel Outsude Kerala: ', i[9])
                        print('Welfare: ', i[10])
                        print('Cough: ', i[11])
                        print('Fever: ', i[12])
                        print('Difficult_in_breathing: ', i[13])
                        print('Loss_of_senses_of_smell_and_taste: ', i[14])
                        print('Diabetes: ', i[15])
                        print('Hypertension: ', i[16])
                        print('Lung_disease: ', i[17])
                        print('Heart_disease: ', i[18])
                        print('Kidney_disorder: ', i[19])
                        print('\n\n----------Covid Related Details----------\n')
                        print('Interaction: ', i[20])
                        print('Infection_Status: ', i[21], '\n\n\n')
                        print(
                            '================================================================================================')

                elif ert == '5':

                    g = 1
                    b = 2

                    while g == 1:

                        o = '''Which of the following risk status you want to know?
                        1.very high risk
                        2.high risk
                        3.intermediate risk
                        4.low risk
                        5.very low risk
                        6.Go Back'''
                        io = input(o)

                        if io == '1':

                            g = 2
                            mc.execute('select * from user where Infection_Status = "very high risk"')
                            t6 = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t6:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif io == '2':

                            g = 2
                            mc.execute('select * from user where Infection_Status = "high risk"')
                            t7 = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t7:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif io == '3':

                            g = 2
                            mc.execute('select * from user where Infection_Status = "intermediate risk"')
                            t8 = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t8:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif io == '4':

                            g = 2
                            mc.execute('select * from user where Infection_Status = "low risk"')
                            t9 = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t9:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif io == '5':

                            g = 2
                            mc.execute('select * from user where Infection_Status = "very low risk"')
                            t11 = mc.fetchall()
                            print(
                                '================================================================================================')

                            for i in t11:
                                print('\n\n----------General Details----------\n')
                                print('Userid: ', i[0])
                                print('Password: ', i[1])
                                print('Name: ', i[2])
                                print('Gender: ', i[3])
                                print('Age: ', i[4])
                                print('Profession: ', i[5])
                                print('Phone: ', i[6])
                                print('Address: ', i[7])
                                print('\n\n----------Health Details----------\n')
                                print('Travel Outside India: ', i[8])
                                print('Travel Outsude Kerala: ', i[9])
                                print('Welfare: ', i[10])
                                print('Cough: ', i[11])
                                print('Fever: ', i[12])
                                print('Difficult_in_breathing: ', i[13])
                                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                                print('Diabetes: ', i[15])
                                print('Hypertension: ', i[16])
                                print('Lung_disease: ', i[17])
                                print('Heart_disease: ', i[18])
                                print('Kidney_disorder: ', i[19])
                                print('\n\n----------Covid Related Details----------\n')
                                print('Interaction: ', i[20])
                                print('Infection_Status: ', i[21], '\n\n\n')
                                print(
                                    '================================================================================================')

                        elif io == '6':

                            g = 2
                            break

                elif ert == '6':

                    b = 2
                    break



                else:

                    r = 1
                    print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]].'))

        elif req == '4':

            break


def useraccdel(mc, mdb):

    l = 1

    while l == 1:

        hj = input('Enter the Userid of the account that you want to delete : ')
        mc.execute('select * from user where userid = %s' % hj)
        fg = mc.fetchall()
        kl = mc.rowcount

        if kl == 0:

            print(colortext('[[red]]THE USERID YOU HAVE ENTERED DOES NOT EXIST. PLEASE TRY AGAIN!!![[YELLOW]]'))

        else:

            l = 2
            print(
                '================================================================================================')

            for i in fg:

                print('\n\n----------General Details----------\n')
                print('Userid: ', i[0])
                print('Password: ', i[1])
                print('Name: ', i[2])
                print('Gender: ', i[3])
                print('Age: ', i[4])
                print('Profession: ', i[5])
                print('Phone: ', i[6])
                print('Address: ', i[7])
                print('\n\n----------Health Details----------\n')
                print('Travel Outside India: ', i[8])
                print('Travel Outsude Kerala: ', i[9])
                print('Welfare: ', i[10])
                print('Cough: ', i[11])
                print('Fever: ', i[12])
                print('Difficult_in_breathing: ', i[13])
                print('Loss_of_senses_of_smell_and_taste: ', i[14])
                print('Diabetes: ', i[15])
                print('Hypertension: ', i[16])
                print('Lung_disease: ', i[17])
                print('Heart_disease: ', i[18])
                print('Kidney_disorder: ', i[19])
                print('\n\n----------Covid Related Details----------\n')
                print('Interaction: ', i[20])
                print('Infection_Status: ', i[21], '\n\n\n')
                print(
                    '================================================================================================')

            u = 1
            while u == 1:

                gd = input('Are you sure you want delete this account? \n{1.Yes   2.No, go back}  :')

                if gd == '1':

                    u = 2
                    mc.execute("delete from user where userid = %s" % (hj))
                    mdb.commit()
                    print('ACCOUNT DELETED')

                elif gd == '2':


                    print(colortext('[[blue]]ACCOUNT DELETION CANCELED[[yellow]]'))
                    break
                    break

                else:

                    print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]].'))




def pgm(mc, mdb):
    hello = ''''\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[[green]]COVID-19 AFFECTION RISK CHECK\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 
     [[blue]]SOFTWARE BY ARJUN SANDHU \n\n\n\n[[magenta]]Check your risk of COVID-19 affection just by completing a few steps through this software.
      \n [[red]]{#NOTE: *UNKNOWN INPUTS OTHER THAN THOSE GIVEN INSIDE BRACKETS NEAR EACH ENQUIRY WILL BE CONSIDERED AS NONE OPTION. 
      \n *FOR ANSWERING TO EACH QUESTIONS PLEASE ANSWER IN THE PROPER FORMAT AS GIVEN NEAR THE QUESTION. 
      \n *THE NUMBER GIVEN NEXT TO THE OPTIONS SHOULD BE ENTERED AS YOUR ANSWER
      except in the case of name, userid, password, age, country name,state names, adress etc as per the question requirement.
       For Example: How are you? { 1. Fine  2. Not fine }: 
       \n-here if your answer is fine then just type 1 and if answer is not fine type 2. 
    \n\n\n[[white]]Are you new to this software? { 1.YES    2.NO }  : [[yellow]] '''

    n = 1
    while n == 1:

        neworold = input(colortext(hello))

        if neworold == '2':

            n = 2

            r5 = 1
            while r5 == 1:

                useroradmin = input('WELCOME BACK!!  :)\n ARE YOU SIGNED UP AS 1.USER OR 2.ADMIN   : ')

                if useroradmin == '1':

                    r5 = 2
                    e = 1
                    j = 1

                    while j == 1:

                        userid1 = input('PLEASE ENTER YOUR USER ID : ')
                        mc.execute("SELECT userid from user where userid = %s;" % userid1)
                        abc = mc.fetchall()

                        q = mc.rowcount

                        if q == 1:

                            e = 2

                            while q == 1:

                                q = 1

                                upswd = input('PLEASE ENTER YOUR PASSWORD : ')
                                mc.execute('select Password from user where userid = %s ;' % (userid1))
                                upswdcheck = mc.fetchone()

                                e = 2

                                if upswd == upswdcheck[0]:

                                    q = 2
                                    print(colortext('[[green]]YOU HAVE BEEN SIGNED IN SUCCESSFULLY :) [[yellow]]. '))
                                    mc.execute('select name from user where userid = %s ;' % (userid1))
                                    uname = mc.fetchone()
                                    unamelist = list(uname)
                                    print('HI ', unamelist[0])

                                    w = 1
                                    while w == 1:

                                        userreq = input('''\nWhat do you want to do?\n
                                        1.Update your profile details
                                        2.Check your COVID-19 affection risk status
                                        3.Delete your account
                                        4.Signout''')

                                        if userreq == '1':

                                            uupdateprofile(userid1, mc, mdb)

                                        elif userreq == '2':

                                            uhealthcheck(userid1, mc, mdb)

                                        elif userreq == '3':

                                            udelacc(userid1, mc)
                                            j = 2
                                            break

                                        elif userreq == '4':

                                            j = 2
                                            break

                                        else:
                                            w = 1
                                            print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]].'))


                                else:

                                    print(colortext(
                                        '[[red]]THE PASSWORD YOU HAVE ENTERED IS WRONG !!!  PLEASE TRY AGAIN[['
                                        'yellow]].'))
                                    pc = input('Enter 1 if u have forgot your password. \nTo try again press any')

                                    if pc == '1':

                                        q = 2
                                        upswdchange(userid1, mc, mdb)

                                    else:

                                        q = 1


                        else:

                            print(colortext(
                                '[[red]]THE USERID YOU HAVE ENTERED DOES NOT EXIST. PLEASE TRY AGAIN!![[yellow]].'))
                            e = 1


                elif useroradmin == '2':

                    r5 = 2
                    e = 1
                    j = 1

                    while j == 1:

                        adminid1 = input('PLEASE ENTER YOUR ADMIN ID : ')
                        mc.execute("SELECT adminid from admin where adminid = %s;" % adminid1)
                        abc = mc.fetchall()
                        q = mc.rowcount

                        if q == 1:

                            e = 2

                            while q == 1:

                                q = 1
                                upswd = input('PLEASE ENTER YOUR PASSWORD : ')
                                mc.execute('select Password from admin where adminid = %s ;' % adminid1)
                                upswdcheck = mc.fetchone()
                                e = 2

                                if upswd == upswdcheck[0]:

                                    q = 2
                                    print(colortext('[[green]]YOU HAVE BEEN SIGNED IN SUCCESSFULLY :) [[yellow]]. '))
                                    mc.execute('select name from admin where adminid = %s ;' % adminid1)
                                    uname = mc.fetchone()
                                    unamelist = list(uname)
                                    print('HI ', unamelist[0])
                                    w = 1

                                    while w == 1:

                                        userreq = input('''\nWhat do you want to do?\n
                                        1.Update your profile details
                                        2.Check your COVID-19 affection risk status
                                        3.Delete your account
                                        4.Change your password
                                        5.Search in Userdata
                                        6.Delete a User account
                                        7.Sign out\n:
                                        ''')

                                        if userreq == '1':

                                            aupdateprofile(adminid1, mc, mdb)

                                        elif userreq == '2':

                                            ahealthcheck1(adminid1, mc, mdb)

                                        elif userreq == '3':

                                            adelacc1(adminid1, mc, mdb)
                                            j = 2
                                            break

                                        elif userreq == '4':

                                            apswdchange1(adminid1, mc, mdb)

                                        elif userreq == '5':

                                            datasearch(mc, mdb)

                                        elif userreq == '6':

                                            useraccdel(mc,mdb)

                                        elif userreq == '7':

                                            j = 2
                                            break


                                        else:

                                            w = 1
                                            print(colortext('[[red]]INVALID INPUT !!! . PLEASE TRY AGAIN[[yellow]].'))



                                else:

                                    print(colortext(
                                        '[[red]]THE PASSWORD YOU HAVE ENTERED IS WRONG !!!  PLEASE TRY AGAIN[['
                                        'yellow]].'))
                                    pc = input('Enter 1 if u have forgot your password. \nTo try again press any')

                                    if pc == '1':

                                        q = 2
                                        apswdchange1(adminid1, mc, mdb)

                                    else:

                                        q = 1

                        else:

                            print(colortext(

                                '[[red]]THE USERID YOU HAVE ENTERED DOES NOT EXIST. PLEASE TRY AGAIN!![[yellow]].'))

                            e = 1

        elif neworold == '1':

            n = 2

            r1 = 1
            while r1 == 1:

                r1 = 2
                useroradmin1 = input(
                    'HI WELCOME ! \n HOW DO YOU WANT TO SIGNUP TO THIS SOFTWARE ? \n1.USER     2.ADMIN   : ')

                if useroradmin1 == '1':

                    r1 = 2
                    yuname = input('What is your full name?  :')
                    print('Hi ', yuname,
                          '.\n COVID-19 infection risk checkup also will be done along with the account sign '
                          'in.\nPlease provide true information in the respective format.\n\n')
                    yuage = input('What is your age?  :')

                    g = 1
                    while g == 1:

                        yugender = input('What is your gender? {enter 1.MALE      2.FEMALE} : ')

                        if yugender == '1':

                            yugender5 = 'male'
                            g = 2

                        elif yugender == '2':

                            yugender5 = 'female'
                            g = 2

                        else:
                            print(colortext('[[red]]INVALID INPUT !!! PLEASE TRY AGAIN.'))
                            g = 1

                    h = 1
                    while h == 1:

                        yuprof = input('''What is your profession?
                        1. Doctor / Nurse / Paramedic
                        2. Police / Officers / Law Enforcement
                        3. Delivery
                        4. Chemist / Pharmacy
                        5. Wholesaler / Retailer / Groceries
                        6. Industry / Manufactures
                        7. Teaching / Non teaching ( education related)
                        8. Student
                        9. Unemployed
                        0. None of the above
                        {enter only the number infront of each related profession} :''')

                        if yuprof == '1':
                            h = 2
                            yuprof5 = 'Doctor / Nurse / Paramedic'

                        elif yuprof == '2':
                            h = 2
                            yuprof5 = 'Police / Officers / Law Enforcement'

                        elif yuprof == '3':
                            h = 2
                            yuprof5 = 'Delivery'

                        elif yuprof == '4':
                            h = 2
                            yuprof5 = 'Chemist / Pharmacy'

                        elif yuprof == '5':
                            h = 2
                            yuprof5 = 'Wholesaler / Retailer / Groceries'

                        elif yuprof == '6':
                            h = 2
                            yuprof5 = 'Industry / Manufactures'

                        elif yuprof == '7':
                            h = 2
                            yuprof5 = 'Teaching / Non teaching ( education related)'

                        elif yuprof == '8':
                            h = 2
                            yuprof5 = 'Student'

                        elif yuprof == '9':
                            h = 2
                            yuprof5 = 'Unemployed'

                        elif yuprof == '0':
                            h = 2
                            yuprof5 = 'None of the above'

                        else:
                            h = 1
                            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN[[white]].'))

                    yuphno = input('Enter your phone number:')
                    yuadd = input('Enter your address:')
                    yupswd = input('Create your password..\n Enter password :')

                    mc.execute('select count(userid) from user;')
                    no = mc.fetchone()
                    sa = list(no)
                    yuserid = 543210 + sa[0]
                    print('This is your generated userid:', yuserid,
                          '\n Please remember your userid and password innorder to sign in to your account next time')
                    adminid1 = yuserid

                    mc.execute(
                        '''insert into user  
                        values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s )''',
                        (yuserid, yupswd, yuname, yugender5, yuage, yuprof5, yuphno, yuadd, 'idk', 'idk', 'idk', 'idk',
                         'idk', 'idk', 'idk', 'idk', 'idk', 'idk', 'idk', 'idk', 'idk', 'idk'))

                    mdb.commit()
                    yuhealthcheck(adminid1, mc, mdb)

                elif useroradmin1 == '2':

                    r1 = 2
                    creatorpermission = crtperm()

                    if creatorpermission == '1':

                        yaname = input('What is your full name?  :')
                        print('Hi ', yaname,
                              '.\n COVID-19 infection risk checkup also will be done along with the account sign '
                              'in.\nPlease provide true information in the respective format.\n\n')
                        yaage = input('What is your age?  :')

                        g1 = 1
                        while g1 == 1:

                            yagender = input('What is your gender? {enter 1.MALE      2.FEMALE} :')

                            if yagender == '1':

                                yagender = 'male'
                                g1 = 2

                            elif yagender == '2':

                                yagender = 'female'
                                g1 = 2

                            else:
                                print(colortext('[[red]]INVALID INPUT !!! PLEASE TRY AGAIN.'))
                                g1 = 1

                        h1 = 1
                        while h1 == 1:

                            yaprof = input('''What is your proffession?
                                                1. Doctor / Nurse / Paramedic
                                                2. Police / Officers / Law Enforcement
                                                3. Delivery
                                                4. Chemist / Pharmacy
                                                5. Wholesaler / Retailer / Groceries
                                                6. Industry / Manufactures
                                                7. Teaching / Non teaching ( education related)
                                                8. Student
                                                9. Unemployed
                                                0. None of the above
                                                {enter only the number infront of each related profession}
                                                ''')

                            if yaprof == '1':

                                h1 = 2
                                yaprof = 'Doctor / Nurse / Paramedic'

                            elif yaprof == '2':

                                h1 = 2
                                yaprof = 'Police / Officers / Law Enforcement'

                            elif yaprof == '3':

                                h1 = 2
                                yaprof = 'Delivery'

                            elif yaprof == '4':

                                h1 = 2
                                yaprof = 'Chemist / Pharmacy'

                            elif yaprof == '5':

                                h1 = 2
                                yaprof = 'Wholesaler / Retailer / Groceries'

                            elif yaprof == '6':

                                h1 = 2
                                yaprof = 'Industry / Manufactures'

                            elif yaprof == '7':

                                h1 = 2
                                yaprof = 'Teaching / Non teaching ( education related)'

                            elif yaprof == '8':

                                h1 = 2
                                yaprof = 'Student'

                            elif yaprof == '9':

                                h1 = 2
                                yaprof = 'Unemployed'

                            elif yaprof == '0':

                                h1 = 2
                                yaprof = 'None of the above'

                            else:
                                h1 = 1
                                print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))

                        yaphno = input('Enter your phone number:')
                        yaadd = input('Enter your address:')
                        yapswd = input('Create your password..\n Enter password :')

                        mc.execute('select count(Adminid) from admin;')
                        no1 = mc.fetchone()
                        sa1 = list(no1)
                        yadminid = 43210 + sa1[0]
                        adminid1 = yadminid
                        print('This is your generated adminid:', adminid1,
                              '\n Please remember your adminid and password innorder to sign in to your account next '
                              'time')
                        a123 = 'insert into admin (Adminid , Password, Name, Gender ,  Age, Profession , Phone, ' \
                               'Address) values( %s, %s, %s, %s, %s, %s, %s, %s )'
                        b123 = (adminid1, yapswd, yaname, yagender, yaage, yaprof, yaphno, yaadd)
                        mc.execute(a123, b123)
                        mdb.commit()
                        yahealthcheck(adminid1, mc, mdb)

                    else:
                        print(colortext(
                            '[[red]]YOU ARE NOT AUTHORIZED TO CREATE ADMIN ACCOUNT WITHOUT CREATOR PERMISSION. \n '
                            'CONTACT CREATOR FOR PERMISSION AND THEN TRY AGAIN'))
                        r1 = 1

        else:
            n = 1
            print(colortext('[[red]]INVALID INPUT!!! PLEASE TRY AGAIN.'))
            continue


main()
