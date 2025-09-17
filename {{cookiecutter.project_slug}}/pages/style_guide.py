import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# 1. Register the page
dash.register_page(__name__, name="Style Guide", path="/style-guide")

# 2. Helper function to create section headers
def create_section_header(title):
    return dmc.Stack([
        dmc.Title(title, order=2),
        dmc.Divider(mt="sm", mb="lg"),
    ])

# 3. Define the page layout
layout = dmc.Stack([
    dmc.Title("Style Guide", order=1),
    dmc.Text("This page showcases the core components available in the Bodewell theme."),
    
    # --- Buttons Section ---
    create_section_header("Buttons"),
    dmc.Group([
        dmc.Button("Primary Button"),
        dmc.Button("Secondary Button", variant="default"),
        dmc.Button("Subtle Button", variant="subtle"),
        dmc.Button("Destructive", color="red"),
    ]),
    
    # --- Inputs Section ---
    create_section_header("Form Inputs"),
    dmc.Group([
        dmc.TextInput(label="Text Input", placeholder="Enter text..."),
        dmc.NumberInput(label="Number Input", value=100),
        dmc.PasswordInput(label="Password Input", placeholder="Enter password..."),
    ]),

    # --- Feedback Section ---
    create_section_header("Feedback Components"),
    dmc.Stack([
        dmc.Alert(
            "This is an important message.",
            title="Informational Alert",
            color="blue",
            withCloseButton=True,
            icon=DashIconify(icon="ic:round-info")
        ),
        dmc.Alert(
            "Something went wrong!",
            title="Error Alert",
            color="red",
            withCloseButton=True,
            icon=DashIconify(icon="ic:round-error")
        ),
    ]),
])