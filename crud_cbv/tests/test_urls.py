from crud_cbv.urls import urlpatterns


def test_urls_len():
    assert 6 == len(urlpatterns)