# ShellSpec Syntax Reference

This document provides a comprehensive reference for the ShellSpec testing framework syntax.

For a quick reference, see the [cheatsheet](shellspec-cheatsheet.txt).

## Table of Contents

1. [Core Syntax Rules](#core-syntax-rules)
2. [Line Types](#line-types)
3. [Operators](#operators)
4. [Arguments and Values](#arguments-and-values)
5. [Execution Flow](#execution-flow)
6. [Complete Reference by Line Type](#complete-reference-by-line-type)
7. [Examples](#examples)

## Core Syntax Rules

ShellSpec uses a **line-oriented syntax** with a unified structure:

**`<prefix><operator> [target] [arguments...]`**

1. Every line is one statement
2. First character(s) determine the statement type
3. Operators have the same meaning across all line types

## Line Types

ShellSpec has **5 fundamental line types**, each with a unique prefix:

| Prefix | Purpose | Example |
|--------|---------|---------|
| `#` | Comments and documentation | `# This is a comment` |
| `>` | Structure definition (tests, snippets) | `> Test name` |
| `$` | Shell command execution | `$. ls -la` |
| `?` | Assertions and verification | `?. stdout "expected"` |
| `:` | General actions | `:. file "test.txt"` |
| `..` | Content blocks | `.. file content line` |

## Operators

The operators follow a predictable pattern:

| Operator | Meaning | Example |
|----------|---------|---------|
| `.` | **Positive/Success** | `$. command`, `?. stdout "ok"` |
| `!` | **Negative/Failure** | `$! failing-cmd`, `?! stderr "error"` |

- **`.`** = expect success, positive assertion
- **`!`** = expect failure, negative assertion  

## Arguments and Values

All line types follow the same argument patterns:

### Argument Types:
1. **Literals**: `"quoted string"`, `'single quotes'`, `unquoted`
2. **Variables**: `@varname` (always prefixed with `@`)
3. **Targets**: First argument after operator, specifies what to act on

### Quoting Rules:
- **Double quotes**: `"string"` - supports escape sequences (`\"`, `\\`)
- **Single quotes**: `'string'` - supports escape sequences (`\'`, `\\`)  
- **Unquoted**: `word` - no spaces, stops at whitespace

### Variable Rules:
- **Declaration**: Variables are created by storing values (`:. stdout @var`)
- **Usage**: Variables are used by reference (`@var` in any argument position)
- **Scope**: Variables persist within a test case, isolated between tests

## Execution Flow

### Test Structure:
1. **File level**: Contains test cases and snippet definitions
2. **Test case level**: Isolated execution environment  
3. **Command level**: Sequential execution within test case

### Execution Order:
1. Parse all definitions (`>` test cases, `>@` snippets)
2. Execute test cases in file order
3. Within each test case, execute commands sequentially

### Variable and State Flow:
- Variables created in one command are available in subsequent commands
- File system operations affect the test's temporary directory
- Each test case starts with clean state

## Complete Reference by Line Type

### Comments (`#`)
```
# comment_text              # Standalone comment
command # trailing_comment  # Trailing comment on any line
```

### Structure (`>`)
```
> test_case_name            # Define a test case
(.. commands ..)

>@ snippet_name             # Define a reusable snippet
(.. commands ..)
```

### Shell Commands (`$`)

**Command Aliases**: You can define aliases for commands to simplify testing or provide custom paths. Edit the `COMMAND_ALIASES` dictionary at the top of `shellspec.py`:

```python
COMMAND_ALIASES = {
    "age-store.py": "../age-store.py",
    "your-command": "/path/to/executable",
}
```

Commands not found in the aliases dictionary will be executed directly as system commands.

Shell commands have two execution modes depending on whether interactive commands are present:

#### Subprocess Mode (Default)
```
$. command [args...]        # Execute command, expect success (exit 0)
$! command [args...]        # Execute command, expect failure (exit ≠ 0)
```

- Fast execution using Python's `subprocess` module
- Captures stdout and stderr separately
- Command completes before moving to next line
- Suitable for non-interactive commands

**Example:**
```
$. ls -la                   # Fast subprocess execution
?. stdout "total"           # Check captured stdout
$! cat missing.txt          # Fast failure detection
?. stderr "No such file"    # Check captured stderr
```

#### Pexpect Mode (Interactive)
```
$. command [args...]        # Start interactive command
$< "expected_text"          # Expect text from command output
$> "input_text"             # Send text to command input
$< "next_expected"          # Expect next response
```

- Slower execution using `pexpect` library (adds several seconds overhead)
- Handles interactive programs that require user input
- Stdout and stderr are combined in pexpect output
- Supports expect/send patterns for complex interactions

**Mode Selection:**
- **Subprocess mode**: Used when no `$<` or `$>` lines follow the shell command
- **Pexpect mode**: Automatically enabled when `$<` or `$>` lines are present

**Interactive Constraints:**
- `$<` and `$>` must immediately follow `$.` or `$!` (no other commands in between)
- Interactive commands cannot appear elsewhere in the file
- All `$<` and `$>` lines form one contiguous interaction sequence

**Example:**
```
$. python quiz_app.py       # Starts pexpect mode (due to $< lines below)
$< "Enter your name:"       # Wait for this prompt
$> "Alice"                  # Send this input  
$< "Hello Alice!"           # Wait for response
$< "Enter age:"             # Wait for next prompt
$> "25"                     # Send age
```

### Assertions (`?`)
```
?. target [args...]         # Assert condition is true
?! target [args...]         # Assert condition is false (negated)
```

**Complete Assertion Syntax:**
```
# Output assertions
?. stdout "text"             # stdout contains "text"
?! stdout "text"             # stdout does NOT contain "text"
?. stderr "text"             # stderr contains "text"  
?! stderr "text"             # stderr does NOT contain "text"

# Exact content matching (with content blocks)
?. stdout                    # stdout matches exactly
.. expected line 1           # Content block: must immediately follow
.. expected line 2           # Content block: preserves whitespace
?! stderr                    # stderr does NOT match exactly
.. error line 1              # Content block
.. error line 2              # Content block

# File assertions
?. file "path"               # file exists
?! file "path"               # file does not exist
?. file "path" "text"        # file contains "text"
?! file "path" "text"        # file does NOT contain "text"

# Exact file content matching (with content blocks)
?. file "path"               # file content matches exactly
.. expected line 1           # Content block: must immediately follow
.. expected line 2           # Content block: preserves whitespace
?! file "path"               # file content does NOT match exactly
.. unwanted line 1           # Content block
.. unwanted line 2           # Content block

# Variable comparisons
?. == @var "value"           # variable equals "value"
?! == @var "value"           # variable does NOT equal "value"
?. != @var1 @var2            # variables are different
?! != @var1 @var2            # variables are NOT different (i.e., same)
?. == @var1 @var2            # variables are equal
?! == @var1 @var2            # variables are NOT equal

# String operations on variables
?. startswith @var "prefix"  # variable starts with "prefix"
?! startswith @var "prefix"  # variable does NOT start with "prefix"
?. endswith @var "suffix"    # variable ends with "suffix"
?! endswith @var "suffix"    # variable does NOT end with "suffix"
?. contains @var "text"      # variable contains "text"
?! contains @var "text"      # variable does NOT contain "text"
```

### General Actions (`:`)
```
:. stdout @variable         # Store stdout in variable

:. stderr @variable         # Store stderr in variable

:. file "path" [mode]       # Create file with content
.. line 1                   # Content block: must immediately follow
.. line 2                   # Content block: preserves whitespace

:. @ snippet_name           # Invoke snippet
```


## Examples

### Learning Progression

**1. Basic Structure**
```
> My first test               # Test case
$. echo "hello"              # Shell command (expect success)
?. stdout "hello"            # Assertion (stdout contains "hello")
```

**2. Using Operators**
```
> Success and failure
$. echo "works"              # Expect success (.)
$! cat missing_file.txt      # Expect failure (!)
?. stdout "works"            # Positive assertion (.)
?! stderr "works"            # Negative assertion (!)
```

**3. Variables**
```
> Variables
$. whoami                    # Run command
:. stdout @user              # Store result in @user variable
?. == @user "alice"          # Use variable in assertion
```

**4. Content Blocks**
```
> File creation and checking
:. file test.txt             # Create file
.. Line one                  # Content block
.. Line two                  # Content block

?. file test.txt             # Check exact content
.. Line one                  # Expected content
.. Line two                  # Expected content
```

**5. Interactive Commands**
```
> Interactive program
$. python quiz.py            # Start interactive command
$< "Enter name:"             # Expect prompt
$> "Alice"                   # Send response  
$< "Hello Alice"             # Expect greeting
```

**6. Snippets**
```
>@ setup                     # Define snippet
:. file config.txt           # Commands in snippet
.. setting=value             # Content

> Test using snippet
:. @ setup                   # Invoke snippet
$. cat config.txt            # Use setup
?. stdout "setting=value"    # Verify
```

### Common Patterns

**File Testing Pattern**
```
:. file input.txt            # Create → Test → Verify
.. test data                 
$. process_file input.txt    
?. file output.txt "result"  
```

**Pipeline Pattern**
```
$. command1                  # Execute → Store → Use → Assert
:. stdout @result            
$. command2 @result          
?. stdout "expected"         
```

**Error Testing Pattern**  
```
$! failing_command           # Expect failure → Check error
?. stderr "error message"    
?! stdout "success"          
```
