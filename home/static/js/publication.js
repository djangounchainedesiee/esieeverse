const CSFR_TOKEN_PUBLICATION = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : NULL;

/**
 * Gère le succès de l'appel de la vue like / dislike et ajoute les champs nécessaire 
 * 
 * @param {JSON} response Une réponse Json
 */
const handleSuccessPublication = (response) => {
    // récupération du badge du nb de like/dislike et changement de sa valeur
    var badge = $(`#user-post-${response.id} .publication-action-buttons .like ins`);
    badge.text(response.nb_likes);

    badge = $(`#user-post-${response.id} .publication-action-buttons .dislike ins`);
    badge.text(response.nb_dislikes);
  };

/**
 * Evènement AJAX
 */  
$(document).ready(function () {
    /**
     * Evènement like
     */
    $(".publication-action-buttons .like").click(function () {
        const id_publication = $(this).data("pk");
        $.ajax({
        url: "/publication/like/" + id_publication + "/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSFR_TOKEN_PUBLICATION ,
        },
        success: handleSuccessPublication,
        });
    });

    /**
     * Evènement dislike
     */
    $(".publication-action-buttons .dislike").click(function () {
      const id_publication = $(this).data("pk");
      $.ajax({
        url: "/publication/dislike/" + id_publication + "/",
        type: "POST",
        data: {
          csrfmiddlewaretoken: CSFR_TOKEN_PUBLICATION,
        },
        dataType: "json",
        success: handleSuccessPublication,
      });
    });
});