from web.app import create_app

app = create_app("testing")
app.testing = True
testing_app = app.test_client()
