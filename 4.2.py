def palindrome_check(input):
    for i in range(len(input)):
        if input[i]==input[-i-1] and i<len(input)//2: # porównujemy pierwsza z ostatnią itd. zatrzymujemy się na środku słowa - każdą parę musze porównać tylko raz, mogę użyż dzielenia bez reszty ponieważ jeśli słowo ma nieparzystą liczbę liter to środkowa litera zawsze zostanie taka sama
            continue
        elif i==len(input)//2: # jeśli wszystkie pary liter się zgadzają to wejdziemy tutaj to spełnimy warunek i zwrócimy True
            return True
        else:
            return False # jeśli napotkamy parę liter która się nie zgadza to nie spełnimy wymagań pierwszego ani drugiego warunku i zwrócimy False
