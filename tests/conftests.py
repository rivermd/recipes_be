import pytest
from recipes_api.models import Recipe
from recipes_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Test Recipe', 'Test Ingredients', 'Test Steps', 0, False)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()
    

