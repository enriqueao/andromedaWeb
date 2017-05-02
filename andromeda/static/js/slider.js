
function atras() {
	var elemento = document.getElementById('slide');
	var margin = elemento.style.marginLeft;
	if (margin == '' || margin == '0%') {
		elemento.style = 'margin-left:-200%'
	} else if(margin == '-200%'){
		elemento.style = 'margin-left:-100%'
	} else if(margin == '-100%'){
		elemento.style = 'margin-left:0%'
	} else {
		elemento.style = 'margin-left:100%';
	}
}

function next() {
	var elemento = document.getElementById('slide');
	var margin = elemento.style.marginLeft;
	if (margin == '' || margin == '0%') {
		elemento.style = 'margin-left:-100%'
	} else if(margin == '-100%'){
		elemento.style = 'margin-left:-200%'
	} else if(margin == '-200%'){
		elemento.style = 'margin-left:0%'
	} else {
		elemento.style = 'margin-left:-100%';
	}
}
