#Définition de la variable
RNA = "AGCUAUGAGUUGCGCAUGCUCAGUCGAUCGCAUACUGAGC"
codonSearch = "AUG"

#Code génétique
genetic_code = {
        "UUU": "F",
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "UAU": "Y",
        "UAC": "Y",
        "UAA": "",
        "UAG": "",
        "UGU": "C",
        "UGC": "C",
        "UGA": "*",
        "UGG": "W",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGU": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }

#Fonction
def codon(valueRNA, valuecodonSearch):
    
    #Définition du cadre à 0 (premier cadre)
    cadre = 0
    
    #Définition du codon recherché
    codonSearch = valuecodonSearch
    
    #Tant que cadre est strictement inférieur à 3
    while cadre < 3:
        #Définition de la variable en Array
        codons = []
        #Définition de la variable isFind à False 
        isFind = False
        
        #Print du cadre actuel
        print("Cadre", str(cadre + 1), ":")
        #Je défini la variable RNA avec la variable RNA en retirant le nombre de caractères du cadre (cadre 0 je retire 0, cadre 1 je retire un caractère, etc)
        RNA = valueRNA[cadre:]
        #Je défini le cadre en faisant +1 au cadre actuel pour la prochaine étape d'analyse
        cadre = cadre + 1
        
        #Pour chaque élément dans la range
        #La range se trouve entre 0 et la longeur de la variable RNA, chaque élément dois faire 3 de longueur.
        for i in range(0, len(RNA), 3):
            #Codon = Le bout de RNA extrait 
            codon = RNA[i:i+3]
            #Ajout du condon à la liste
            codons.append(codon)
        
        #Si le dernier élément n'est pas strictement égale à 3
        if len(codons[-1]) != 3:
            #Supprimer le dernier élément
            codons.pop()
        
        #Pour chaques éléments dans la liste des condons
        for i in range(len(codons)):
            #Si le condon parfaitement égale à "AUG"
            if codons[i] == codonSearch:
                #Je print l'emplacement du condon dans la liste.
                print(str(i + 1), "ème place")
                
                #Si trouvé je défini la variable à True
                isFind = True
        
        #Si isFind strictement égale à True
        if isFind == True:
            #Pour chaques éléments dans la liste des codons
            for i in range(len(codons)):
                #Si le codon est strictement égale à "AUG"
                if codons[i] == codonSearch:
                    #Définition de l'array Codons sans les codons présent avant "AUG"
                    codons = codons[i:]           
                    #Print de l'array sans les codons présents avant.
                    print(f"Séquence {codonSearch}", str(codons))
                    #Arrêt
                    break
            
            #Création de la variable geneticCode en array
            geneticCode = []
            
            #Pour chaque éléments dans la liste des codons
            for i in range(len(codons)):
                #Si le codon match dans le tableau du code génétique
                if codons[i] in genetic_code:
                    #Ajout du match à la variable geneticCode
                    geneticCode.append(genetic_code[codons[i]])
            
            #Print du code génétique
            print("Code génétique", geneticCode)
        #Sinon
        else:
            print("AUG n'a pas été trouvé dans la liste.")

 
#Démarage de la fonction
codon(RNA, codonSearch)