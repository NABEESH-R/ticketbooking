print("LOCATIONS")
print("1)CHENNAI-->KARUR")
print("2)BANGALORE-->MADURAI")
print("3)COVAI-->SALEM")
print("4)SALEM-->ERODE")
print("5)NAMAKKAL-->CHENNAI")
print("6)VELLORE-->THENI")
LOCATON=int(input("ENTER YOUR LOCATION:"))

if(LOCATON==1):
    print("BUS TIMINGS")
    print("1)6.00 AM  - 10.00 AM")
    print("2)12.00 AM - 9.00 AM")
    print("3)11.00 PM - 8.00 AM")
    print("4)7.00 AM  - 1.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("6.00 AM  - 10.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        
        
                    
    elif(TIME==2):
        print("12.00 AM - 9.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("11.00 PM - 8.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("7.00 AM  - 1.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        
elif(LOCATON==2):
    print("BUS TIMINGS")
    print("1)7.00 AM - 12.00 AM")
    print("2)8.00 PM - 3.00 AM")
    print("3)3.00 PM - 1.00 AM")
    print("4)5.00 AM - 10.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("7.00 AM - 12.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==2):
        print("8.00 PM - 3.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("3.00 PM - 1.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("5.00 AM - 10.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        
elif(LOCATON==3):
    print("BUS TIMINGS")
    print("1)8.00 AM   - 12.00 PM")
    print("2)10.00 PM  - 3.00 AM")
    print("3)6.00 PM   - 2.00 AM")
    print("4)9.00 AM   - 11.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("8.00 AM   - 12.00 PM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==2):
        print("10.00 PM  - 3.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("6.00 PM   - 2.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("9.00 AM   - 11.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
elif(LOCATON==4):
    print("BUS TIMINGS")
    print("7.00 AM - 12.00 AM")
    print("8.00 PM - 3.00 AM")
    print("3.00 PM - 1.00 AM")
    print("5.00 AM - 10.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("7.00 AM - 12.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==2):
        print("8.00 PM - 3.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("3.00 PM - 1.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("5.00 AM - 10.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
   
elif(LOCATON==5):
    print("BUS TIMINGS")
    print("1)6.00 AM  - 10.00 AM")
    print("2)12.00 AM - 9.00 AM")
    print("3)11.00 PM - 8.00 AM")
    print("4)7.00 AM  - 1.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("6.00 AM  - 10.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==2):
        print("12.00 AM - 9.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("11.00 PM - 8.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("7.00 AM  - 1.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
   
elif(LOCATON==6):
    print("BUS TIMINGS")
    print("1)8.00 AM  - 12.00 PM")
    print("2)10.00 PM - 3.00 AM")
    print("3)6.00 PM  - 2.00 AM")
    print("4)9.00 AM  - 11.00 AM")
    TIME=int(input("ENTER TIME:"))
    if(TIME==1):
        print("8.00 AM   - 12.00 PM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==2):
        print("10.00 PM  - 3.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==3):
        print("6.00 PM   - 2.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
    elif(TIME==4):
        print("9.00 AM   - 11.00 AM")
        print("1.AC + SLEEPER")
        print("2.AC + SEMI SLEEPER")
        print("3.NON AC + SLEEPER")
        print("4.NON AC + SEMI SLEEPER")
        TYPE=int(input("ENTER YOUR TYPE:"))
        if(TYPE==1):
            print("BUS DETAILS")
            print("BUS NAME-SELVA TRAVELS")
            print("BUS NUMBER-TN47932HN")
            print("CONTACT - 8899921333")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.5U")
                    print("2.4U")
                    print("3.3L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 5U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 4U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 3L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                    
        elif(TYPE==2):
            print("BUS DETAILS")
            print("BUS NAME-MURUGAN TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 7382328222")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.12U")
                    print("2.6U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 12U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==3):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.10U")
                    print("2.9U")
                    print("3.8L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 10U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 8L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
        elif(TYPE==4):
            print("BUS DETAILS")
            print("BUS NAME-GANESH TRAVELS")
            print("BUS NUMBER-TN47832HW")
            print("CONTACT - 9965987774")
            A=int(input("ENTER 1 FOR CONTINUE:"))
            if(A==1):
                print("SEAT SELECTION")
                print("1.WINDOW SEAT")
                print("2.CORNER SEAT")
                B=int(input("SELECT THE SEAT:"))
                if(B==1):
                    print("AVAILABE SEATS")
                    print("1.11U")
                    print("2.9U")
                    print("3.7L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 11U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 9U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 7L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
                elif(B==2):
                    print("AVAILABE SEATS")
                    print("1.2U")
                    print("2.6U")
                    print("3.9L")
                    C=int(input("ENTER YOUR SEAT NO:"))
                    if(C==1):
                        print("SEAT NO 2U IS SELECTED")
                    elif(C==2):
                        print("SEAT NO 6U IS SELECTED")
                    elif(C==3):
                        print("SEAT NO 9L IS SELECTED")
                    print("FILL PERSONAL DETAILS")
                    NAME=input("ENTER YOUR NAME:")
                    DOB=input("ENTER YOUR DATE OF BIRTH(DD-MM-YYYY):")
                    EMAIL=input("ENTER YOUR EMAIL:")
                    PHONENUM=int(input("ENTER YOUR PHONE NUMBER(10-DIGITS):"))
                    print(NAME)
                    print(DOB)
                    print(PHONENUM)
                    CONFORM=int(input("PRESS 1 FOR CONFORMATION:"))
                    if(CONFORM==1):
                        print("YOUR BOOKING IS COMPLETED!")
                    else:
                        print("YOUR BOOKING IS CANCELLED")
   
else:
    print("INVALID INPUT")



