import json
import sys
from pathlib import Path

FICHIER = Path("taches.json")

def charger():
    return json.loads(FICHIER.read_text()) if FICHIER.exists() else []

def sauvegarder(taches):
    FICHIER.write_text(json.dumps(taches, ensure_ascii=False, indent=2))

def main():
    taches = charger()
    if len(sys.argv) < 2:
        print("Usage : python todo.py [ajouter <texte> | liste | fait <numéro>]")
        return
    cmd = sys.argv[1]
    if cmd == "ajouter":
        taches.append({"texte": " ".join(sys.argv[2:]), "fait": False})
        sauvegarder(taches)
    elif cmd == "liste":
        for i, t in enumerate(taches, 1):
            print(f"{i}. [{'x' if t['fait'] else ' '}] {t['texte']}")
    elif cmd == "fait":
        taches[int(sys.argv[2]) - 1]["fait"] = True
        sauvegarder(taches)

if __name__ == "__main__":
    main()
