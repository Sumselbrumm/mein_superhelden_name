
#Superhelden Name aus 3 Ziffern je 1-5 
characteristics = ["Grimmiger", "Garstiger", "Wuselnder","Mächtiger", "Überdimensionaler", "Oberaffengeiler"]
nouns = ["Sternen", "Melonen", "Fels", "Hut", "Gott", "Galaxie", "Nokia 5110", "Neutronen"]
executions =["Zermatscher", "Zerstörer", "Vernichter", "Verzwirbler", "Zerfetzer", "Atomisierer"]

#Funktionen definieren
def input_number(text, list):
    component = int(input(text))
    if component in range(1,len(list)+1,1):
        pass
    else:
        component = input_number("Deine Zahl muss zwischen 1 und "+ str(len(list)) +" sein. Bitte neu wählen:", list)
    return component

#user input
first_component = input_number("Gib hier deine erste Zahl zwischen 1 und " + str(len(characteristics)) + " ein: ", characteristics)
second_component = input_number("Gib hier deine zweite Zahl zwischen 1 und " + str(len(nouns)) + " ein: ", nouns)
third_component = input_number("Gib hier deine dritte Zahl zwischen 1 und " + str(len(executions)) + " ein: ", executions)
    
print()
print("Dein Superheldenname ist: ", characteristics[first_component-1], nouns[second_component-1], executions[third_component-1])
print()
# ganz schön langweilig dieser Code! Das kann ich jetzt viel besser. :-D
