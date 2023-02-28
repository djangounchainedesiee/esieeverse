const CSFR_TOKEN = document.querySelector('[name=csrfmiddlewaretoken]').value;

const handleSuccess = (response) => {
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
            csrfmiddlewaretoken: CSFR_TOKEN,
        },
        success: handleSuccess,
        });
    });

    $(".publication-action-buttons .dislike").click(function () {
      const id_publication = $(this).data("pk");
      $.ajax({
        url: "/publication/dislike/" + id_publication + "/",
        type: "POST",
        data: {
          csrfmiddlewaretoken: CSFR_TOKEN,
        },
        dataType: "json",
        success: handleSuccess,
      });
    });
});