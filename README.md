# ya_build_wrapper

## About

*ya_build_wrapper* is a wrapper around **CMake and other build tasks**. It is fully written in ***Python***.

## License

See the [LICENSE.md](LICENSE.md) file of this repository.

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file of ya_build_wrapper.

## Roadmap

See the [ROADMAP.md](ROADMAP.md) file of this repository.

## Dependencies

This project depends on the **rich** and the **pyyaml** library.
Please make sure they're *installed* before running this program!

## Nerd facts

"Real" source code:

- *Lines of Code*: 334
- *Complexity*: 84
- *Lines of Code per Complexity*: 3,976190476

Test code:

- *Lines of Code*: 100
- *Complexity*: 12
- *Lines of Code pder Complexity*: 8,333333333

Misc:

- *Current version*: 0.2

## Native executable

I provide also native executables for **windows**, **linux** and **macOS**.
You can download them at the *release page* of this repository in **Github**.

## Example

Run this program with **"--generate-example-config"** to get an **example** *build task configuration*.

## Usage

Once you wrote your build task configuration, you can start *ya_build_wrapper* with *"--cfg-input PATH-TO-YOUR-BUILD-TASK-CONFIGURATION"* and it runs.


Also, if you are **in CI mode** and one of the steps failed, *ya_build_wrapper* writes a **"FAIL-file"**.
It **contains plaintext informations** on *which command the task executed* and *which return type it had*.

If that **"FAIL-file"** exists, you can start this program with *"--fail-if-build-failed"*, so your **workflow stops running if one step failed**.

