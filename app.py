from presentation.middlewares import initialize_middlewares
from presentation.routes.content import initialize_routes
from infrastructure.database import initialize_database
from flask import Flask

app = Flask(__name__)

initialize_middlewares(app)
initialize_routes(app)
initialize_database()

if __name__ == "__main__":
    app.run(debug=True)
