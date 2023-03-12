const CSFR_TOKEN_PUBLICATION = document.querySelector('[name=csrfmiddlewaretoken]') ? document.querySelector('[name=csrfmiddlewaretoken]').value : NULL;

const handleSuccessPublication = (response) => {
    var badge = $(`#user-post-${response.id} .publication-action-buttons .like ins`);
    badge.text(response.nb_likes);
    console.log('Badge like : ', badge)
    badge = $(`#user-post-${response.id} .publication-action-buttons .dislike ins`);
    badge.text(response.nb_dislikes);
  };

$(document).ready(function () {
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