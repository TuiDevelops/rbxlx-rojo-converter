import os

from parser import parse_rbxlx
from emitter import emit_script
from project import generate_project_json


ROOT_SERVICES = {
    "ServerScriptService",
    "ReplicatedStorage",
    "StarterPlayer",
    "StarterGui",
}


def convert_rbxlx(rbxlx_path, output_dir, log):
    root_items = parse_rbxlx(rbxlx_path)

    src_root = os.path.join(output_dir, "src")
    os.makedirs(src_root, exist_ok=True)

    converted = 0

    def walk(node, path_stack):
        nonlocal converted

        class_name = node["class"]
        name = node["name"]
        source = node["source"]

        # Serviço raiz
        if class_name in ROOT_SERVICES:
            path_stack = [class_name]

        # Script
        if node["is_script"]:
            file_path = emit_script(
                src_root,
                path_stack,
                name,
                class_name,
                source
            )
            log(f"✔ Script: {file_path}")
            converted += 1

        for child in node["children"]:
            new_stack = path_stack.copy()
            if class_name not in ROOT_SERVICES:
                new_stack.append(name)
            walk(child, new_stack)

    for item in root_items:
        walk(item, [])

    generate_project_json(output_dir)

    log("")
    log(f"✅ Conversão finalizada — {converted} scripts extraídos.")
