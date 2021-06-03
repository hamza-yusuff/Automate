import smtplib,ssl

user='hamzalondon27yusuff@gmail.com'
password='isfarnayeem'
port=465


recievers=[['rumananabi', 'rumananabiclass2', 'nabirumana@gmail.com'], ['khadijasaifuddin', 'khadijasaifuddinclass2', 'khadija.ctg@gmail.com'],
 ['qamrunnahar', 'qamrunnaharclass2', 'lovely_nahar90@yahoo.com'], ['farabeecgs', 'farabeecgsclass2', 'farabeecgs@gmail.com'],
 ['fariyahoque', 'fariyahoqueclass2', 'fariyahoque29@gmail.com'], ['savinaserrao', 'savinaserraoclass2', 'savinaserrao@yahoo.com'], ['nargisfatema', 'nargisfatemaclass2', 'nargisf_ctg@yahoo.com'],
 ['selina', 'selinaclass8', 's4elina@gmail.com'], ['rajib', 'rajibclass8', 'infocgsrajibchy@gmail.com'],
 ['fauzia', 'fauziaclass8', 'fauzia.mostafasaby@gmail.com'], ['kamrun', 'kamrunclass8', 'kamrunjulie7@gmail.com'], ['sharminakther', 'sharminaktherclass8', 'sharmin.cgsmiddle@gmail.com'],
 ['partho', 'parthoclass8', 'infocgs.partho@gmail.com'], ['asad', 'asadclass8', 'infocgs.asad@gmail.com'], ['kishoredashgupta', 'kishoredashguptaclass8', 'kishore_dgupta@yahoo.com'],
 ['mousumiaktar', 'mousumiaktarclass8', 'mousumiaktar@hotmail.com'], ['himelchowdhury', 'himelchowdhuryclass8', 'him_cgs@yahoo.com'], ['erinachowdhury', 'erinachowdhuryclass8', 'erina2_19@yahoo.com'],
 ['sukdebmaths', 'sukdebmathsclass8', 'sukdeb06@yahoo.com'], ['ziacgs', 'ziacgsclass8', 'ziamohiuddincgs@gmail.com'], ['faiza', 'faizaclass8', 'faizachy10@gmail.com'],
 ['ruhbayna', 'ruhbaynaclass8', 'ruhbaynamc@gmail.com'], ['masihanazrul', 'masihanazrulcgsd2020', 'nazrulmasiha@gmail.com'], ['samiachowdhury', 'samiachowdhurycgsd2020', 'samiatupur27@gmail.com'],
 ['rikhtianasrin', 'rikhtianasrincgsd2020', 'nasrin365@gmail.com'], ['ummesalma', 'ummesalmacgsd2020', 'salma.cgsd@gmail.com'], ['sojedaakterchowdhury', 'sojedaakterchowdhurycgsd2020', 'sojeda.chowdhury@gmail.com'],
 ['hasanulkarimraffi', 'hasanulkarimrafficgsd2020', 'hasanul101@gmail.com'],
 ['faribatabassum', 'faribatabassumcgsd2020', 'faribatabassum1994@gmail.com'], ['mahiyathsadequebhuiyan', 'mahiyathsadequebhuiyancgsd2020', 'mahiyath_19@hotmail.com']]



def sendmail(username,pass_word,email):
    reciever=email
    starting='Hello Sir/Miss, please use this link https://cgsconnect.web.app/ and the credentials below to login into your account on CONNECT, please change your password after you login.'
    ending="Pleas do not use the link sent in the previous mail"
    name='hamza'
    message = """\
    Subject: User credentials and New Link

    {}
    {}
    username: {}
    password: {}
    email: {}
    """.format(starting,ending,username,pass_word,email)

    context =ssl.create_default_context()

    print('starting')

    with smtplib.SMTP_SSL("smtp.gmail.com", port , context=context) as server:
        server.login(user,password)
        server.sendmail(user,reciever,message)
    print("send email")



for i in range(len(recievers)):
    sendmail(recievers[i][0],recievers[i][1],recievers[i][2])

sendmail("hamza","pass",user)
