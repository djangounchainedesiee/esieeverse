let choiceIndex = 0;

$(document).ready(function () {
    $("#create-evenement-form #form-evenement-add-choice-btn").click(function () {
        choiceIndex++;
        const CHOICE_CONTAINER = document.querySelector("#create-evenement-form #form-evenement-choices-container")
        const CHOICE_P = document.createElement("p");
        CHOICE_P.classList.add("choice");
        CHOICE_P.innerHTML = `
        <label for="id_nom_choix">Nom choix n° ${choiceIndex}</label>
        <input type="text" name="nom_choix" class="form-control" required="" id="id_nom_choix" maxlength="60">
        `;
        CHOICE_CONTAINER.appendChild(CHOICE_P);
    });
});