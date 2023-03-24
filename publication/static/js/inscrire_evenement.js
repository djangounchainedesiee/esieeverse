const CSFR_TOKEN_INSCRIRE = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : '';

/**
 * Gère le succès de l'appel au vote et ajoute les champs nécessaire 
 * 
 * @param {JSON} response Une réponse Json
 */
const handleSuccessInscriptionEvenement = function (response) {
    const INSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #btn-inscription-evenement-${ evenement.id }`);
    INSCRIPTION_EVENEMENT_BUTTON.remove();
};

/**
 * Evènement AJAX
 */
$(document).ready(function () {
    $(".evenement-choixs .form-check .form-check-input").click(function () {
        const id_evenement = $(this).data("pk");
        //APPEL AJAX vers 'voter'
        $.ajax({
        url: "/inscrire/" + id_evenement + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_INSCRIRE ,
        },
        success: handleSuccessInscriptionEvenement,
        });
    });
});