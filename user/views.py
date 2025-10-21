from django.http import JsonResponse
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt #TODO: eliminare (utilizzo a fini didattici)
def add_user(request):
	if request.method == "POST":
		try:
			data = json.loads(request.body)

			new_user = User.objects.create(
				first_name = data.get('first_name'),
				last_name = data.get('last_name'),
				email = data.get('email')
			)

			response_data = {
				'id': new_user.id, 
				'first_name': new_user.first_name,
				'last_name': new_user.last_name,
				'email': new_user.email
			}

			return JsonResponse(response_data, status=201)
	

		except (json.JSONDecodeError, KeyError) as e:
			return JsonResponse({'error': 'Invalid data provided'}, status=400)

	else:
		return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
