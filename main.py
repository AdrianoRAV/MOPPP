import flet as ft

def main(page: ft.Page):
    # Definindo o título e cores
    page.title = "Correios Checklist"
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE,
        text_theme=ft.TextTheme(
            headline_large=ft.TextStyle(color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
            body_large=ft.TextStyle(color=ft.colors.BLUE),
            label_large=ft.TextStyle(color=ft.colors.WHITE),
        ),
    )
    page.bgcolor = ft.colors.WHITE

    # Variáveis de estado
    observation = ft.Ref[ft.TextField]()

    # Lista de células e perguntas
    cells = ['PRÉ ABERTURA - ABERTURA - C1', 'TRIAGEM MANUAL MENSAGENS - C2', 'TRIAGEM AUTOMATIZADA MENSAGENS - C3', 'CONSOLIDAÇÃO C4', 'ERM OE - C5', 'INDUÇÃO PO SUL - C6', 'INDUÇÃO PO NORTE - C7', 'ALA LESTE PO - C8', 'ALA OESTE PO - C9', 'TRATAMENTO MANUAL SEDEX -  RECONDICIONAMENTO - C10', 'INDUÇÃO GO - ABERTURA DE MALAS - C11', 'ALA D - C12', 'ALA B_C - C13']
    # Lista de perguntas
    perguntas_celula = [
        "A carga é movimentada conforme previsto?",
        'O descarregamento e carregamento dos veículos é realizado conforme previsto?',
        'A montagem dos páletes aeronáuticos é realizada de acordo com o padrão estabelecido?',
        'A carga é disponibilizada para carregamento em horário compatível com o previsto na Ficha Técnica para a saída da linha?',
        'São realizadas as verificações previstas para ocorrer no momento da apresentação/parada do veículo na unidade? Lançamento RDVO?',
        'Os equipamentos e unitizadores estão posicionados nas estações de trabalho e organizados conforme o leiaute previamente definido pela unidade?',
        'A compactação da carga é feita de forma a aproveitar a capacidade máxima do unitizador?' ,
        'Quando ocorre o bloqueio da Estação de Retrabalho, são tomadas, imediatamente, ações para  desbloqueio?',
        'Os objetos com danos na embalagem são disponibilizados para a área de recondicionamento?',
        'O recondicionamento dos objetos é realizado cumprindo-se os procedimentos previstos?',
        'Os unitizadores a serem expedidos são devidamente rotulados?',
        'É afixado rótulo de identificação nos unitizadores (todos), colocada tampa (CDL/Caixeta), passada a fita de arquear (CDL) e posto o lacre (CDL, Caixetas e Malas), conforme previsto?',
        'A carga localizada na área de armazenagem,  para posterior tratamento, está devidamente identificada?',
        'Os amarrados cujo conteúdo seja destinado à triagem em manipuladores/máquinas são desfeitos na estação de abertura?',
        'No momento da abertura, são verificados os rótulos das caixetas e malas a fim de evitar o tratamento indevido da carga? A mesa é utilizada para abertura?',
        'Os envelopes que estiverem misturados com os pacotes são disponibilizados para a área de tratamento manual?',
        'Os objetos de formato normal são depositados, observando-se o faceamento e o encabeçamento correto, virando-se o unitizador sobre a bandeja de alimentação?',
        'A máquina é desabastecida na operação após fechamento do plano?',
        'A triagem é realizada de acordo com o padrão estabelecido?',
        'São confeccionados amarrados dos objetos para as direções que serão expedidas em malas? Estes são confeccionados de forma a não se desfazerem durante o transporte?',
        'A carga destinada às unidades de distribuição é devidamente compactada observando o faceamento e encabeceamento?',
        'Os objetos são triados com base na informação fornecida pelo STES?',
        'Há desabastecimento contínuo do manipulador?',
        'Há o controle diário da produtividade individual de todos os empregados envolvidos na triagem manual durante toda a jornada de trabalho?',
        'A empilhadeira é usada conforme previsto?',
        'A paleteira pantográfica está sendo utilizada?',
        'O suporte para caixetas é usado corretamente?',
        'Todos os rótulos são retirados após o  esvaziamento dos unitizadores?',
        'Os unitizadores e objetos são manuseados corretamente durante toda a operação?',
        'As caixetas, malas, mangas e tampas, estão dispostas em equipamentos específicos de forma a evitar o contato direto com o piso?',
        'A unidade envia os unitizadores vazios (CDL, caixetas e malas de nylon) para a centralizadora nacional?',
        'É efetuada a postagem dos objetos coletados/recebidos, conforme definido? (PREPOSTO)',
        ]
    perguntas = {
        'PRÉ ABERTURA - ABERTURA - C1': [perguntas_celula[0], perguntas_celula[1]],  # Referencia as perguntas 1 e 2
        'TRIAGEM MANUAL MENSAGENS - C2': [perguntas_celula[0], perguntas_celula[1], perguntas_celula[2]],  # Referencia as perguntas 1, 2 e 3
        'TRIAGEM AUTOMATIZADA MENSAGENS - C3': [perguntas_celula[1], perguntas_celula[3]],  # Referencia as perguntas 2 e 4
        'CONSOLIDAÇÃO C4': perguntas_celula,
        'ERM OE - C5': perguntas_celula,
        'INDUÇÃO PO SUL - C6': [perguntas_celula[0], perguntas_celula[1], perguntas_celula[2], perguntas_celula[3]],
        'INDUÇÃO PO NORTE - C7': perguntas_celula,
        'ALA LESTE PO - C8': perguntas_celula,
        'ALA OESTE PO - C9': perguntas_celula,  # Referencia todas as perguntas
        'TRATAMENTO MANUAL SEDEX -  RECONDICIONAMENTO - C10': perguntas_celula,  # Referencia todas as perguntas
        'INDUÇÃO GO - ABERTURA DE MALAS - C11': perguntas_celula,  # Referencia todas as perguntas
        'ALA D - C12': perguntas_celula,  # Referencia todas as perguntas
        'ALA B_C - C13': perguntas_celula,  # Referencia todas as perguntas
        'ALA A - C14': perguntas_celula,  # Referencia todas as perguntas
        'SALA DE CONTROLE  - C15': perguntas_celula,  # Referencia todas as perguntas
        'ENTREPOSTO NORTE - CÉLULA 17': perguntas_celula,  # Referencia todas as perguntas
        'GCCAP - C18': perguntas_celula,  # Referencia todas as perguntas
    }

    # Função para enviar o formulário
    def submit_form(e):
        print(f'Célula selecionada: {selected_cell.value}')
        print(f'Observações: {observation.current.value}')

    # Função para tirar foto
    def take_photo(e):
        print("Tirar foto - (Flet não suporta captura de imagem diretamente)")

    # Função para atualizar as abas com as perguntas filtradas
    def update_tabs(e):
        selected = selected_cell.value
        new_tabs = []  # Nova lista de abas com base na célula selecionada

        for pergunta in perguntas[selected]:
            new_tabs.append(
                ft.Tab(
                    text='pergunta',
                    content=generate_tab_content(pergunta)
                )
            )

        # Substitui as abas atuais pelas novas
        tabs.tabs = new_tabs
        page.update()

    # Função que gera o conteúdo de cada aba
    def generate_tab_content(pergunta_texto):
        return ft.Column(
            controls=[
                ft.Text(
                    pergunta_texto,
                    size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER
                ),
                ft.ElevatedButton("SIM", on_click=submit_form,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE), width=360),
                ft.ElevatedButton("NÃO", on_click=submit_form,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE), width=360),
                ft.ElevatedButton("NÃO SE APLICA", on_click=submit_form,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE), width=360),
                ft.ElevatedButton("Tirar Foto", on_click=take_photo,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE), width=360),
                ft.TextField(ref=observation, label="Observações", multiline=True, width=360, height=100)
            ],
            spacing=20,
            expand=True,
            alignment=ft.MainAxisAlignment.START,
        )

    # Dropdown para selecionar a célula
    selected_cell = ft.Dropdown(
        label="Selecione a célula",
        options=[ft.dropdown.Option(cell) for cell in cells],
        value="PRÉ ABERTURA - ABERTURA - C1",  # Define a célula 1 como padrão
        on_change=update_tabs
    )

    # Controles iniciais e AppBar
    tabs = ft.Tabs(expand=True)  # Criação das tabs (aberto inicialmente)
    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text(value="CORREIOS MOPPP", size=24, weight=ft.FontWeight.BOLD, color="black"),
        center_title=False,
        bgcolor=ft.colors.BLUE,
        actions=[ft.PopupMenuButton(items=[ft.PopupMenuItem(text="Item 1")])]
    )

    # Adicionar Dropdown e Tabs na página
    page.add(selected_cell, tabs)

    # Carregar perguntas da célula 1 por padrão
    update_tabs(None)

ft.app(target=main)
