from prettytable import PrettyTable

def calculator():
    list = PrettyTable()
    r = int(input('How many reps did you do? \n'))


    w = int(input('How much weight did you lift in lbs? \n' ))

    

    print(f"You lifted {w} for {r} reps ")
    # To add a column
    # Syntax:- pretty.add_column(fieldname, column, align='c'/'r'/'l',valign='t'/'m'/'b')
    # Here,valign:- desired vertical alignment for new columns -"t" for top, "m" for middle and "b" for bottom
    # Here, align:- desired alignment for this column - "l" forleft, "c" for centre and "r" for right

    # pretty.add_column('Names',['Rahul','Modi','Arvind','Sonia','John Cena'],align='l',valign='t')
    # pretty.add_column('Item',['Egg','Bread','Spam','Bacon','Butter'],valign='b')
    # pretty.add_column('Rating',['7','3','9','2','10'],valign='m')

    eplay = w * (1 + (r/30))
    lombardi = w * (r**0.10)
    conner= w * (1 +(r/40))

    list.field_names = ["Formula", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

    percentages_eplay = ["eplay",]
    percentages_lombardi = ["lombardi",]
    percentages_conner = ["conner",]


    for i in range(1, 11, 1):
        percentages_eplay.append(round((i*0.1*eplay),2))
    for i in range(1, 11, 1):
        percentages_lombardi.append(round((i*0.1*lombardi),2))
    for i in range(1, 11, 1):
        percentages_conner.append(round((i*0.1*conner),2))

    #percentage(eplay_max)
    #percentage(lombardi_max)
    #percentage(conner_max)

    list.add_row(percentages_eplay)
    list.add_row(percentages_lombardi)
    list.add_row(percentages_conner)
    #list.add_column("eplay", "lombardi", "conner")
    print(list)


calculator()