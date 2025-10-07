function convertCelciusToFahrenheit(celcius) {
	let fahrenheit
	fahrenheit = (celcius * 1.8) + 32
	return fahrenheit
}

// -- Não edite abaixo!

function conversaoCtoF() {
	let textCelcius = document.getElementById("celciusText")
	let textFahrenheit = document.getElementById("resultFahrenheit")
	textFahrenheit.textContent = convertCelciusToFahrenheit(textCelcius.value) + 
								 "ºF"
}