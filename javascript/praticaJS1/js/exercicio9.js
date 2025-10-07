function haOnzeDigitos(cpf) {
    let tamanho = cpf.length
    if (tamanho == 11){
        return true
    }
    else{
        return false
    }
}

function todosOsOnzeDigitosSaoNumeros(cpf) {
    let list_cpf = cpf.split('')
    for (let i of list_cpf) {
        if (isNaN(i)){
            return false
        }
    }
    return true
}

function osOnzeNumerosSaoDiferentes(cpf) {
    let list_cpf = cpf.split('')
    let count = 0
    let i= 0
    while (i < list_cpf.length - 1) {
        if (list_cpf[i] == list_cpf[i+1]){
            count += 1
        }
        i += 1
        console.log(count)
    }
    if (count != 10) {
        return true
        }
    return false
}
function oPrimeiroDigitoVerificadorEhValido(cpf) {
    let list_cpf = cpf.split('')
    let i = 0
    let soma = 0
    for (mult = 10; mult >= 2; mult--){
        soma += list_cpf[i]*mult
        i += 1
    }
    let resto = (soma*10) % 11
    if (resto = 10){
        resto = 0
    }
    if (resto == list_cpf[9]){
        return true
    }
    return false
}

function oSegundoDigitoVerificadorEhValido(cpf) {
    let list_cpf = cpf.split('')
    let i = 0
    let soma = 0
    for (mult = 11; mult >= 2; mult--){
        soma += list_cpf[i]*mult
        i += 1
    }
    let resto = (soma*10) % 11
    if (resto = 10){
        resto = 0
    }
    if (resto == list_cpf[10]){
        return true
    }
    return false
}





//------------------- Não edite abaixo ----------------------------
function validarCPF(validacao, cpf) {
    switch (validacao) {
        case "onzeDigitos": return haOnzeDigitos(cpf)
        case "onzeSaoNumeros": return todosOsOnzeDigitosSaoNumeros(cpf) && validarCPF("onzeDigitos", cpf)
        case "naoSaoTodosIguais": return osOnzeNumerosSaoDiferentes(cpf) && validarCPF("onzeSaoNumeros", cpf)
        case "verificador10": return oPrimeiroDigitoVerificadorEhValido(cpf) && validarCPF("naoSaoTodosIguais", cpf)
        case "verificador11": return oSegundoDigitoVerificadorEhValido(cpf) && validarCPF("verificador10", cpf)

        default:
            console.error(validacao+" é um botão desconhecido...")
            return false
    }
}


function tratadorDeCliqueExercicio9(nomeDoBotao) {
    const cpf = document.getElementById("textCPF").value

    const validacao = (nomeDoBotao === "validade") ? "verificador11": nomeDoBotao
    const valido = validarCPF(validacao, cpf)
    const validoString = valido ? "valido": "inválido"
    const validadeMensagem = "O CPF informado ("+cpf+") é "+ validoString
    console.log(validadeMensagem)

    if (nomeDoBotao !== "validade") {
        let divResultado = document.getElementById(validacao);
        divResultado.textContent = validoString
        divResultado.setAttribute("class", valido ? "divValidadeValido": "divValidadeInvalido")    
    } else {
        window.alert(validadeMensagem)
    }

    
}