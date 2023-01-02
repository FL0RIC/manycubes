#--------------------------------------------------------------------------------#
#                                                                                #
#                                   ManyCubes                                    #
#                                                                                #
#--------------------------------------------------------------------------------#

import os
from time import sleep
import csv

'''

version = input("version : ")


def open_server(version):
   ''''''Open a minecraft server with the version wanted''''''
    os.chdir(f"minecraft_jar\minecraft_{version}")
    os.system(f"minecraft_server_{version}.jar nogui")


if not("eula.txt" in os.listdir(f"minecraft_jar\minecraft_{version}")) : # Check if the version was already opened before
    open_server(version) # Create everthing needed to start the server
    fichier_eula = open("eula.txt", "r")
    contenue = fichier_eula.read()
    fichier_eula.close()
    index = (contenue.find("eula=false"), contenue.find("eula=false") + len("eula=false"))
    contenue = contenue[:index[0]]+ "eula=true" + contenue[index[1]:]
    fichier_eula = open(f"eula.txt", "w")
    fichier_eula.write(contenue)
    fichier_eula.close()
os.system("cmd")
open_server(version)
'''
print(os.listdir("minecraft_jar\minecraft_1.19.3"))

os.system("start.bat")
print("fin")