function inversor_string(){
    let string = window.prompt("escreva a mensagem a ser invertida")
    let list_string = []
    for (const valor of string) {
        list_string.push(valor)
    }
    const tamanho_str = list_string.length

    let str_invert = ""

    for (let i = tamanho_str - 1; i >= 0; i--){
        str_invert += list_string[i]
    }
    window.alert(str_invert)
}
// outra forma de fazer (bem mais facil)
/*
function inversor_string_simples(){
    let string = window.prompt("escreva a mensagem a ser invertida")
    let str_invert = string.split('').reverse().join('');
    window.alert(str_invert)
}
   */ 