const CSFR_TOKEN_CHOIX = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : NULL;

const handleSuccessChoix = function (response) {
    for (const choix of response.choixs) {
        console.log('Choix : ', choix)
        const CHOIX = $(`.evenement-choixs .form-check .form-check-input #${choix.id}`);
        //CHOIX.text = choix.utilisateurs
        CHOIX.off('click');
    }
};

$(document).ready(function () {
    $(".evenement-choixs .form-check .form-check-input").click(function () {
        console.log('Click choix : ')
        const id_choix = $(this).data("pk");
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