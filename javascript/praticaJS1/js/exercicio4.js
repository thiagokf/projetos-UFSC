function tratadorDeCliqueExercicio4() {
    let numero = window.prompt("Escreva um numerozudo:")

    numero = Number(numero)

    if (numero >= 30 && numero <= 50) {
        console.log(numero + " está no intervalo [30,50].");
    }
    else if (numero >=60 && numero <= 100) {
        console.log(numero + " está no intervalo [60,100]");
    }
    else {
       console.log("O número informado não está em nenhum dos dois intervalos."); 
    }
}