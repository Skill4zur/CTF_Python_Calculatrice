#/usr/bin/python3
#Created by SkillAzur

import os

def main():
    try:
        """
        CTF python: Super Calculator v0.2
        Objectif: Lire le contenu de flag.txt
        Il est interdit de modifier le programme comme le précédent
        """
        print("Super Calculator v0.2 ")
        print("Manuel d'utilisation: entrez ci-dessous un calcul comme: '1+1-1+1', '(3*2)**2', '6.0-5.2'...")
        print("Calcul: ")
        x = input()
        if verifier(x):
            print(eval(x))
            return x
        else:
            return "/!\\ Alerte Tentative De Hack /!\\"
        return False

    except EOFError:
        return False
    except KeyboardInterrupt:
        return False
    except:
        return False

def verifier(calcul):
    #Suite à un hack de la v0.1, j'ai décidé de mettre un verifier
    #pour éviter un prochain hack
    if "open" in calcul or "flag.txt" in calcul or "read" in calcul:
        print("/!\\ Alerte Tentative De Hack /!\\")
        return False
    else:
        return True

def setup():
    #Ne modifie surtout pas cette fonction sinon le CTF pourras pas se setup
    #Le code est obfusqué pour tenter d'éviter la triche et les changements

    buff = b""
    buff += b"\x6f\x70\x65\x6e\x28\x22\x66\x6c\x61\x67\x2e\x74\x78\x74\x22\x2c"
    buff += b"\x20\x22\x61\x22\x29\x2e\x77\x72\x69\x74\x65\x28\x22\x46\x4c\x41"
    buff += b"\x47\x7b\x44\x4f\x4e\x27\x54\x5f\x54\x52\x55\x53\x54\x5f\x55\x53"
    buff += b"\x45\x52\x5f\x49\x4e\x50\x55\x54\x7d\x22\x29"

    buff1 = b""
    buff1 += b"\x6f\x73\x2e\x72\x65\x6d\x6f\x76\x65\x28\x22\x66\x6c\x61\x67\x2e"
    buff1 += b"\x74\x78\x74\x22\x29"

    buff2 = b""
    buff2 += b"\x70\x72\x69\x6e\x74\x28\x22\x50\x61\x73\x20\x74\x6f\x75\x63\x68"
    buff2 += b"\x65\x20\x61\x75\x20\x70\x72\x6f\x67\x72\x61\x6d\x6d\x65\x20\x21"
    buff2 += b"\x21\x22\x29"

    buff3 = b""
    buff3 += b"\x6e\x6f\x74\x20\x6f\x73\x2e\x70\x61\x74\x68\x2e\x65\x78\x69\x73"
    buff3 += b"\x74\x73\x28\x22\x66\x6c\x61\x67\x2e\x74\x78\x74\x22\x29"

    buff4 = b""
    buff4 += b"\x6f\x73\x2e\x70\x61\x74\x68\x2e\x65\x78\x69\x73\x74\x73\x28\x22"
    buff4 += b"\x66\x6c\x61\x67\x2e\x74\x78\x74\x22\x29"

    if eval(buff3):
        eval(buff)
    elif eval(buff4):
        eval(buff1)
    else:
        eval(buff2)

if __name__ == '__main__':
    eval(b"\x73\x65\x74\x75\x70\x28\x29")
    main()
    eval(b"\x73\x65\x74\x75\x70\x28\x29")
