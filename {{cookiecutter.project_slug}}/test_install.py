print("--- Starting Bodewell Installation Test ---")

try:
    import dash
    print("✅ Successfully imported 'dash'")
except ImportError:
    print("❌ FAILED to import 'dash'. Please run: python3 -m pip install dash")
    exit()

try:
    import dash_mantine_components as dmc
    print("✅ Successfully imported 'dash_mantine_components'")
except ImportError:
    print("❌ FAILED to import 'dash_mantine_components'. Please run: python3 -m pip install dash-mantine-components")
    exit()

try:
    import bodewell_ui_py
    print("✅ Successfully imported 'bodewell_ui_py'")
except ImportError:
    print("❌ FAILED to import 'bodewell_ui_py'. Make sure you've run: python3 -m pip install -e ../bodewell-ui-py")
    exit()

print("\n--- ✅ All components appear to be installed correctly! ---")