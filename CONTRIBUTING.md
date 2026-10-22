# CONTRIBUTING.md

Thank you for your interest in contributing to ya_build_wrapper. We welcome improvements and fixes — please read these guidelines before opening issues or pull requests. This file explains which contributions will be accepted for merging and how to prepare them.

## What we accept (will consider for merge)
The repository maintainer (asaeppel4231) will accept and merge contributions in the following categories:

1. New languages (translations)
   - Add translations for error and output strings.
   - Follow the existing translation file format and structure (use the same keys and placeholders as the existing locale—typically copy the `en` source and translate).
   - Add tests or examples that demonstrate the translated output where applicable.

2. A better self-calling detection function
   - Improvements or replacements for the function that detects self-invocation are welcome.
   - Provide clear tests that show the current edge cases being fixed.
   - Include rationale and performance notes if the change affects runtime behavior.

3. Rewrites in another programming language
   - Re-implementations in other languages are accepted.
   - Provide a clear README for the language-specific implementation, including build/run instructions and compatibility notes.
   - Keep feature parity with the original where practical or clearly document differences.

4. Critical runtime errors
   - Bug fixes for runtime failures caused by changes in standard libraries (for example, Python stdlib changes) or other critical breakages.
   - Include minimal reproducible examples, stack traces, environment (OS, language/runtime version), and tests that fail before the fix and pass after.

## What we do NOT merge
- General-purpose PRs outside the four allowed categories above (new features, experiments, stylistic changes, or large refactors) should be done in forks. The maintainer will not merge PRs that fall outside the permitted list.
- If you think something outside those categories is essential, open an issue first to discuss; the maintainer may ask you to maintain it in a separate fork or decide case-by-case.

## Before you open an issue or PR
- Search existing issues and PRs — your idea may already be discussed.
- For non-obvious changes, open an issue first describing the problem and proposed approach. This speeds review and avoids wasted work.
- For translations: mention the locale code (e.g., `fr`, `de`) and the translation format you used.
- For runtime/compatibility bugs: include full stack traces, the exact runtime version (e.g., Python 3.11.8), and steps to reproduce.

## How to submit a PR
1. Fork the repository and create a branch named with the pattern `contrib/<short-desc>` or `fix/<short-desc>`.
2. Keep the PR focused and small; one concern per PR.
3. Include a clear PR description:
   - Summary of the change
   - What problem it fixes or feature it adds
   - Any migration or compatibility notes
   - Testing steps and results
4. If applicable, include tests that demonstrate the fix or new behavior.
5. Run existing test suites and linters locally where possible, and ensure your changes don't break unrelated behavior.
6. Use descriptive commit messages and squash or rebase as appropriate before merge.

## Tests and quality
- Add tests for bug fixes and core functionality changes.
- If you change public behavior or outputs, include tests and examples.
- Maintain code readability and document any non-obvious decisions.

## Translations guidance
- Match keys exactly to the source language file.
- Preserve placeholders (e.g., `{name}`, `%s`) and formatting.
- If plural forms are required, follow the existing pluralization approach used in the repo.
- Add a small example or test that proves the translated strings are used in the right context.

## Self-calling detection improvements
- Provide unit tests that cover common and edge cases (recursive calls, invoked via symlinks, invoked via different entrypoints, etc.).
- Document assumptions and performance characteristics.
- If the change relies on platform-specific behavior, document supported platforms.

## Rewrites / language ports
- Include a README explaining goals and limitations of the port.
- Provide example usage and at least minimal automated tests.
- Prefer idiomatic code for the target language while preserving the core design and behavior.

## Security and sensitive data
- Do not include secrets, private keys, credentials, or sensitive data in issues, PRs, or commits.
- If you discover a security vulnerability, please open a private issue or send an email to the maintainer (use the address in the repo) rather than a public issue.

## Licensing and contributor agreement
- By contributing, you confirm your contributions are compatible with this repository's license.
- If your contribution contains work from others, ensure you have the right to submit it under the project license.

## Code of Conduct
- Treat other contributors with respect. Be constructive and kind.
- The project follows a community code of conduct. Abusive or disrespectful behavior will not be tolerated.

## Review process and timeline
- PRs will be reviewed at the maintainer's discretion. Response times may vary.
- The maintainer may request changes, ask for tests, or decline merges that fall outside the permitted contribution areas.

## If your PR is not merged
- You are welcome to keep the work in a fork and continue maintaining it.
- If you believe a PR should be merged despite being outside the listed categories, open an issue to discuss it first.

Thank you for contributing — your effort and interest are appreciated.

(Generated with assistance from GitHub Copilot Chat Assistant)

