#!/usr/bin/env python3

# Copyright (c) 2026 asaeppel4231
# SPDX-License-Identifier: MIT

import pytest
import sys
import platform
import os

from src import utils

# AI generated test

def test_self_calling_protection(monkeypatch, tmp_path):
    dummy_file = tmp_path / "builder.py"
    dummy_file.touch()

    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        monkeypatch.setattr(sys, "argv", [str(dummy_file)])

        assert utils.cmd_tries_to_call_build_script("builder.py") == True
        assert utils.cmd_tries_to_call_build_script(str(dummy_file)) == True
        assert utils.cmd_tries_to_call_build_script("") == False
    finally:
        os.chdir(old_cwd)

def test_command_exists():
    assert utils.command_exists("") == False
    assert utils.command_exists("not_possible_to_exist") == False

    print(platform.system())
    
    if platform.system() in ["Linux", "Darwin"]:
        assert utils.command_exists("ls") == True
    elif platform.system() == "Windows":
        assert utils.command_exists("dir") == True

# AI generated test, modified by me

def test_logs_dir_preparation(tmp_path):
    utils.LOGS_DIR = str(tmp_path / "temp_logs")

    # Skip query
    utils.prepare_logs_dir(1)
    assert os.path.exists(utils.LOGS_DIR) is True
    
    dummy_log = os.path.join(utils.LOGS_DIR, "old_build.log")
    with open(dummy_log, "w") as f:
        f.write("")

    dummy_log_2 = os.path.join(utils.LOGS_DIR, "log.log")
    with open(dummy_log_2, "w") as f:
        f.write("LOG: Hello World")
        
    utils.prepare_logs_dir(1)
    
    assert os.path.exists(utils.LOGS_DIR) == True

    assert os.path.exists(dummy_log) == False
    assert os.path.exists(dummy_log_2) == False
    
