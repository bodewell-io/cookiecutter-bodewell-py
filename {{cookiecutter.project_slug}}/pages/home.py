import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# 1. Register the page
dash.register_page(__name__, path="/", name="Dashboard")

# 2. Helper function to create dashboard stat cards
def create_stat_card(title, value, icon, color):
    """Creates a themed card for displaying a single statistic."""
    return dmc.Card(
        withBorder=True,
        shadow="sm",
        radius="md",
        children=[
            dmc.Group([
                dmc.Text(title, size="sm", c="gray"),
                dmc.ThemeIcon(
                    DashIconify(icon=icon),
                    size="lg",
                    variant="light",
                    color=color,
                )
            ], justify="space-between"),
            dmc.Text(value, size="xl", fw=700, mt="sm"),
        ]
    )

# 3. Define the page layout
layout = dmc.Stack([
    dmc.Title("Dashboard", order=1),
    dmc.Text("Welcome to the Bodewell App Starter for Python!"),
    
    # --- Stat Cards Section ---
    dmc.SimpleGrid(
        cols={"base": 1, "sm": 2, "lg": 4},
        mt="lg",
        children=[
            create_stat_card("Revenue", "$12,345", "ic:round-attach-money", "blue"),
            create_stat_card("New Users", "678", "ic:round-person-add", "green"),
            create_stat_card("Open Tickets", "23", "ic:round-error-outline", "orange"),
            create_stat_card("Conversion Rate", "12.4%", "ic:round-trending-up", "teal"),
        ]
    ),
    
    # --- Progress Section (Corrected) ---
    dmc.Card(
        withBorder=True,
        shadow="sm",
        radius="md",
        mt="xl",
        children=[
            # We now use a Group to place the title and label on the same line
            dmc.Group([
                dmc.Text("Quarterly Goal Progress", fw=500),
                dmc.Text("75%", c="blue", fw=500)
            ], justify="space-between"),
            # The Progress component no longer has the 'label' argument
            dmc.Progress(value=75, color="blue", size="lg", mt="sm"),
        ]
    ),

    # --- Alert Section ---
    dmc.Alert(
        "This is an informational alert to show system status or provide helpful tips.",
        title="System Status",
        color="blue",
        withCloseButton=True,
        icon=DashIconify(icon="ic:round-info"),
        mt="xl"
    ),
])