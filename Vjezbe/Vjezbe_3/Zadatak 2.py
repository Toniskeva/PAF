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
#Pri povećavanju broja iteracija,sve više se povećava broj S, pa je svakom vrtnjom petlje oduzimanja sve manja razlika između broja S
#i novog broja S nakon oduzimanja 1/3, pa se odbacuju decimale koje su neznatne u odnosu na velik cijeli dio broja i time nastaje sve veći konačni ostatak zbog zaokruživanja pomoću baze 2.