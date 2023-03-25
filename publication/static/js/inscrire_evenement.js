const CSFR_TOKEN_INSCRIRE = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : '';

/**
 * Gère le succès de l'appel à l'inscription d'un évènement
 * @param {JSON} response Une réponse Json
 */
const handleSuccessInscriptionEvenement = function (response) {
    const INSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #btn-inscription-evenement-${ response.id_evenement }`);
    INSCRIPTION_EVENEMENT_BUTTON.off('click');
    INSCRIPTION_EVENEMENT_BUTTON.text('Inscris');
    INSCRIPTION_EVENEMENT_BUTTON.removeClass('btn btn-link');
};

/**
 * Evènement AJAX
 */
$(document).ready(function () {
    $(".we-video-info .description .btn").click(function () {
        const id_evenement = $(this).data("pk");
        $.ajax({
        url: "http://127.0.0.1:8000/publication/inscrire/" + id_evenement + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_INSCRIRE ,
        },
        success: handleSuccessInscriptionEvenement,
        });
    });
});