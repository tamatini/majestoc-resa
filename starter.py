from majestoc_resa.services import api
from majestoc_resa import app
# the API-versioned way
# app.register_blueprint(blueprint, url_prefix='/api/1')
# the regular way

api.init_app(app)
app.run(debug=True)