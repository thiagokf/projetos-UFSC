function tratadorDeCliqueExercicio3() {
    let msg = window.prompt("escreva sua mensagem:")

    let list_msg = []
    for (const valor of msg) {
        list_msg.push(valor)
    }
    console.log(list_msg)

    let nova_msg = ""

    for (let i= 1; i < list_msg.length - 1; i++){
        nova_msg += list_msg[i]
    }

    window.alert(nova_msg)
}