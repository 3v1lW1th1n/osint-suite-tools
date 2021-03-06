#*****************************************************************************
# Lista de targets para BuscadorPersonas.py
# Funcion "main"

target_list = "targets.txt"

# Lista de datos obtenidos de los diferentes bots
# Función "graphGenerator"

emailsData_list = []
phonesData_list = []
wikipediaData_list = []
youtubeData_list = []
companiesData_list = []
DNIData_list = []

#*****************************************************************************
# Lista de politicos de espana investigados o condenados
# Archivo findData.py

politicosSpain_investigados = "data/Corruptos/list-spain-11-5-2019.txt"

#*****************************************************************************
# Banner principal

banner = """
▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓▓█████   ██████      ▄████  ▄▄▄     ▄▄▄█████▓▓█████   ██████    
▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒     ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒    
░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ░ ▓██▄      ▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ░ ▓██▄      
░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒   ░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒   
░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░▒████▒▒██████▒▒   ░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒▒██████▒▒   
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░    ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░   
 ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░░ ░▒  ░ ░     ░   ░   ▒   ▒▒ ░   ░     ░ ░  ░░ ░▒  ░ ░   
 ░ ░  ░   ░   ▒      ░   ░ ░   ░         ░   ░  ░  ░     ░ ░   ░   ░   ▒    ░         ░   ░  ░  ░     
   ░          ░  ░         ░             ░  ░      ░           ░       ░  ░           ░  ░      ░     
 ░                                                                                                    
____________________________________________________________________________________________________

License: GNU 3.0 | AUTOR: Jorge Coronado | Twitter: @JorgeWebsec | Contact: jorgewebsec[@] gmail.com
____________________________________________________________________________________________________

Version: 1.0 | Date: 17/04/2020 | Description: Search engines and add new BuscadorTelefono.py
Version: 1.1 | Date: 10/05/2020 | Description: parser in URLS and graph report generator
Version: 1.2 | Date: 01/06/2020 | Description: add facebook search and to correct bugs
____________________________________________________________________________________________________

Discleimer: This application allows you to create intelligence through open sources. 
You do not access information that is not public. The author is not responsible for its use.
____________________________________________________________________________________________________

Description: Dante's Gates Minimal Version is an open application with a GNU license for OSINT with
Spanish and international sources. Currently it is maintained by Jorge Coronado and there are other
versions such as mobile and APIs for your applications.
----
Description: Dante's Gates Minimal Version is an open application with a GNU license for OSINT with
Spanish and international sources. Currently it is maintained by Jorge Coronado and there are other
versions such as mobile and APIs for your applications.

"""

