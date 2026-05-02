from pathlib import Path

def show_tree(path, level=0):
    indent = "    " * level
    
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}[DIR]  {item.name}")
            show_tree(item, level + 1)
        else:
            print(f"{indent}[FILE] {item.name}")


current_path = Path.cwd()

print(f"\nDirectory Structure of: {current_path}\n")
show_tree(current_path)