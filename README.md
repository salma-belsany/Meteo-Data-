Installer dépendances:
pip install -r requirements.txt
------------------
lancement de projet : 
depuis "\meteo"  avec cmd : "python .\__main__.py"
------------------
teste unitaire : 
"python -m pytest --cov=services --cov=data_structures --cov=utils --cov=config --cov-report=term-missing -v"
------------------
Docker: 
Pour Lance un conteneur Docker en mode INTERACTIF avec terminal:docker run -it mon-image
