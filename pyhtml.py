# vershtml.py version 1.1.1

import keyword
import html

"""py.txt en py.htm
imperatifs :
1/ les strings n'utilisent pas les simples quotes

"""
# constantes css
intro = "<em ><a style=\"margin-left:35px; color:grey;\" href=\"https://site2wouf.fr/python_vers_html.php\">"
intro += "Code Python traduit en HTML: </a></em>"
intro += """<code><pre style=\"margin-top:2px; margin-left:20px; font-size:120%;border-radius: 20px; 
 max-width:600px; max-height:600px; padding-left :15px; overflow-x:auto; 
  border:3px ridge grey; Line-Height: 1.5;\">"""
fin = "</pre></code>"
motsclefs = keyword.kwlist
natives = ["abs", "bytes", "chr", "eval", "exec", "input", "int", "len", "max",
           "min", "open", "print", "str"]
nativestyle = "<span style=\"color:purple\">"
motsclefstyle = "<span style=\"color:orange\">"
diesestyle = "<span style=\"color:red\">"
fichier = open("py.txt", "r")
texte = fichier.read()
fichier.close()
avant = ["/n", " ", "(", "=", "."]
apres = ["/n", " ", ")", ".", "(", ":"]
print("Cette application va transformer le code python du fichier py.txt en html")
print("Et enregistrer le résultat dans py.htm...")
print("Les deux fichiers étant dans le répertoire de l'application !")
nom = input("(Facultatif ) Entrez le nom du programme :")
sources = ""
if nom != "":

    sources = input("(Facultatif ) Entrez un lien hypertext:")

# pretraitement à cause du caractère d echappement en html
texte = texte.replace("\\\"", "|@@|")

""" c est ici qu on modifie texte"""
liste = texte.split("\"\"\"")
"""les elements paires de la liste sont des commentaires de type triples cotes"""
i = 1
texte = ""
for morceau in liste:
    if i % 2 == 1:
        # On cherche les strings
        morceau2 = morceau.split("\"")
        morceau2propre = ""
        j = 1
        for partie in morceau2:
            if j % 2 == 1:
                """On continue le traitement en cherchant les # hors chaine (commentaires)
qu'on remplace temporairement par |&|

"""

                partiepropre = partie.replace("#", "|&|")
                for mot in motsclefs:
                    for av in avant:
                        for ap in apres:
                            partiepropre = partiepropre.replace(av + mot + ap,
                                                                av + motsclefstyle + mot + "</span>" + ap)
                for mot in natives:
                    for av in avant:
                        for ap in apres:
                            partiepropre = partiepropre.replace(av + mot + ap, av + nativestyle + mot + "</span>" + ap)
                morceau2propre += partiepropre
            else:
                morceau2propre = morceau2propre + "<span style=\"color:#04B404\">\"" \
                                 + html.escape(partie, quote=True) + "\" </span>"
            j += 1

        texte += morceau2propre
    else:
        texte = texte + "<span style=\"color:#04B404\">\"\"\"" + html.escape(morceau, quote=True) + "\"\"\" </span>"
    i += 1

""" reste à verifier ligne par ligne les mots clefs et les commentaires"""
lignes = texte.split("\n")
texte = ""
for ligne in lignes:

    demi = ligne.split("|&|", 1)
    lignefinale = str(demi[0])
    for mot in motsclefs:
        for x in apres:
            if demi[0].find(mot + x) == 0:
                lignefinale = motsclefstyle + mot + x + "</span>" + demi[0][len(mot) + len(x):]

    for mot in natives:
        for x in apres:
            if demi[0].find(mot + x) == 0:
                lignefinale = nativestyle + mot + x + "</span>" + demi[0][len(mot) + len(x):]
    texte += lignefinale
    if len(demi) > 1:
        texte = texte + "<span style=\"color:red\">|&|" + demi[1] + "</span>\n"
    else:
        texte = texte + "\n"

texte = intro + texte + fin

# postraitement
texte = texte.replace("|@@|", "\\\"")
texte = texte.replace("|&|", "#")
if nom != "" and sources != "":
    texte = texte + """<p style=\"text-align:right; 
width:600px; margin-top:2px; \"><em><a style=\"color:grey;\" href=\"" + sources + "\">""" + nom + "</a></em></p>"
elif nom != "" and sources == "":
    texte = texte + "<p style=\"text-align:right;width:600px;margin-top:2px; color:grey;\"><em>" + nom + "</em></p>"

fichier = open("py.htm", "w")
fichier.write(texte)
fichier.close()
# vershtml.py version 1.1.1
