from django.contrib import auth
from .models import *
from django.contrib.auth.models import User

def getting_authenticate_info(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	get_username = UsersAuthorisation.objects.filter(session_key=session_key, authorisation_status=True)
	authenticate_status = bool(get_username)
	if authenticate_status == True:
		username = list(get_username)[0]
		superuser_status = User.objects.get(username = username).is_superuser#for personal office
	else:
		username = None
	return locals()