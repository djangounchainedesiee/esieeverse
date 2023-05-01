const CSFR_TOKEN_INSCRIRE_DESINSCRIRE = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : '';

/**
 * Réceptionne le clic du bouton d'inscription
 */
const handleClickInscriptionEvenement = function () {
    const id_evenement = $(this).data("pk");
    $.ajax({
    url: "http://127.0.0.1:8000/publication/inscrire/" + id_evenement + "/",
    type: "POST",
    data: {
        csrfmiddlewaretoken: CSFR_TOKEN_INSCRIRE_DESINSCRIRE ,
    },
    success: handleSuccessInscriptionEvenement,
    });
}

/**
 * Réceptionne le clic du bouton de desinscription
 */
const handleClickDesInscriptionEvenement = function () {
    const id_evenement = $(this).data("pk");
    $.ajax({
    url: "http://127.0.0.1:8000/publication/desinscrire/" + id_evenement + "/",
    type: "POST",
    data: {
        csrfmiddlewaretoken: CSFR_TOKEN_INSCRIRE_DESINSCRIRE ,
    },
    success: handleSuccessDesInscriptionEvenement,
    });
}

/**
 * Gère le succès de l'appel à l'inscription d'un évènement
 * @param {JSON} response Une réponse Json
 */
const handleSuccessInscriptionEvenement = function (response) {
    const INSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #btn-inscription-evenement-${ response.id_evenement }`);
    INSCRIPTION_EVENEMENT_BUTTON.off('click');
    INSCRIPTION_EVENEMENT_BUTTON.text('Inscris');
    INSCRIPTION_EVENEMENT_BUTTON.attr('id', `text-inscris-evenement-${ response.id_evenement }`);
    INSCRIPTION_EVENEMENT_BUTTON.removeAttr('data-pk');
    INSCRIPTION_EVENEMENT_BUTTON.removeClass('btn btn-link inscription');

    const DESCRIPTION_EVENEMENT = $(`#user-event-${ response.id_evenement } .we-video-info .description`);
    const DESINSCRIPTION_EVENEMENT_BUTTON_HTML = 
    `<span id="btn-desinscription-evenement-${ response.id_evenement }" class="btn btn-link desinscription" data-pk="${ response.id_evenement }">`
    + 'Se Désinscrire' 
    + '</span>';
    DESCRIPTION_EVENEMENT.append(DESINSCRIPTION_EVENEMENT_BUTTON_HTML);

    const DESINSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #btn-desinscription-evenement-${ response.id_evenement }`);
    DESINSCRIPTION_EVENEMENT_BUTTON.click(handleClickDesInscriptionEvenement);
};

const handleSuccessDesInscriptionEvenement = function (response) {
    const DESINSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #btn-desinscription-evenement-${ response.id_evenement }`);
    DESINSCRIPTION_EVENEMENT_BUTTON.off('click');
    DESINSCRIPTION_EVENEMENT_BUTTON.remove();

    const INSCRIPTION_EVENEMENT_BUTTON = $(`#user-event-${ response.id_evenement } .we-video-info .description #text-inscris-evenement-${ response.id_evenement }`);
    INSCRIPTION_EVENEMENT_BUTTON.text("S'inscrire");
    INSCRIPTION_EVENEMENT_BUTTON.addClass('btn btn-link inscription');
    INSCRIPTION_EVENEMENT_BUTTON.attr('data-pk', response.id_evenement);
    INSCRIPTION_EVENEMENT_BUTTON.attr('id', `btn-inscription-evenement-${ response.id_evenement }`);
    INSCRIPTION_EVENEMENT_BUTTON.on('click', handleClickInscriptionEvenement);
};

/**
 * Evènement AJAX
 */
$(document).ready(function () {
    $(".we-video-info .description .inscription").click(handleClickInscriptionEvenement);
    $(".we-video-info .description .desinscription").click(handleClickDesInscriptionEvenement);
});