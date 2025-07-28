import flet as ft
import assets.codec as codec

codec = codec.Codec()


def main(page: ft.Page):
    page.title = "CipherX — RyZeEe"
    page.bgcolor = "#121212"
    page.padding = 40
    page.scroll = "auto"
    page.theme_mode = "dark"
    page.window.resizable = False

    input_text = ft.TextField(
        multiline=True,
        min_lines=5,
        max_lines=10,
        label="Введите текст",
        border_color="#00FFC6",
        border_radius=12,
        text_style=ft.TextStyle(size=18),
        filled=True,
        fill_color="#1E1E1E",
        width=600
    )

    output_text = ft.TextField(
        multiline=True,
        min_lines=5,
        max_lines=10,
        label="Результат",
        read_only=True,
        border_radius=12,
        border_color="#00FFC6",
        text_style=ft.TextStyle(size=18),
        filled=True,
        fill_color="#1E1E1E",
        width=600
    )

    def encrypt_text(e):
        # Примитивная замена (пример шифрования)
        if input_text.value:
            output_text.value = codec.encode(input_text.value)
            page.update()

    def decrypt_text(e):
        if input_text.value:
            output_text.value = codec.decode(input_text.value)
            page.update()

    encrypt_btn = ft.ElevatedButton(
        "🔐 Зашифровать",
        on_click=encrypt_text,
        style=ft.ButtonStyle(
            bgcolor="#00FFC6",
            color="#000000",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12)
        )
    )

    decrypt_btn = ft.ElevatedButton(
        "🔓 Расшифровать",
        on_click=decrypt_text,
        style=ft.ButtonStyle(
            bgcolor="#00FFC6",
            color="#000000",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12)
        )
    )

    title = ft.Text(
        "🧬 CipherX",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#00FFC6"
    )

    page.add(
        ft.Column(
            [
                title,
                input_text,
                ft.Row([encrypt_btn, decrypt_btn], spacing=20),
                output_text
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )
    )

ft.app(target=main)
