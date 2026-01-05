# FFmpeg Installation Guide

FFmpeg is a powerful multimedia framework used for processing audio and video files. It is required for audio processing
in this project. Follow the instructions below to install FFmpeg on your system.

## Windows

1. Go to this link: https://www.gyan.dev/ffmpeg/builds/#release-builds.
2. Download the `ffmpeg-release-essentials.zip` from release builds section.
3. Extract the downloaded zip file.
4. Rename the folder to `ffmpeg`
5. Move it to the location: `C:\ffmpeg`
6. Press **Win + R** → type `sysdm.cpl` → Press **Enter**
7. Go to **Advanced** tab → Click on **Environment Variables**
8. Under **System variables**, select **Path**
9. Click **Edit** → **New**
10. Add: `C:\ffmpeg\bin`
11. Click on button **OK** → **OK** → **OK**
12. After the installation is complete, verify it by running:
   ```bash
   ffmpeg -version
   ```

## macOS
1. Open Terminal.
2. Install Homebrew if you haven't already by running:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Once Homebrew is installed, run the following command to install FFmpeg:
   ```bash
   brew install ffmpeg
   ```
4. After the installation is complete, verify it by running:
   ```bash
   ffmpeg -version
   ```
## Linux (Ubuntu/Debian)
1. Open Terminal.
2. Update the package list:
   ```bash
   sudo apt update
   ```
3. 
    - For Dabian/Ubuntu-based systems, run:
        ```bash
        sudo apt install ffmpeg
        ```
    - Fedora-based systems, use:
        ```bash
        sudo dnf install ffmpeg
        ```
    - Arch Linux-based systems, use:
        ```bash
        sudo pacman -S ffmpeg
        ```
4. After the installation is complete, verify it by running:
   ```bash
   ffmpeg -version
   ```