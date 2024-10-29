# 🧹 ProcX

```text
 ____                     __  __
|  _ \  _ __   ___    ___ \ \/ /
| |_) || '__| / _ \  / __| \  /
|  __/ | |   | (_) || (__  /  \
|_|    |_|    \___/  \___|/_/\_\

```

🧹 ProcX is an interactive command-line tool for quickly searching and terminating processes, offering a streamlined alternative to traditional `kill`.

## ✨ Features

TBD

## 🚀 Installation

To install **procx**, simply clone the repository and follow the instructions below:

```bash
git clone https://github.com/trinhminhtriet/procx.git
cd procx
cargo build --release
./target/release/procx --version
```

Running the below command will globally install the `procx` binary.

```bash
cargo install procx
```

Optionally, you can add `~/.cargo/bin` to your PATH if it's not already there

```bash
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 💡 Usage

Run **procx** with the following command to kill the process:

```sh
./procx [options]

```

## 🗑️ Uninstallation

Running the below command will globally uninstall the `procx` binary.

```bash
cargo uninstall procx
```

Remove the project repo

```bash
rm -rf /path/to/git/clone/procx
```

## 🤝 How to contribute

We welcome contributions!

- Fork this repository;
- Create a branch with your feature: `git checkout -b my-feature`;
- Commit your changes: `git commit -m "feat: my new feature"`;
- Push to your branch: `git push origin my-feature`.

Once your pull request has been merged, you can delete your branch.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
