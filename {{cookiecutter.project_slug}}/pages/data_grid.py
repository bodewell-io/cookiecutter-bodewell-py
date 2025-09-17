import dash
import dash_mantine_components as dmc
import dash_ag_grid as dag

# 1. Register the page
dash.register_page(__name__, name="Data Grid", path="/data-grid")

# 2. Define sample data and column definitions
rowData = [
    {"name": "Alice", "age": 28, "role": "Engineer"},
    {"name": "Bob", "age": 34, "role": "Designer"},
    {"name": "Charlie", "age": 45, "role": "Manager"},
    {"name": "Diana", "age": 22, "role": "Intern"},
]

columnDefs = [
    {"field": "name", "headerName": "Name", "checkboxSelection": True},
    {"field": "age", "headerName": "Age"},
    {"field": "role", "headerName": "Role"},
]

# 3. Define the page layout
layout = dmc.Stack([
    dmc.Title("Data Grid", order=1),
    dmc.Text("This is an example of a themed AG Grid component."),
    dmc.Space(h="lg"),
    # 4. Add the AG Grid component
    dag.AgGrid(
        rowData=rowData,
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        defaultColDef={"sortable": True, "filter": True},
        # This className is the key to applying our custom theme
        className="ag-theme-alpine",
        style={"height": "400px"},
    ),
])