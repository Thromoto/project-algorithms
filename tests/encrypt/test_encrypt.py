import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('xablau', 'str')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(9, 8)
    assert encrypt_message("xablau", 9) == "ualbax"
    assert encrypt_message("xablau", -1) == "ualbax"
    assert encrypt_message("xablau", 3) == "bax_ual"
    assert encrypt_message("xablau", 4) == "ua_lbax"
