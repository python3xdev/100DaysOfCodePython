let root = document.documentElement;
var computed_style = getComputedStyle(document.body)

var current_theme = 'dark'
var icon_bar_out = true

// Create 3 functions
// function 1 - will call function 2 or 3 depending on what them is currently on
// function 2 - will change the website to light theme
// function 3 - will change the wensite to dark theme
function ChangeTheme() {
	if (current_theme === 'dark') {
		current_theme = 'light'

		document.getElementById('themeChangerIcon').className = 'far fa-moon'
		// document.getElementById('body').className = 'bodyBackgroundLight'

		root.style.setProperty('--background-color', '#e6e6e6');
		root.style.setProperty('--main-div-color', '#fdf5e6');
		root.style.setProperty('--text-color', '#353535');
	}
	else {
		current_theme = 'dark'

		document.getElementById('themeChangerIcon').className = 'far fa-sun'
		// document.getElementById('body').className = 'bodyBackgroundDark'

		root.style.setProperty('--background-color', '#3a3a3a');
		root.style.setProperty('--main-div-color', '#2e2e2e');
		root.style.setProperty('--text-color', '#cacaca');
	}
}

function ToggleSidebar() {
	if (icon_bar_out) {
		icon_bar_out = false
		document.getElementById('toggleMenuIcon').className = 'fas fa-arrow-alt-circle-right'
		document.getElementById('sidebar-social-icon-twitter').classList.add('hideItem');
		document.getElementById('sidebar-social-icon-discord').classList.add('hideItem');
		document.getElementById('sidebar-social-icon-github').classList.add('hideItem');
		document.getElementById('sidebar-social-icon-linkedin').classList.add('hideItem');
		document.getElementById('sidebar-social-icon-youtube').classList.add('hideItem');
		document.getElementById('themeChanger').classList.add('hideItem');
	}
	else {
		icon_bar_out = true
		document.getElementById('toggleMenuIcon').className = 'fas fa-arrow-alt-circle-left'
		document.getElementById('sidebar-social-icon-twitter').classList.remove('hideItem');
		document.getElementById('sidebar-social-icon-discord').classList.remove('hideItem');
		document.getElementById('sidebar-social-icon-github').classList.remove('hideItem');
		document.getElementById('sidebar-social-icon-linkedin').classList.remove('hideItem');
		document.getElementById('sidebar-social-icon-youtube').classList.remove('hideItem');
		document.getElementById('themeChanger').classList.remove('hideItem');
	}
}


// --------------------- Self Typing Sentence ---------------------
async function typeSentence(sentence, eleRef, delay = 100) {
	const letters = sentence.split("");
	let i = 0;
	while(i < letters.length) {
		await waitForMs(delay);
		$(eleRef).append(letters[i]);
		i++
	}
	return;
}

async function deleteSentence(eleRef) {
	const sentence = $(eleRef).html();
	const letters = sentence.split("");
	let i = 0;
	while(letters.length > 0) {
		await waitForMs(100);
		letters.pop();
		$(eleRef).html(letters.join(""));
	}
}

function waitForMs(ms) {
	return new Promise(resolve => setTimeout(resolve, ms))
}

const carouselText = [
{text: "Daniel.", color: computed_style.getPropertyValue('--blue')},
{text: "a Software Engineering Student.", color: computed_style.getPropertyValue('--green')},
]

async function carousel(carouselList, eleRef) {
	var i = 0;
	while (true) {
		updateFontColor(eleRef, carouselList[i].color)
		await typeSentence(carouselList[i].text, eleRef);
		await waitForMs(1500);
		await deleteSentence(eleRef);
		await waitForMs(500);
		i++
		if(i >= carouselList.length) {i = 0;}
	}
}

function updateFontColor(eleRef, color) {
	$(eleRef).css('color', color);
}

window.onload = carousel(carouselText, '#feature-text') // Starting the 'animation'.
// ----------------------------------------------------------------
