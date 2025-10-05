# fix_docs.py
import os
import re

# --- Configuration ---
# The main directory containing your markdown documentation.
DOCS_DIRECTORY = 'APITopics'

def fix_code_blocks(content: str) -> str:
    """
    Finds <script>...</script> blocks and replaces them with
    Markdown fenced code blocks for JavaScript.
    """
    def replace_with_fence(match):
        # Extract the code inside the <script> tag.
        # .strip() removes leading/trailing whitespace.
        inner_code = match.group(1).strip()
        # Return the code formatted in a JS code block.
        return f"```js\n{inner_code}\n```"

    # A regular expression to find content within <script> tags.
    # re.DOTALL allows '.' to match newlines.
    # re.IGNORECASE makes the search case-insensitive (e.g., <SCRIPT>).
    script_pattern = re.compile(r'<script>(.*?)</script>', re.DOTALL | re.IGNORECASE)
    
    return script_pattern.sub(replace_with_fence, content)

def fix_image_paths(content: str) -> str:
    """
    Finds relative Docusaurus image paths like ./img/... and converts
    them to absolute paths /img/...
    """
    # Regex to find Markdown images linking to the './img/' folder.
    # Group 1: Alt text
    # Group 2: The rest of the image path after './img/'
    image_pattern = re.compile(r'!\[(.*?)\]\(\./img/(.*?)\)')
    
    # Replace with a format using an absolute path.
    # \1 and \2 are backreferences to the captured groups.
    return image_pattern.sub(r'![\1](/img/\2)', content)

def process_markdown_file(file_path: str) -> bool:
    """
    Reads a file, applies all fixes, and writes it back if changes were made.
    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Apply all the fixing functions
        content = original_content
        content = fix_code_blocks(content)
        content = fix_image_paths(content)

        # Only write to the file if the content has actually changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ FIXED: {file_path}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"❌ ERROR processing {file_path}: {e}")
        return False

def main():
    """
    Main function to walk through the docs directory and process files.
    """
    print(f"🚀 Starting scan in directory: '{DOCS_DIRECTORY}'...")
    
    if not os.path.isdir(DOCS_DIRECTORY):
        print(f"Error: Directory '{DOCS_DIRECTORY}' not found. Please run this script from your project's root folder.")
        return

    fixed_files_count = 0
    total_files_scanned = 0

    # os.walk recursively scans the directory
    for root, _, files in os.walk(DOCS_DIRECTORY):
        for file in files:
            # Process only .md and .mdx files
            if file.endswith(('.md', '.mdx')):
                total_files_scanned += 1
                file_path = os.path.join(root, file)
                if process_markdown_file(file_path):
                    fixed_files_count += 1

    print("\n---")
    print("✨ Scan Complete! ✨")
    print(f"Scanned: {total_files_scanned} markdown files.")
    print(f"Fixed:   {fixed_files_count} files.")
    print("\n⚠️ IMPORTANT: Please review the changes with 'git diff' or a similar tool before committing.")

if __name__ == '__main__':
    main()