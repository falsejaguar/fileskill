import os
import shutil

ROOT = "/main"

def full(path):
    return os.path.join(ROOT, path.lstrip("/"))

def fs_read(path):
    with open(full(path), "r") as f:
        return f.read()

def fs_write(path, content, safe_mode=True):
    p = full(path)
    if safe_mode and os.path.exists(p):
        return "safe_mode prevents overwriting existing file"
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(content)
    return "ok"

def fs_delete(path, safe_mode=True):
    p = full(path)
    if safe_mode:
        return "safe_mode prevents deletion"
    os.remove(p)
    return "ok"

def fs_list(path):
    return os.listdir(full(path))

def fs_mkdir(path):
    os.makedirs(full(path), exist_ok=True)
    return "ok"

def fs_rmdir(path, safe_mode=True):
    if safe_mode:
        return "safe_mode prevents directory removal"
    shutil.rmtree(full(path))
    return "ok"
