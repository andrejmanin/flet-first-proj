import flet as ft

def main(page: ft.Page):
    page.title = "Flet Py App"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#F5EEE6"

    row_user = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls= [
            ft.IconButton(
                icon=ft.icons.MENU,
                icon_color="#3D3B40",
                icon_size=20,
            ),

            ft.IconButton(
                icon=ft.icons.ACCOUNT_CIRCLE,
                icon_color="#3D3B40",
                icon_size=20,
            ),
            ft.Text(
                text_align=ft.TextAlign.LEFT,
                value="Andrew Manin",
                weight=ft.FontWeight.W_500,
                color="#294B29"

            )
        ]
    )

    row_info = ft.Row(
        [
            ft.Container(
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    value="Account age: 3 dayse\nUsername: Andrew\nLast name: Manin\nUser age: 15\nCountry: "
                          "Ukraine\nCity: Vinnitsia",
                    color="#789461",
                    size=20,
                    font_family="Comic Sans MS",
                ),
                bgcolor="#DBE7C9",
                border_radius=25,
                height=200,
                width=250,
            ),
            ft.Container(
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    value="STATISTIC",
                    color="#789461",
                    size=40,
                    font_family="Comic Sans MS",
                ),
                bgcolor="#DBE7C9",
                border_radius=25,
                height=200,
                width=250,
            )
        ]
    )


    main_column = ft.Column(
        alignment=ft.MainAxisAlignment.START,
        controls= [
            row_user,
            row_info
        ]

    )

    page.add(
        main_column,
    )

    page.update()

ft.app(target=main)