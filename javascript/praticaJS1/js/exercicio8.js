function obterRegiaoFiscalAtravesDoCPFInformado(cpfInformado) {
    //edite esta função!
    let regiaoFiscal = undefined
    console.log(cpfInformado)
    if (cpfInformado[8] == 1) {
        regiaoFiscal = ('DF, GO, MT, MS e TO')
    }
    else if (cpfInformado[8] == 2) {
        regiaoFiscal = ('AC, AP, AM, PA, RO e RR')
    }
    else if (cpfInformado[8] == 3) {
        regiaoFiscal = ('CE, MA e PI')
    }
    else if (cpfInformado[8] == 4) {
        regiaoFiscal = ('AL, PB, PE e RN')
    }
    else if (cpfInformado[8] == 5) {
        regiaoFiscal = ('BA e SE')
    }
    else if (cpfInformado[8] == 6) {
        regiaoFiscal = ('MG')
    }
    else if (cpfInformado[8] == 7) {
        regiaoFiscal = ('ES e RJ')
    }
    else if (cpfInformado[8] == 8) {
        regiaoFiscal = ('SP')
    }
    else if (cpfInformado[8] == 9) {
        regiaoFiscal = ('PR e SC')
    }
    else if (cpfInformado[8] == 0) {
        regiaoFiscal = ('RS')
    }
    //----------------------------
    return regiaoFiscal
}



function tratadorDeCliqueExercicio8() {
    let textCPF = document.getElementById("textCPF")
	let textRegiao = document.getElementById("regiaoFiscal")

    const regiaoFiscal = obterRegiaoFiscalAtravesDoCPFInformado(textCPF.value);
    textRegiao.textContent = "Região fiscal: "+regiaoFiscal
}
