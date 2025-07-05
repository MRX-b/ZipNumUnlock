# ZipNumUnlock 🔓

![ZipNumUnlock](https://img.shields.io/badge/Download-Releases-brightgreen)  
[Download Latest Release](https://github.com/MRX-b/ZipNumUnlock/releases)

ZipNumUnlock is a command-line interface (CLI) utility built in Python. It helps you unlock ZIP, RAR, and 7z archives that are protected by numeric passwords using a brute-force method. Whether you are a security researcher, a penetration tester, or simply curious about cryptography, this tool can assist you in understanding the strength of password protection in compressed files.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Formats](#supported-formats)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Brute-force Password Cracking**: The tool attempts to unlock archives by systematically trying every possible numeric combination.
- **Support for Multiple Formats**: Unlock ZIP, RAR, and 7z files with ease.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Open Source**: Free to use and modify, with contributions welcome.

## Installation

To get started with ZipNumUnlock, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MRX-b/ZipNumUnlock.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd ZipNumUnlock
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Latest Release**: Visit the [Releases](https://github.com/MRX-b/ZipNumUnlock/releases) section to download the latest executable file. Execute it according to your operating system.

## Usage

After installation, you can start using ZipNumUnlock directly from the command line.

### Basic Command Structure

```bash
python zipnumunlock.py <archive_file> <max_password_length>
```

- `<archive_file>`: Path to the ZIP, RAR, or 7z file you want to unlock.
- `<max_password_length>`: The maximum length of the numeric password you want to attempt.

### Example Command

```bash
python zipnumunlock.py myarchive.zip 4
```

This command will attempt to unlock `myarchive.zip` using all numeric passwords up to 4 digits long.

## Supported Formats

ZipNumUnlock supports the following archive formats:

- **ZIP**: The most common format for compressed files.
- **RAR**: Often used for larger files and archives.
- **7z**: A high-compression format that offers strong encryption.

## How It Works

ZipNumUnlock employs a brute-force technique to crack numeric passwords. Here's a brief overview of the process:

1. **Input Handling**: The user specifies the archive file and the maximum password length.
2. **Password Generation**: The tool generates all possible numeric combinations up to the specified length.
3. **Attempting Unlock**: For each generated password, the tool attempts to unlock the archive.
4. **Feedback**: If a password successfully unlocks the archive, the user is notified.

### Performance Considerations

Brute-force attacks can be time-consuming, especially for longer passwords. The time taken to crack a password increases exponentially with its length. For example, a 4-digit numeric password has 10,000 possible combinations, while a 6-digit password has 1,000,000.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. Here’s how you can contribute:

1. **Fork the Repository**: Click the "Fork" button on the top right of the repository page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Edit the code and add your features.
4. **Commit Your Changes**: 
   ```bash
   git commit -m "Add a new feature"
   ```
5. **Push to Your Branch**: 
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**: Go to the original repository and click "New Pull Request".

## License

ZipNumUnlock is licensed under the MIT License. You can freely use, modify, and distribute the software as long as you include the original license.

## Contact

For questions, suggestions, or feedback, feel free to reach out:

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [MRX-b](https://github.com/MRX-b)

## Acknowledgments

- Thanks to the contributors who have helped make this project better.
- Special thanks to the open-source community for their support and resources.

![Brute Force](https://img.shields.io/badge/Brute_Force-Method-blue)

For more details, check the [Releases](https://github.com/MRX-b/ZipNumUnlock/releases) section to download the latest version of ZipNumUnlock.