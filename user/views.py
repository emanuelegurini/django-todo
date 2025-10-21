from django.http import JsonResponse
from .models import User

"""
In Django la view ha lo stesso ruolo del controller nel pattern MVC (in pattern usiamo MTV).
Quindi la view e una funzione che riceve le richieste e restituisce le risposte. 

https://www.programmareinpython.it/blog/che-cosa-rende-django-speciale-miglior-web-framewo/
"""

def users_list(request):
	users = User.objects.all()
 	# Serialize the QuerySet into a list of dictionaries using .values

	print(f'users: ${users}')
	data = list(users.values('id', 'first_name', 'last_name', 'email'))	

	"""
	Il parametro 'safe=False' e necessario per l'invio di una lista:
		- di default JsonResponse accetta solo dizionari (safe=True), come meccanismo di sicurezza per evitare di splorre dati non strutturati o sensibili in modo involontario 
		- Se passi un oggetto che non è un dizionario con safe=True, Django genera un errore

	Differenze tra lista e dizionario:
		- lista:
			- nomi = ['Ada', 'Neri', 2]

		- dizionario: 
			- persona = {'nome': 'Ada', 'cognome': 'Neri', 'eta': 25}
	"""

	return JsonResponse(data, safe=False)
