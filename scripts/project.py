import os

def generate_project_json(output_dir):
    content = """{
  "name": "ConvertedGame",
  "tree": {
    "$className": "DataModel",

    "ServerScriptService": {
      "$path": "src/ServerScriptService"
    },

    "ReplicatedStorage": {
      "$path": "src/ReplicatedStorage"
    },

    "StarterPlayer": {
      "StarterPlayerScripts": {
        "$path": "src/StarterPlayer/StarterPlayerScripts"
      }
    },

    "ServerStorage": {
      "$path": "src/ServerStorage"
    },

    "StarterGui": {
      "$path": "src/StarterGui"
    }
  }
}
"""
    path = os.path.join(output_dir, "default.project.json")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
