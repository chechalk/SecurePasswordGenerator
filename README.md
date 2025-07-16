# 🔐 Secure Password Generator (KeyGen)

A command-line Python 3.13 tool to generate secure passwords with custom options. It supports clipboard copying, entropy estimation, strength classification, and optional password history saving.

---

## Features

- Generate strong random passwords using `secrets` and `random`.
- Customize:
  - Length
  - Inclusion of uppercase, lowercase, digits, symbols
  - Exclude ambiguous characters (`O`, `0`, `I`, `l`, `1`)
- Entropy calculation for security insight.
- Password strength classification (Weak, Moderate, Strong).
- Optional clipboard copy (with `pyperclip`).
- Save password history to a file.

---

## 🔧 Requirements

- Python 3.13+
- Optional:
  - `pyperclip`
