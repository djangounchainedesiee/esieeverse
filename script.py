import random
from django.contrib.auth.models import User
from esieeverse.models import Filiere, Promotion, Utilisateur

def generate_users(num_users):
    filieres = Filiere.objects.all()
    promotions = Promotion.objects.all()

    usernames = [
        'john_doe', 'jane_smith', 'mike_jackson', 'emily_wilson', 'alexander_brown',
        'sophia_johnson', 'liam_thompson', 'olivia_clark', 'william_harris', 'ava_lewis',
        'james_martin', 'isabella_hall', 'benjamin_lee', 'mia_taylor', 'lucas_miller',
        'charlotte_anderson', 'samuel_thomas', 'sarah_walker', 'henry_mitchell', 'grace_ward',
        'david_ross', 'amelia_harris', 'joseph_adams', 'abigail_carter', 'mason_cook',
        'elizabeth_bell', 'oliver_james', 'emily_baker', 'jacob_nelson', 'chloe_parker',
        'matthew_green', 'ella_white', 'aiden_hughes', 'sophie_campbell', 'jayden_hill',
        'lily_roberts', 'daniel_morgan', 'avery_evans', 'noah_kelly', 'zoey_richardson',
        'ryan_wood', 'addison_wright', 'ethan_bailey', 'aubrey_cooper', 'williamson_foster',
        'charles_murphy', 'grace_allen', 'hudson_stewart', 'scarlett_cox', 'jackson_peterson'
    ]

    first_names = [
        'John', 'Jane', 'Mike', 'Emily', 'Alexander',
        'Sophia', 'Liam', 'Olivia', 'William', 'Ava',
        'James', 'Isabella', 'Benjamin', 'Mia', 'Lucas',
        'Charlotte', 'Samuel', 'Sarah', 'Henry', 'Grace',
        'David', 'Amelia', 'Joseph', 'Abigail', 'Mason',
        'Elizabeth', 'Oliver', 'Emily', 'Jacob', 'Chloe',
        'Matthew', 'Ella', 'Aiden', 'Sophie', 'Jayden',
        'Lily', 'Daniel', 'Avery', 'Noah', 'Zoey',
        'Ryan', 'Addison', 'Ethan', 'Aubrey', 'Williamson',
        'Charles', 'Grace', 'Hudson', 'Scarlett', 'Jackson'
    ]

    last_names = [
        'Doe', 'Smith', 'Jackson', 'Wilson', 'Brown',
        'Johnson', 'Thompson', 'Clark', 'Harris', 'Lewis',
        'Martin', 'Hall', 'Lee', 'Taylor', 'Miller',
        'Anderson', 'Thomas', 'Walker', 'Mitchell', 'Ward',
        'Ross', 'Harris', 'Adams', 'Carter', 'Cook',
        'Bell', 'James', 'Baker', 'Nelson', 'Parker',
        'Green', 'White', 'Hughes', 'Campbell', 'Hill',
        'Roberts', 'Morgan', 'Evans', 'Kelly', 'Richardson',
        'Wood', 'Wright', 'Bailey', 'Cooper', 'Foster',
        'Murphy', 'Allen', 'Stewart', 'Cox', 'Peterson'
    ]

    for i in range(num_users):
        # Création d'un utilisateur Django
        username = usernames[i]
        password = f'password{i}'
        user = User.objects.create_user(username=username, password=password)

        # Sélection aléatoire d'une filière et d'une promotion
        filiere = random.choice(filieres)
        promotion = random.choice(promotions)

        # Création de l'utilisateur avec la filière et la promotion sélectionnées
        utilisateur = Utilisateur.objects.create(user=user, filiere=filiere, promotion=promotion)

        # Attribution d'un prénom et d'un nom cohérents
        first_name = first_names[i % len(first_names)]
        last_name = last_names[i % len(last_names)]
        user.first_name = first_name
        user.last_name = last_name
        user.save()

generate_users(50)
