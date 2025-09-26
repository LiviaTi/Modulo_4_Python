
def format_cents(num: int) -> str:
    """ Função que transforma os inteiros em string"""
    if num >= 0:
        prefix = "[+] R$ "
    else:
        prefix = "[-] R$ "

    reais = abs(num) / 100  

    valor_formatado = f"{reais:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

    return prefix + valor_formatado
