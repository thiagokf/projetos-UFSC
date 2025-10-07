/* iniciar apenas com home */
let login_body = document.getElementById("login-body")
login_body.style.display = "none"
let nova_conta = document.getElementById("nova-conta")
nova_conta.style.display = "none"
let home = document.getElementById("divHome")

function mostrarApenasLogin() {
    login_body.style.display = "block"
    nova_conta.style.display = "none"
    home.style.display = "none"
    caixa_email.value = ""
    caixa_senha.value = ""
}

function mostrarApenasConta() {
    nova_conta.style.display = "block"
    home.style.display = "none"
    login_body.style.display = "none"
}

function mostrarApenasHome() {
    login_body.style.display = "none"
    nova_conta.style.display = "none"
    home.style.display = "block"
}

/* tratamento das caixar do login */
let caixa_email = document.getElementById("email")
let caixa_senha = document.getElementById("login-password")
let botao_login = document.getElementById("botaoLogin")
botao_login.disabled = true;

function verificaCampos() {
    const emailValue = caixa_email.value.trim()
    const passwordValue = caixa_senha.value.trim()

    const camposPreenchidos = emailValue.length > 0 && passwordValue.length > 0 & emailValue.includes('@');
    if (camposPreenchidos == true) {
        botao_login.disabled = false;
    }
    else {
        botao_login.disabled = true;
    }
}
caixa_email.addEventListener('input', verificaCampos);
caixa_senha.addEventListener('input', verificaCampos);

