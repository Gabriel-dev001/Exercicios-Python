import random

Server_1 = []
Server_2 = []
Server_3 = []

def Main():
    print(f"Server 1 - {len(Server_1)} Users")
    print(f"Server 2 - {len(Server_2)} Users")
    print(f"Server 3 - {len(Server_3)} Users")

    choice = input()

    if choice == "":
        Distribution()
    else:
        Restructure()


def Distribution():
    server = balancing()

    match(server):
        case "server1":
            Server_1.append("|")

        case "server2":
            Server_2.append("|")

        case "server3":
            Server_3.append("|") 

    Main()

def balancing():    #VERIFICAR QUAL SERVIDOR TEM MENOS USUARIO/CHECK WHICH SERVER HAS LESS USER

    if len(Server_1) == len(Server_2) and len(Server_1) == len(Server_3):
        return "server1"

    if len(Server_1)<=len(Server_2) and len(Server_1)<=len(Server_3):
        return "server1"
    
    if len(Server_2)<=len(Server_1) and len(Server_2)<=len(Server_3):
        return "server2"
    
    if len(Server_3)<=len(Server_1) and len(Server_3)<=len(Server_2):
        return "server3"
    
#-----

def Restructure():
    (server_delet) = random.randint(1, 3)   #IREI TIRAR UM USUARIO DE UM SERVER ALEATORIO/WILL TAKE A USER FROM A RANDOM SERVER


    match(server_delet):
        case 1:
            if len(Server_1) != 0:
                ramdom_user = random.randint(0, len(Server_1)-1)
                del Server_1[ramdom_user]

        case 2:
            if len(Server_2) != 0:
                ramdom_user = random.randint(0, len(Server_2)-1)
                del Server_2[ramdom_user]

        case 3:
            if len(Server_3) != 0:
                number_users = len(Server_3)
                ramdom_user = random.randint(0, len(Server_3)-1)
                del Server_3[ramdom_user]

    Main()

Main()