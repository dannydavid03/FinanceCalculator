x=open('ABOOUT THE PROGRAM.txt','w')
x.write("Welcome to Danny & Andrew's desperate attempt at Internals!!! \n\n"
        'The aim of this program is to create a user friendly interface that enables users to - nah sike, this is just a desperate attempt by the creators of this program to avoid failing \nboards by getting lit internals.\n\n'
        'However, if you are jobless enough to try and use this program, you would be midly surprised at its usefulness. You can create an account and store all your financial details, '
        'such as\nmonthly income and expenses and then use it to find out how much you would be saving at the end of the year!\n'
        '\nIt might sound simple, we admit, it is, but great efforts have been taken (by Andrew mostly, he is like, the BEST) in order to ensure that your password is protected, '
        'and the integrity of\nyour data is not compromised (lmao nah we just put it all in an excel sheet yo, do not expect too much and dont be surprised either, lol).'
        '\n\nBut seriously, we hope you enjoy using this program and we defenitely do not judge you at all for wasting your time on something that can be done using '
        'a pen, paper and a calculator.\n(I mean come on dude, are you genuinely dumb enough to be reading this right now? Seriously??? Get a life buddy.)\n\n')
x.close()

y=open('ABOUT THE PROGRAMMERS.txt','w')
y.write(' The Programmers are Andrew Gonsalves & Daniel Alexander from 12 SC F (THE INDIAN HIGH SCHOOL, RIP (1961-2020))'
        '\n Andrew Gonsalves is a dashing, handsome young man with a brilliant mind, and a charming personality. He serves as the surpeme and benevolent leader for the students of 12 SC F.'
        'He is dearly loved by all those who know him, and to the surprise and genuine concern from his friends, is single. (So ladies, you know what to do ;)'
        '(fake_gonsalves.jr ,on insta fyi))'
        '\n Daniel Alexander........yeah he is nice I guess idk\n')
y.close()

def program():
    x=open('ABOOUT THE PROGRAM.txt','r')
    for i in x:
        print(i, end=' ')
    x.close()

def author():
    y=open('ABOUT THE PROGRAMMERS.txt','r')
    for i in y:
        print(i)
    y.close()
