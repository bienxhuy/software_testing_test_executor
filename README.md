# Test Executor

## Setup Virtual Environment

### First Time Setup

1. Create the virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:

**Windows (Git Bash/WSL):**
```bash
source venv/Scripts/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

### Daily Usage

Activate the virtual environment before working:
```bash
source venv/Scripts/activate
```

You'll see `(venv)` in your terminal prompt when active.

### Deactivate

When you're done working:
```bash
deactivate
```

## Managing Dependencies

### Save current packages:
```bash
pip freeze > requirements.txt
```

### Install from requirements:
```bash
pip install -r requirements.txt
```
