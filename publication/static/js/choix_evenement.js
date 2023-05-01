const CSFR_TOKEN_CHOIX = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : '';

/**
 * Gère le succès de l'appel au vote et ajoute les champs nécessaire 
 * 
 * @param {JSON} response Une réponse Json
 */
const handleSuccessChoix = function (response) {
    const TOTAL_VOTES = response.total_votes
    // Pour chaque choix on affiche une barre de progression en tant que résultat
    for (const choix of response.choixs) {
        // Récupération du champ HTML input relatif au choix, suppresion de l'évent et du champ
        const CHOIX_INPUT_FIELD = $(`.evenement-choixs .form-check #evenement-choix-${choix.id}`);
        CHOIX_INPUT_FIELD.off('click');
        CHOIX_INPUT_FIELD.remove();
        
        // Calcul du pourcentage et création d'une barre de pourcentage
        const PROGRESS_BAR_HTML = `
            <div class="progress flex-grow-1">
                <div class="progress-bar bg-success" role="progressbar" style="width: ${choix.pourcentage}%;" aria-valuenow="${choix.nb_votes}" aria-valuemin="0" aria-valuemax="${TOTAL_VOTES}">${choix.pourcentage}%</div>
            </div>
        `;

        // Récupération de la div parent et ajout de la progress bar
        const CHOIX_DIV = $(`.evenement-choixs .form-check #evenement-label-choix-${choix.id}`).parent();
        CHOIX_DIV.append(PROGRESS_BAR_HTML);
    }
};

/**
 * Evènement AJAX
 */
$(document).ready(function () {
    $(".evenement-choixs .form-check .form-check-input").click(function () {
        const id_choix = $(this).data("pk");
        //APPEL AJAX vers 'voter'
        $.ajax({
        url: "/voter/" + id_choix + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_CHOIX ,
        },
        success: handleSuccessChoix,
        });
    });
});