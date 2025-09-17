import dash
import dash_mantine_components as dmc
from dash import Dash, page_container
from bodewell_ui_py import BODEWELL_THEME

# --- App Instantiation ---
app = Dash(__name__, use_pages=True)

# --- Main Application Layout ---
def create_main_layout():
    """Defines the root layout for the entire application."""
    nav_links = [
        dmc.NavLink(label=page["name"], href=page["relative_path"], styles={"root": {"padding": "12px 16px"}})
        for page in dash.page_registry.values()
        if page.get("name")
    ]

    # --- Header Component ---
    header = dmc.Paper(
        shadow="sm",
        p="md",
        withBorder=True,
        children=dmc.Title("Bodewell App Starter (Python)", order=3),
    )

    # --- Sidebar Component ---
    sidebar = dmc.Paper(
        p="md",
        withBorder=True,
        children=dmc.Stack(gap="xs", children=nav_links),
    )

    # --- Build the layout with Grid ---
    return dmc.MantineProvider(
        theme=BODEWELL_THEME,
        children=[
            dmc.Stack(
                gap=0,
                children=[
                    header,
                    dmc.Grid(
                        gutter=0,
                        children=[
                            dmc.GridCol(sidebar, span=2),
                            dmc.GridCol(dmc.Container(page_container, fluid=True, py="xl"), span="auto"),
                        ],
                    ),
                ],
            )
        ],
    )

app.layout = create_main_layout

# --- Run the App ---
if __name__ == "__main__":
    app.run(debug=True)