const CSFR_TOKEN_FOLLOWER = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : '';

const handleSuccessAbonne = function (response) {
    const ADD_FRIEND = $(`#id-utilisateur-${response.id_utilisateur_to_add} .friend-meta .add_friend`);
    ADD_FRIEND.removeClass('add_friend');
    ADD_FRIEND.text("Abonné");
    ADD_FRIEND.off('click');
};

const handleSuccessDesabonne = function () {
    location.reload();
};


const handleSuccessAbonneProfilTopBar = function(){
    location.reload();
}

$(document).ready(function () {
    $(".followers .friend-meta .add_friend").click(function () {
        const id_utilisateur = $(this).data("pk");
        $.ajax({
        url: "/add_friend/" + id_utilisateur + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_CHOIX ,
        },
        success: handleSuccessAbonne,
        });
    });
    $(".followers .friend-meta .delete_friend").click(function () {
        const id_utilisateur = $(this).data("pk");
        $.ajax({
        url: "/add_friend/" + id_utilisateur + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_CHOIX ,
        },
        success: handleSuccessDesabonne,
        });
    });
    $(".add-btn .add_friend").click(function () {
        const id_utilisateur = $(this).data("pk");
        $.ajax({
        url: "/add_friend/" + id_utilisateur + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_CHOIX ,
        },
        success: handleSuccessAbonneProfilTopBar,
        });
    });
});