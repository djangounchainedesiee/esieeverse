from django.shortcuts import redirect
from django.http import HttpRequest

def check_utilisateur_auth(request: HttpRequest) -> bool:
    """Vérifie si l'utilisateur est connecté et qu'il est connecté au bon type utilisateur

    Args:
        request (HttpRequest): La requête contenant l'utilisateur
    """
    return request.user.is_authenticated or (hasattr(request.user, 'utilisateur') and request.user.utilisateur is not None)