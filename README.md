<h1 align="center">
         DIAL Admin Course
    </h1>
    <p align="center">
        <p align="center">
        <a href="https://dialx.ai/">
          <img src="https://dialx.ai/logo/dialx_logo.svg" alt="About DIALX">
        </a>
    </p>
<h4 align="center">
    <a href="https://discord.gg/ukzj9U9tEe">
        <img src="https://img.shields.io/static/v1?label=DIALX%20Community%20on&message=Discord&color=blue&logo=Discord&style=flat-square" alt="Discord">
    </a>
</h4>

# DIAL Admin Course

Materials for DIAL Admin course - a comprehensive guide to administering and developing applications for the DIAL
platform.

## Table of Contents

- [Getting Started](#getting-started)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Open in IDE](#step-2-open-in-ide)
- [Running the DIAL Platform](#running-the-dial-platform)
    - [Installing Docker](#installing-docker)
    - [Starting the Platform](#starting-the-platform)
    - [Accessing DIAL Services](#accessing-dial-services)
    - [Stopping the Platform](#stopping-the-platform)
- [Running Python Applications](#running-python-applications)
    - [Installing Python](#installing-python)
    - [Setting Up the Project](#setting-up-the-project)
    - [Running the Echo App](#running-the-echo-app)
- [Troubleshooting](#troubleshooting)

---

## Getting Started

### Step 1: Clone the Repository

<details> 
<summary><b>Instructions</b></summary>

First, you need to download (clone) this repository to your computer.

#### Option A: Using Git (Recommended)

1. **Install Git** (if not already installed):

    - **Windows**: Download from [git-scm.com](https://git-scm.com/download/win) and run the installer
    - **macOS**: Open Terminal and run: `xcode-select --install`
    - **Linux (Ubuntu/Debian)**: Open Terminal and run: `sudo apt install git`

2. **Clone the repository**:

   Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:

   ```bash
   git clone https://github.com/YOUR_USERNAME/dial-admin-course.git
   cd dial-admin-course
   ```

   > **Note**: Replace `YOUR_USERNAME` with the actual repository path provided by your instructor.

#### Option B: Download as ZIP

1. Go to the repository page on GitHub
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract the ZIP file to a folder on your computer

</details>

### Step 2: Open in IDE

<details> 
<summary><b>Instructions</b></summary>

An IDE (Integrated Development Environment) makes it easier to work with code files.

#### Recommended: Visual Studio Code (VS Code)

1. **Download VS Code** from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install VS Code** by running the downloaded installer

3. **Open the project**:
    - Launch VS Code
    - Go to **File** → **Open Folder**
    - Navigate to the `dial-admin-course` folder you cloned/downloaded
    - Click **Select Folder**

4. **Install recommended extensions** (optional but helpful):
    - Python extension
    - Docker extension
    - YAML extension

   To install: Click the Extensions icon in the left sidebar (or press `Ctrl+Shift+X`) and search for each extension.

</details>

---

## Running the DIAL Platform

The DIAL platform runs in Docker containers. Docker allows you to run applications in isolated environments without
installing them directly on your computer.

### Installing Docker

<details> 
<summary><b>Instructions</b></summary>

<details> 
<summary><b>Windows</b></summary>

1. **Check system requirements**:
    - Windows 10 64-bit (Build 19041 or higher) or Windows 11
    - Enable virtualization in BIOS (usually enabled by default)

2. **Download Docker Desktop**:
    - Go to [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
    - Click **"Download for Windows"**

3. **Install Docker Desktop**:
    - Run the downloaded installer
    - Follow the installation wizard
    - **Important**: When prompted, ensure **"Use WSL 2 instead of Hyper-V"** is selected

4. **Start Docker Desktop**:
    - After installation, launch Docker Desktop from the Start menu
    - Wait for Docker to start (the whale icon in the system tray should stop animating)

5. **Verify installation**:
   Open Command Prompt or PowerShell and run:
   ```bash
   docker --version
   docker compose version
   ```

</details>

<details> 
<summary><b>macOS</b></summary>

1. **Download Docker Desktop**:
    - Go to [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
    - Click **"Download for Mac"**
    - Choose the correct version for your chip (Intel or Apple Silicon/M1/M2)

2. **Install Docker Desktop**:
    - Open the downloaded `.dmg` file
    - Drag Docker to the Applications folder
    - Launch Docker from Applications

3. **Grant permissions**:
    - When prompted, enter your password to allow Docker to install its networking components

4. **Verify installation**:
   Open Terminal and run:
   ```bash
   docker --version
   docker compose version
   ```

</details>

<details> 
<summary><b>Linux</b></summary>

1. **Update your system**:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install Docker**:
   ```bash
   # Install prerequisites
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

   # Add Docker's official GPG key
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

   # Add Docker repository
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

   # Install Docker
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
   ```

3. **Add your user to the docker group** (to run Docker without sudo):
   ```bash
   sudo usermod -aG docker $USER
   ```

   > **Important**: Log out and log back in for this change to take effect.

4. **Verify installation**:
   ```bash
   docker --version
   docker compose version
   ```

   </details>

</details>

---

### Starting the Platform

All the services are already configured in the [docker-compose.yml](/docker-compose.yml).

<details> 
<summary><b>Instructions</b></summary>

1. **Open a terminal** in the project folder:
    - **VS Code**: Go to **Terminal** → **New Terminal** (or press `` Ctrl+` ``)
    - **Or** navigate to the project folder in your system terminal

2. **Start all services**:
   ```bash
   docker compose up -d
   ```

   > **What this does**:
   > - `docker compose up` - starts all the services defined in `docker-compose.yml`
   > - `-d` - runs in "detached" mode (in the background)

3. **Wait for services to start**:

   The first time you run this command, Docker will download all required images. This may take **10-20 minutes**
   depending on your internet speed.

   You can check the status of services:
   ```bash
   docker compose ps
   ```

   All services should show as "running" or "healthy".

4. **View logs** (optional):
   ```bash
   # View all logs
   docker compose logs

   # View logs for a specific service
   docker compose logs core

   # Follow logs in real-time
   docker compose logs -f
   ```

</details>

---

### Accessing DIAL Services

Once all services are running, you can access:

| Service                | URL                                            | Username   | Password   |
|------------------------|------------------------------------------------|------------|------------|
| **DIAL Chat**          | [http://localhost:3100](http://localhost:3100) | dial       | dial       |
| **DIAL Admin Console** | [http://localhost:3102](http://localhost:3102) | dial-admin | dial       |
| **Keycloak Admin**     | [http://localhost:8900](http://localhost:8900) | admin      | admin      |
| **Grafana**            | [http://localhost:3002](http://localhost:3002) | admin      | adminadmin |

DIAL Chat users credentials:

| Service                     | Username | Password |
|-----------------------------|----------|----------|
| User with admin premissions | dial     | dial     |
| Regular user                | user     | dial     |

---

### Stopping the Platform

<details> 
<summary><b>Instructions</b></summary>

To stop all services:

```bash
docker compose down
```

To stop and remove all data (start fresh):

```bash
docker compose down -v
```

</details>

---

## Running Python Applications

Throughout the course, you will create and run Python applications that interact with the DIAL platform.

### Installing Python

<details> 
<summary><b>Windows</b></summary>

1. **Download Python**:
    - Go to [python.org/downloads](https://www.python.org/downloads/)
    - Download Python 3.10 or newer

2. **Install Python**:
    - Run the installer
    - **Important**: Check the box **"Add Python to PATH"** at the bottom of the installer
    - Click **"Install Now"**

3. **Verify installation**:
   Open Command Prompt and run:
   ```bash
   python --version
   pip --version
   ```

</details>

<details> 
<summary><b>macOS</b></summary>

1. **Install using Homebrew** (recommended):
   ```bash
   # Install Homebrew if not installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install Python
   brew install python@3.11
   ```

2. **Or download from python.org**:
    - Go to [python.org/downloads](https://www.python.org/downloads/)
    - Download and install Python 3.10 or newer

3. **Verify installation**:
   ```bash
   python3 --version
   pip3 --version
   ```

</details>

<details> 
<summary><b>Linux</b></summary>

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

Verify installation:

```bash
python3 --version
pip3 --version
```

</details>

---

### Setting Up the Project

<details> 
<summary><b>Instructions</b></summary>

1. **Open a terminal** in the project folder

2. **Create a virtual environment**:

   A virtual environment keeps project dependencies isolated from your system Python.

   **Windows**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   > You'll see `(.venv)` at the beginning of your terminal prompt when the virtual environment is active.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

</details>

---

### Running the Echo App

<details> 
<summary><b>Instructions</b></summary>

The Echo App is a simple example application that echoes back whatever you send to it.

1. **Make sure the DIAL platform is running**:
   ```bash
   docker compose ps
   ```

2. **Activate the virtual environment** (if not already active):

   **Windows**:
   ```bash
   .venv\Scripts\activate
   ```

   **macOS/Linux**:
   ```bash
   source .venv/bin/activate
   ```

3. **Run the Echo App**:
   ```bash
   python app_demo/echo_app.py
   ```

   You should see output similar to:
   ```
   INFO:     Started server process [12345]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://0.0.0.0:5022 (Press CTRL+C to quit)
   ```

4. **Test the app**:
    - Open DIAL Chat at [http://localhost:3100](http://localhost:3100)
    - Log in with username `dial` and password `dial`
    - Select the **"Echo app"** from the model selector
    - Send a message - you should see it echoed back with "Magical Echo✨" prefix

5. **Stop the app**:
   Press `Ctrl+C` in the terminal where the app is running.

</details>

---

## Platform Schema

![img](/platform-schema.png)


---


## Troubleshooting

<details> 
<summary><b>Docker Issues</b></summary>

**Problem**: `docker: command not found`

- **Solution**: Make sure Docker is installed and added to PATH. Restart your terminal after installation.

**Problem**: `Cannot connect to the Docker daemon`

- **Solution**:
    - Windows/macOS: Make sure Docker Desktop is running (check the system tray)
    - Linux: Run `sudo systemctl start docker`

**Problem**: Services fail to start or show "unhealthy"

- **Solution**:
    1. Check logs: `docker compose logs <service-name>`
    2. Try restarting: `docker compose restart`
    3. If issues persist, try a clean start: `docker compose down -v && docker compose up -d`

**Problem**: Port already in use

- **Solution**: Another application is using the required port. Either stop that application or modify the ports in
  `.env` file.

</details>

<details> 
<summary><b>Python Issues</b></summary>

### Python Issues

**Problem**: `python: command not found`

- **Solution**:
    - Windows: Reinstall Python and make sure to check "Add Python to PATH"
    - macOS/Linux: Use `python3` instead of `python`

**Problem**: `pip: command not found`

- **Solution**: Use `python -m pip` instead of `pip`, or `python3 -m pip` on macOS/Linux

**Problem**: Module not found errors

- **Solution**: Make sure your virtual environment is activated and dependencies are installed:
  ```bash
  source .venv/bin/activate  # or .venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

</details>

<details> 
<summary><b>Application Issues</b></summary>

**Problem**: Echo app can't connect to DIAL Core

- **Solution**: Make sure the DIAL platform is running (`docker compose ps`) and the Core service is healthy.

**Problem**: Can't access DIAL Chat or Admin Console

- **Solution**:
    1. Check if services are running: `docker compose ps`
    2. Wait a few minutes after starting - services need time to initialize
    3. Check logs for errors: `docker compose logs chat` or `docker compose logs admin-frontend`

</details>

