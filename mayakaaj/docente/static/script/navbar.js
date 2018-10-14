/**
 * Created by Ampire on 12/10/18.
 */
function hover(element, name) {
    element.querySelector("#icon").setAttribute('src', '/static/icon/' + name);
}

function unhover(element, name) {
    element.querySelector("#icon").setAttribute('src', '/static/icon/' + name);
}