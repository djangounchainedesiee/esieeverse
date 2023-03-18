from django import template

register = template.Library()

@register.filter
def percentage(nb1: int, nb2: int) -> int:
    """Calcule un pourcentage entre deux nombres

    Args:
        nb1 (int): Premier nombre
        nb2 (int): Deuxième nombre

    Returns:
        int: Le pourcentage
    """
    return (nb1 * 100) / nb2