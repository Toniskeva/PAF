def funkcija(N):
    S=5
    for i in range(N):
        S+=1/3
    for i in range(N):
        S=S-1/3
    print(S)
funkcija(200)
funkcija(2000)
funkcija(20000)
#Pri povećavanju broja iteracija,povećavanjem broja S sve je manja razlika između brojeva pri zbrajanju i oduzimanju jer drugi se drugi broj zaokružuje sve više kako je 5 značajnije od male decimale te je sve manji