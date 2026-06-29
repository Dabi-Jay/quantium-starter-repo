from dash.testing.application_runners import import_app

app = import_app("app")


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header is not None
    assert "Soul Foods" in header.text


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio_buttons = dash_duo.find_element("#region-filter")

    assert radio_buttons is not None