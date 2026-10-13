#!/usr/bin/env python3

# Copyright (c) 2026 asaeppel4231
# SPDX-License-Identifier: MIT

import pytest
from src import build_steps

def test_build_steps_yaml_parsing(tmp_path):
    test_file = tmp_path / "config_parser_test.yaml"

    test_file.write_text("build:\n\
  steps:\n\
    - description: \"Test 1\"\n\
      cmd: \"echo\"\n\
      log_file_name_base: \"echo_test\"\n\
      rwd: \".\"\n\
      environment: \"both\"\n\
      \n\
    - description: \"Test 2\"\n\
      cmd: \"pwd\"\n\
      log_file_name_base: \"pwd_test\"\n\
      rwd: \".\"\n\
      environment: \"local\"\n\
      \n\
    - description: \"Test 3\"\n\
      cmd: \"ls\"\n\
      log_file_name_base: \"ls_test\"\n\
      rwd: \".\"\n\
      environment: \"ci\"\n\
    ")

    ci = build_steps.get_build_steps(test_file, 1)
    local = build_steps.get_build_steps(test_file, 0)

    assert ("Test 1", "echo", "echo_test", ".") in ci
    assert ("Test 3", "ls", "ls_test", ".") in ci
    assert ("Test 2", "pwd", "pwd_test", ".") not in ci

    assert ("Test 1", "echo", "echo_test", ".") in local
    assert ("Test 2", "pwd", "pwd_test", ".") in local
    assert ("Test 3", "ls", "ls_test", ".") not in local
