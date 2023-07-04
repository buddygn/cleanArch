import pytest
from .connection import DbConnectionHander


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DbConnectionHander()
    engine = db_connection_handle.get_engine()

    assert engine is not None
