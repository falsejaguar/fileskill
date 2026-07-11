import subprocess
import tempfile
import os

def run_python(code, safe_mode=True):
    if safe_mode and ("import" in code or "open(" in code):
        return "safe_mode prevents imports and file I/O"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp.flush()
        try:
            result = subprocess.run(
                ["python3", tmp.name],
                capture_output=True,
                text=True
            )
            return result.stdout + result.stderr
        finally:
            os.unlink(tmp.name)
