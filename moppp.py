import flet as ft

def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.YELLOW
        )
    )

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        leading_width=40,
        title=ft.Text("CORREIOS MOPPP"),
        center_title=False,
        bgcolor=ft.colors.BLUE,


    )
    cells = ["Célula A", "Célula B", "Célula C", "Célula D" , "Célula F"]

    selected_cell = None
    observation_controller = ft.TextField(label="Observações", multiline=True, width=600, height=500)

    def submit_form(e):
        print(f'Célula selecionada: {selected_cell.value}')
        print(f'Observações: {observation_controller.value}')

    def take_photo(e):
        print("Tirar foto pressionado")
        # Aqui você pode adicionar lógica para capturar a foto

    selected_cell = ft.Dropdown(
        label="Selecione a célula",
        options=[ft.dropdown.Option(cell) for cell in cells],


    )
    texto1 = ft.Text(
            'Os equipamentos e unitizadores estão posicionados nas estações de trabalho e organizados conforme o leiaute previamente definido pela unidade?',
            size=20,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,

            )
    texto2 = ft.Text(
            'Os equipamentos e unitizadores estão posicionados nas estações de trabalho e organizados conforme o leiaute previamente definido pela unidade?',
            size=20,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
            )

    page.add(texto1,
            selected_cell,
            ft.ElevatedButton("SIM", on_click=submit_form, bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE, width='600'),
            ft.ElevatedButton("NÃO", on_click=submit_form, bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE, width='600'),
            ft.ElevatedButton("NÃO SE APLICA", on_click=submit_form, bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE,
                              width='600'),
            ft.ElevatedButton("Tirar Foto", on_click=take_photo, bgcolor=ft.colors.YELLOW, color=ft.colors.BLUE,
                          width='600'),
            observation_controller
    )

ft.app(target=main, host='195.195.0.0', port=8550)








