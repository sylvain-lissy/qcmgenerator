const addQcmForm = document.getElementById("addQcmForm")

//Ajouter les informations
const addInformation = document.createElement("div")
addInformation.classList.add("card-text", "border", "border-primary", "mb-2", "rounded", "rounded-3")            
addInformation.innerHTML = `                         
    <p class="bg-primary text-light ps-1 pb-0 m-0">INFORMATIONS :</p>
    <div class="form-check ps-1 pe-3">
    <div class="input-group m-1 me-0 pe-1">
        <input type="text" class="form-control" placeholder="Quel est le nom du QCM ?">
    </div>
    <div class="input-group m-1 me-0 pe-1">
        <input type="text" class="form-control" placeholder="Quel est le thème ?">
    </div>`
addQcmForm.appendChild(addInformation)

//Ajouter les questions
for (let i = 1; i < 11; i++) {
    const addQuestion = document.createElement("div")
    addQuestion.classList.add("card-text", "border", "border-primary", "mb-2", "rounded", "rounded-3")            
    addQuestion.innerHTML = `                         
            <p class="bg-primary text-light ps-1 pb-0 m-0">QUESTION ${i} :</p>
            <div class="form-check ps-1 pe-3">
                <div class="input-group m-1 me-0 pe-1">
                <input type="text" class="form-control" placeholder="intitulé de la question ${i} ...">
                </div>
                <div class="input-group mb-1 ps-1 pe-0 me-0">
                <div class="input-group-text">
                    <input class="form-check-input m-0" type="checkbox">
                </div>
                <input type="text" class="form-control" placeholder="réponse 1...">
                </div>
                <div class="input-group mb-1 ps-1 pe-0 me-0">
                <div class="input-group-text">
                    <input class="form-check-input m-0" type="checkbox">
                </div>
                <input type="text" class="form-control" placeholder="réponse 2...">
                </div>
                <div class="input-group mb-1 ps-1 pe-0 me-0">
                <div class="input-group-text">
                    <input class="form-check-input m-0" type="checkbox">
                </div>
                <input type="text" class="form-control" placeholder="réponse 3...">
                </div>
                <div class="input-group mb-1 ps-1 pe-0 me-0">
                <div class="input-group-text">
                    <input class="form-check-input m-0" type="checkbox">
                </div>
                <input type="text" class="form-control" placeholder="réponse 4...">
                </div>
            </div>`
    addQcmForm.appendChild(addQuestion)
}

//Ajouter le bouton du formulaire
const addButton = document.createElement("div")
addButton.classList.add("form-floating", "d-grid", "gap-2")            
addButton.innerHTML = `<button type="submit" class="btn btn-success btn-sm">Valider le Quizz<i class="bi bi-check2 ps-2"></i></button>`
addQcmForm.appendChild(addButton)