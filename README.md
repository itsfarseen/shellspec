# ShellSpec

Testing framework for shell commands with declarative syntax.

## Features

- Test shell commands with expected success/failure
- Interactive command testing with pexpect
- Variable storage and manipulation
- File operations and content verification
- Reusable test snippets
- Isolated test environments

## Installation

Requirements: Python 3.7+, pexpect library

```bash
pip install pexpect
chmod +x shellspec.py
```

## Usage

```bash
# Run all tests
./shellspec.py mytests.spec

# Run specific test by number or name
./shellspec.py mytests.spec --test 1
./shellspec.py mytests.spec --test "file operations"

# Show command output
./shellspec.py mytests.spec --verbose
```

## Writing Tests

For complete syntax documentation, see [SYNTAX.md](SYNTAX.md).

For a quick reference, see the [cheatsheet](shellspec-cheatsheet.txt).

### Basic Test Structure

```
> Test case name
$. command args           # Run command expecting success
?. stdout "expected"      # Assert stdout contains "expected"
```

## Demos and Examples

**Calculator**

See the [calculator_spec.txt](examples/calculator_spec.txt) for the test implementation.

![Calculator Demo](screencasts/calculator.gif)


**File Processor**

See the [file_processor_spec.txt](examples/file_processor_spec.txt) for the test implementation.

![File Processor Demo](screencasts/file_processor.gif)

**Interactive Calculator**

See the [interactive_calculator_spec.txt](examples/interactive_calculator_spec.txt) for the test implementation.

![Interactive Calculator Demo](screencasts/interactive_calculator.gif)


## Configuration

### Command Aliases

ShellSpec allows you to define aliases for commands to simplify testing or provide custom paths. Edit the `COMMAND_ALIASES` dictionary in `shellspec.py`:

```python
COMMAND_ALIASES = {
    "myapp": "../path/to/myapp",
    "python3": "/usr/bin/python3",
}
```

Commands not found in the aliases dictionary will be executed directly as system commands.

### Timeout Settings

The default timeout for shell commands is 30 seconds. Modify `SHELL_TIMEOUT` in `shellspec.py` to change this.

## Documentation

- **[SYNTAX.md](SYNTAX.md)** - Complete syntax reference with examples
- **[shellspec-cheatsheet.txt](shellspec-cheatsheet.txt)** - Quick reference for all commands


## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Projects

ShellSpec was originally developed as part of the age-store project for testing command-line encryption tools. It has been extracted into its own project for broader use.
