import hashlib
from colorama import init, Fore
import sys
import os
import time

init()
def title():
        print(Fore.GREEN + """
           :::    :::           :::        ::::::::       :::    :::       ::::::::       :::::::::           :::        ::::::::       :::    :::
          :+:    :+:         :+: :+:     :+:    :+:      :+:    :+:      :+:    :+:      :+:    :+:        :+: :+:     :+:    :+:      :+:   :+:
         +:+    +:+        +:+   +:+    +:+             +:+    +:+      +:+             +:+    +:+       +:+   +:+    +:+             +:+  +:+
        +#++:++#++       +#++:++#++:   +#++:++#++      +#++:++#++      +#+             +#++:++#:       +#++:++#++:   +#+             +#++:++
       +#+    +#+       +#+     +#+          +#+      +#+    +#+      +#+             +#+    +#+      +#+     +#+   +#+             +#+  +#+
      #+#    #+#       #+#     #+#   #+#    #+#      #+#    #+#      #+#    #+#      #+#    #+#      #+#     #+#   #+#    #+#      #+#   #+#
     ###    ###       ###     ###    ########       ###    ###       ########       ###    ###      ###     ###    ########       ###    ###
                                                                                                                                   
                                                                                                                                """+Fore.BLUE+'By MusiGo'+Fore.WHITE)

def help():
     title()
     print(Fore.WHITE+"""

     Usage: hashcrack [parameter] 

     -v / --verbose = write detail of cracking in the terminal
     
     -h / --hash = specify the hash (sha256, md5, sha1, sha224, sha384, sha3_512, sha512, all)

     -m / --mode = specify the cracking mode to use
                | w = use wordlist mode
                | i = use incremental mode (10) character max

     -p / --path = specify the path of the wordlist to use

     --psswd = specify the password to crack

     -o / --output-file = specify the output file if password is found

     --help = show basic help message and exit

     -w / -wizzard = use the mode for beginner
"""+Fore.WHITE)

def wizzard():
        title()
        print(Fore.BLUE + """
1) sha256
2) md5
3) sha1
4) sha224
5) sha384
6) sha3_512
7) sha512
"""+Fore.WHITE)
        printage = input(Fore.BLUE +"choose your hash(1-9): "+Fore.WHITE)
        dmd = input(Fore.BLUE +"write your password hashed: "+Fore.WHITE)
        wordlist = input(Fore.BLUE +"write path of your wordlist for crack hashed password: "+Fore.WHITE)
        test1 = printage
        with open(f'{wordlist}', 'rb') as fichier:
                for ligne in fichier:
                        if int(test1) == 1:
                                test1234 = hashlib.sha256()
                        elif int(test1) == 2:
                                test1234 = hashlib.md5()
                        elif int(test1) == 3:
                                test1234 = hashlib.sha1()
                        elif int(test1) == 4:
                                test1234 = hashlib.sha224()
                        elif int(test1) == 5:
                                test1234 = hashlib.sha384()
                        elif int(test1) == 6:
                                test1234 = hashlib.sha3_512()
                        elif int(test1) == 7:
                                test1234 = hashlib.sha512()
                        ligne = ligne.strip()
                        test1234.update(ligne)
                        print(Fore.BLUE+ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                        if test1234.hexdigest() == dmd:
                                print(Fore.RED + "[+]password found: ", ligne)
                                sys.exit()
                print(Fore.WHITE+"[-]password not found"+Fore.WHITE)

verbose = False
mode = None
path = None
hashused = None
passwordtocrack = None
output_file = None


try:
        args = sys.argv[1]
        args2 = sys.argv[1:]
        nmb = len(args2)
        for loop in range(nmb):
                nmb-=1
                if args2[nmb-1] == "--verbose":
                        verbose = True
                if args2[nmb-1] == "-v":
                        verbose = True
                if args2[nmb-1] == "--hash":
                        hashused = args2[nmb]
                if args2[nmb-1] == "-h":
                        hashused = args2[nmb]
                if args2[nmb-1] == "--mode":
                        mode = args2[nmb]
                if args2[nmb-1] == "-m":
                        mode = args2[nmb]
                if args2[nmb-1] == "--path":
                        path = args2[nmb]
                if args2[nmb-1] == "-p":
                        path = args2[nmb]
                if args2[nmb-1] == "--passwd":
                        passwordtocrack = args2[nmb]
                if args2[nmb-1] == "-o":
                        output_file = args2[nmb]
                if args2[nmb-1] == "--output-file":
                        output_file = args2[nmb]

        if args == '--help':
                help()
        elif args == '--wizzard':
                wizzard()
        elif args == '-w':
                wizzard()

except IndexError as error:
        help()
        with open(f"{os.path.expanduser('~')}/.hashcrack.log", "a") as errorlogs:
                errorlogs.write(str(error) + "\n")
except Exception as allerror:
        with open(f"{os.path.expanduser('~')}/.hashcrack.log", "a") as errorlogs:
                errorlogs.write(str(allerror) + "\n")


def bywordlist():
        iteration = 0
        title()
        time.sleep(1.5)
        printage = hashused
        dmd = passwordtocrack
        wordlist = path
        test1 = printage
        with open(f'{wordlist}', 'rb') as fichier:
                for ligne in fichier:
                        if test1 == "all":
                                for loop in range(7):
                                        iteration += 1
                                        ligne = ligne.strip()
                                        if iteration == 1:
                                                test1234 = hashlib.sha256()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 2:
                                                test1234 = hashlib.md5()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 3:
                                                test1234 = hashlib.sha1()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 4:
                                                test1234 = hashlib.sha224()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 5:
                                                test1234 = hashlib.sha384()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 6:
                                                test1234 = hashlib.sha3_512()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                        elif iteration == 7:
                                                test1234 = hashlib.sha512()
                                                test1234.update(ligne)
                                                if verbose == True:
                                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                                if test1234.hexdigest() == dmd:
                                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                                        if(output_file != None):
                                                                with open(output_file, "w") as file_output_fichier:
                                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                                        sys.exit()
                                                iteration = 0
                                
                        else:
                                if test1 == "sha256":
                                        test1234 = hashlib.sha256()
                                elif test1 == "md5":
                                        test1234 = hashlib.md5()
                                elif test1 == "sha1":
                                        test1234 = hashlib.sha1()
                                elif test1 == "sha224":
                                        test1234 = hashlib.sha224()
                                elif test1 == "sha384":
                                        test1234 = hashlib.sha384()
                                elif test1 == "sha3_512":
                                        test1234 = hashlib.sha3_512()
                                elif test1 == "sha512":
                                        test1234 = hashlib.sha512()


                                ligne = ligne.strip()
                                test1234.update(ligne)
                                if verbose == True:
                                        print(Fore.BLUE + ligne.decode("utf-8"), ":", test1234.hexdigest()+Fore.WHITE)
                                if test1234.hexdigest() == dmd:
                                        print(Fore.RED + "[+]password found: ", ligne.decode("utf-8")+Fore.WHITE)
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + ligne.decode("utf-8"))
                                        sys.exit()
                print(Fore.WHITE+"[-]password not found"+Fore.WHITE)
combinaison = 0
def byincremental():
    title()
    time.sleep(1.5)
    def test(chaine, passwordtocrack):
        global combinaison
        combinaison += 1
        iteration = 0
        if hashused == "all":
                for loop in range(7):
                        iteration += 1
                        if iteration == 1:
                                hashhashhash = hashlib.sha256()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()

                        if iteration == 2:
                                hashhashhash = hashlib.md5()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()
                        
                        if iteration == 3:
                                hashhashhash = hashlib.sha1()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()

                        if iteration == 4:
                                hashhashhash = hashlib.sha224()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()

                        if iteration == 5:
                                hashhashhash = hashlib.sha384()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()

                        if iteration == 6:
                                hashhashhash = hashlib.sha3_512()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()

                        if iteration == 7:
                                hashhashhash = hashlib.sha512()
                                hashhashhash.update(chaine.encode("utf-8"))
                                if verbose == True:
                                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                                if hashhashhash.hexdigest() == passwordtocrack:
                                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                                        if(output_file != None):
                                                with open(output_file, "w") as file_output_fichier:
                                                        file_output_fichier.write("password: " + chaine)
                                        sys.exit()
                                iteration = 0
        else:

                if hashused == "sha256":
                        hashhashhash = hashlib.sha256()
                elif hashused == "md5":
                        hashhashhash = hashlib.md5()
                elif hashused == "sha1":
                        hashhashhash = hashlib.sha1()
                elif hashused == "sha224":
                        hashhashhash = hashlib.sha224()
                elif hashused == "sha384":
                        hashhashhash = hashlib.sha384()
                elif hashused == "sha3_512":
                        hashhashhash = hashlib.sha3_512()
                elif hashused == "sha512":
                        hashhashhash = hashlib.sha512()
                hashhashhash.update(chaine.encode("utf-8"))
                if verbose == True:
                        print(Fore.BLUE+chaine+" : "+hashhashhash.hexdigest()+Fore.WHITE)
                if hashhashhash.hexdigest() == passwordtocrack:
                        print(Fore.RED + "[+]password found: ", chaine+Fore.WHITE)
                        print(Fore.WHITE+"number of test: " + str(combinaison)+Fore.WHITE)
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print(Fore.WHITE+"time for found the password: " + str(elapsed_time) + "s")
                        if(output_file != None):
                                with open(output_file, "w") as file_output_fichier:
                                        file_output_fichier.write("password: " + chaine)
                        sys.exit()
    liste = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
        '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<',
        '.', '>', '/', '?'
    ]
    start_time = time.time()
    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, passwordtocrack)

                            for l7 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                                test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, passwordtocrack)

                            for l7 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                                test(chaine, passwordtocrack)

                                for l8 in liste:
                                    chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                    test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, passwordtocrack)

                            for l7 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                                test(chaine, passwordtocrack)

                                for l8 in liste:
                                    chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                    test(chaine, passwordtocrack)

                                    for l9 in liste:
                                        chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
                                        test(chaine, passwordtocrack)

    for l in liste:
        chaine = l
        test(chaine, passwordtocrack)

        for l2 in liste:
            chaine = l + l2
            test(chaine, passwordtocrack)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, passwordtocrack)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, passwordtocrack)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, passwordtocrack)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, passwordtocrack)

                            for l7 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                                test(chaine, passwordtocrack)

                                for l8 in liste:
                                    chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                    test(chaine, passwordtocrack)

                                    for l9 in liste:
                                        chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
                                        test(chaine, passwordtocrack)

                                        for l10 in liste:
                                            chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10
                                            test(chaine, passwordtocrack)

if verbose == False and mode == None and path == None and hashused == None and passwordtocrack == None and output_file == None:
      print("use --help parameter for help")
      sys.exit()
elif mode == None:
        print("use --help parameter for help")
        sys.exit()
elif hashused == None:
        print("use --help parameter for help")
        sys.exit()
elif passwordtocrack == None:
        print("use --help parameter for help")
        sys.exit()

if mode == "w":
        bywordlist()
elif mode == "i":
        byincremental()
        print(Fore.WHITE+"[-]the password it too longer 10 character max"+Fore.WHITE)
