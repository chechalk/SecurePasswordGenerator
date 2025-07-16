# 🔐 Secure Password Generator (KeyGen)

A command-line Python 3.13 tool to generate secure passwords with custom options. It supports clipboard copying, entropy estimation, strength classification, and optional password history saving.

## Features

- Generate strong random passwords using `secrets` and `random`
- Customize length, symbols, digits, uppercase/lowercase inclusion
- Exclude ambiguous characters like `O`, `0`, `I`, `l`
- Classify password strength (Weak/Moderate/Strong)
- Clipboard copy support (with `pyperclip`)
- Save password history to file

## 🔧 Requirements

```txt
pyperclip>=1.8.2
```

Install with:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python keygen.py
```

Follow prompts for all options. You can generate multiple passwords, and optionally save them or copy to clipboard.

## 🧾 License

MIT - See `LICENSE`
