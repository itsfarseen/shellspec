import os
import subprocess

# List of spec files in the examples directory
spec_files = [
    "calculator_spec.txt",
    "file_processor_spec.txt",
    "interactive_calculator_spec.txt",
]

# Template for the tape file
tape_template = """Set Shell fish
Set FontSize 16
Set Width 1200
Set Height 800
Set Padding 0

Sleep 500ms
Type "../shellspec.py ../examples/{spec_file} --verbose"
Sleep 500ms
Enter
Sleep 20s
"""

temp_tape_file = ".temp.tape"

for spec_file in spec_files:
    # Create the tape file content
    tape_content = tape_template.format(spec_file=spec_file)

    # Write the temporary tape file
    with open(temp_tape_file, "w") as f:
        f.write(tape_content)

    # Generate the gif in the current folder (screencasts)
    gif_file_name = f"{spec_file.replace('_spec.txt', '.gif')}"
    command = f"vhs {temp_tape_file} -o {gif_file_name}"
    print(f"Running: {command}")
    subprocess.run(command, shell=True)

# Clean up the temporary tape file
if os.path.exists(temp_tape_file):
    os.remove(temp_tape_file)

print("Done.")
