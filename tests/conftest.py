import os

import pytest


@pytest.fixture(autouse=True)
def generate_config(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text("urls:\n  root: https://shoup.io\n  foo: https://baz\n")

    os.environ["CRISCO_CONFIG_PATH"] = str(config_path)
