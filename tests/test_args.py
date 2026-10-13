#!/usr/bin/env python3

# Copyright (c) 2026 asaeppel4231
# SPDX-License-Identifier: MIT

import pytest

from src import args

# Test is AI-generated
def test_parse_args_unsupported_language(monkeypatch, capsys):
    monkeypatch.setattr("src.args.getlocale", lambda: ("fr_FR", "UTF-8"))

    with pytest.raises(SystemExit) as exit_info:
        args.parse_args()

        assert exit_info.value.code == -1

        captured = capsys.readouterr()
        assert "Unsupported" in captured.out and "language" in captured.out and "detected" in captured.out
