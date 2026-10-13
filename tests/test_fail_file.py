#!/usr/bin/env python3

# Copyright (c) 2026 asaeppel4231
# SPDX-License-Identifier: MIT

from _pytest.deprecated import PARSEFACTORIES_NODEID_DEPRECATED
import pytest

from src import fail_file

def test_read_and_write_fail_file(tmp_path):
    fail_file.FAIL_PATH = str(tmp_path / "FAIL")

    with pytest.raises(SystemExit) as exit_info:
        fail_file.write_fail_file(1, "ls", ".")

        assert exit_info.value.code == 0

    fail_dict: dict = fail_file.read_fail_file()

    assert len(fail_dict) == 3

    assert fail_dict.get("returncode", 0) == 1
    assert fail_dict.get("command", " ") == "ls"
    assert fail_dict.get("workdir", " ") == "."

def test_ci_fail(tmp_path):
    fail_file.FAIL_PATH = str(tmp_path / "FAIL")

    with pytest.raises(SystemExit) as exit_info:
        fail_file.write_fail_file(128, "abc", ".")

        assert exit_info.value.code == 0

    with pytest.raises(SystemExit) as exit_info:
        fail_file.fail_if_ci_build_failed()
        
