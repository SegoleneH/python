# Notation pour sauter des lignes dans la chaîne de caractères
text4 = """ <div>
                <h1></h1>
            <div>
        """

text5 = "<div>\n\t<h1>Titre de 1er niveau</h1>\n<div>\n"
print(text4)
print(text5)
# \n : retour à la ligne \t = tabulation
# alt + Z : retour à la ligne auto

# text6 = "Foo "Bar" Baz" --> erreur de syntaxe
text6 = 'Foo Bar Baz'
text6 = "Foo \"Bar\" Baz" # --> \= caractère d'échappement \\ = \ 



