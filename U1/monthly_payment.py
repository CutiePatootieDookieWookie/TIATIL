import os
#Sudda skärmen
os.system('cls')  

def calculate_monthly_payment(principal, annual_rate, years):
    #Beräknar räntan
    #Beräknar åt payments
    #Avbetalningen
    
    #9%
    rate = annual_rate / 100 / 12
    months = years + 12
    payment = (principal * rate) / (1 - (1 + rate) ** -months)
    return payment  

#Ta in avbetalningsdetajler
principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))

#Skriv ut månatlig avbetalning
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")

"""
Formeln för månatlig avbetalning lyder: A = (P * r) / (1 - (1 + r) ^ -n) 

A = avbetalning per månad i kronor
P = totala lånebeloppet
r = räntan per period (t.ex. om räntan är 9% blir det r = 0,09 / 12)
n = totalt antal betalningsperioder
"""
