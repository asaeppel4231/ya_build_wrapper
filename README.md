# ya_build_wrapper

## About

*ya_build_wrapper* is a wrapper around CMake and other build tasks. It is fully written in Python.

## Dependencies

This project depends on the rich and the pyyaml library.
Please make sure the're installed before running this program!

## Nerd facts

- *Lines of Code*: 224
- *Complexity*: 55
- *Lines of Code per Complexity*: 4,072727273

## Native executable

I provide also native executables for windows, linux and macOS.
You can download them at the Release page of this repository in Github.

## Example

Run this program with --cfg-input 0 and --generate-example-config to get an example build task configuration.

## Using

Once you wrote your build task configuration, you can start ya_build_wrapper with --cfg-input PATH-TO-YOUR-BUILD-TASK-CONFIGURATION and it runs.
Also, if you are in CI mode and one of the steps failed, ya_build_wrapper writes a FAIL-file. It contains plaintext informations on which command the task executed and which return typ it had.
If that FAIL-file exists, you can start this program with --fail-if-build-failed, so your workflow stops running if one step failed.

