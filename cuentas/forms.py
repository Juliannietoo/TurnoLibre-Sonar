from django.contrib.auth.forms import AuthenticationForm


class FormularioEntrada(AuthenticationForm):
    """Inicio de sesión con un mensaje genérico que no revela qué dato falla (NFR-005)."""

    error_messages = {
        "invalid_login": "Usuario o contraseña incorrectos.",
        "inactive": "Usuario o contraseña incorrectos.",
    }

    def clean_username(self):
        # Se admiten mayúsculas y espacios exteriores; la contraseña no se altera.
        return self.cleaned_data["username"].strip().lower()
