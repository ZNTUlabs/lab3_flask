import os
import tempfile

import pytest

@pytest.fixture
def switch_on_all(client):
	rv = client.get('/api/pin/on/all')
	data = json.loads(rv.data)
	assert assert_equal(data['data'], "All pins was turn ON")