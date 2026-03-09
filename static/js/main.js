function previewImage(input){

    const preview = document.getElementById("preview");

    const file = input.files[0];

    if(file){
        preview.src = URL.createObjectURL(file);
    }

}

function loading(){

    document.getElementById("btn").innerText="Processing...";
}

function previewImage(input){

    const preview = document.getElementById("preview");

    const file = input.files[0];

    if(file){
        preview.src = URL.createObjectURL(file);
    }

}