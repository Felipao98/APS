from Visao import loginCadastro

def main():
    # Cria instâncias dos componentes Model, View e Controller
    model = model()
    visao = loginCadastro()
    control = control(model, visao)

    # Conecta o Controller à View
    visao.conectar_controle(control)

    # Inicia o aplicativo
    visao.iniciar_aplicativo()

if __name__ == "__main__":
    main()
