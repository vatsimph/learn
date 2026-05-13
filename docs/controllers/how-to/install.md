# Sector Files

The Philippines vACC utilizes EuroScope for its Air Traffic Controllers as it can host a near 1 to 1 system that the real world controllers use (TopSky).

Currently, only approved controllers may use our sector files.

The VATPHIL Updater is a desktop application that automatically downloads, installs, and keeps your sector files up to date. It handles everything from first-time installation to AIRAC cycle updates.

---

## EuroScope

The EuroScope [[Download]](https://www.euroscope.hu/wp/installation/) page can be found here.

### Prerequisites

Before installing EuroScope v3.2.4 and later, be sure to download and install the latest C++ redistributable package from Microsoft:
https://aka.ms/vs/17/release/vc_redist.x86.exe

---

## VATPHIL Updater

### Logging In

When you open the updater, you will be prompted to log in with your VATSIM account.

1. Click **Login with VATSIM** — your browser will open the VATSIM SSO page.
2. Approve the login in your browser.
3. The app will detect the login automatically and bring you to the main screen.

!!! note

     Only controllers authorised by the Philippines vACC staff will be granted access. If you see a "CID not authorised" error and you are an active controller, please contact vACC staff.

---

### Selecting an Installation Folder

Before installing, you need to point the updater to a folder where your sector files will live.

1. Click **Browse Folder**.
2. Navigate to any location on your computer (e.g. your EuroScope directory).
3. The updater will automatically create a **VATPHIL Sector** subfolder inside your chosen location.

!!! tip 

    The updater remembers your folder between sessions — you only need to do this once.

---

### Installing / Updating Sector Files

Once a folder is selected, the updater checks the remote files against your local install.

| Status           | Button shown                         | What it means                  |
| ---------------- | ------------------------------------ | ------------------------------ |
| Not installed    | **Install Update**                   | No local files found           |
| Update available | **Install Update**                   | New AIRAC available            |
| Up to date       | **Selective Repair** / **Reinstall** | Files match the latest release |

Click **Install Update** to begin. A progress bar at the bottom of the status card will track the download. The sector profile is updated automatically to match the new AIRAC cycle once the install completes.

??? info "How many MBs is the sector file?"

    Unfortunately the sector files will set you back `566.8 MB`
---

### Entering Your Controller Details

After installing, fill in the **Controller Details** panel in the left sidebar:

| Field                 | What to enter                                  |
| --------------------- | ---------------------------------------------- |
| **Name**              | Any VATSIM approved name conventions[^1]       |
| **VATSIM CID**        | Your VATSIM CID (pre-filled from VATSIM login) |
| **VATSIM Password**   | Your VATSIM network password                   |
| **Hoppie ACARS Code** | Your personal Hoppie logon code (optional)     |

Click **Apply** when done. EuroScope is ready to connect immediately.

!!! warning

     Your VATSIM password is saved locally in `config.json` next to the updater. **Do not share this file with anyone.**

??? info "Hoppie Account"

    Create an account from [Hoppie](https://www.hoppie.nl/acars/system/register.html)
---

### Selective Repair

If only specific files are missing or corrupted, use **Selective Repair** instead of a full reinstall.

1. Click **Selective Repair**.
2. A window will appear listing all remote files. Missing or outdated files are pre-checked and highlighted in red.
3. Use the search bar to filter files by name if needed.
4. Check any additional files you want to re-download, then click **Repair Selected**.

---

### Full Reinstall

**Reinstall** re-downloads every file from scratch. Use this if your installation is in an inconsistent state or you want a completely clean install.

1. Click **Reinstall** and confirm when prompted.
2. All existing files will be deleted and re-downloaded from the server.

---

### Keeping the Updater Itself Up to Date

The updater checks for a new version of itself each time you log in. If a newer version is available, you will be prompted to download and install it. The app restarts automatically once the update is applied, no manual steps required.

!!! info "**Version 0.9.2**"

    Controller Beta can be found [here](https://vats.im/ph/install)

---

## Folder Structure

### Setup/
Contains the installers for VACS, Track Audio, and vATIS. Can be deleted after installation.

### RPHI/
The main folder containing all required files for EuroScope.

#### Alias.txt
This file contains keyboard shortcuts for messages you want to type quickly during your session. To add your own shortcut, use the following format:

```
.[shortcut] [Message]
```

**Example:**
```
.yes Affirm
```

Each shortcut must begin with a period (`.`).
If you think this shortcut should be added for everyone, create a ticket with your shortcut.

#### ASR/
Contains all the `.asr` screen files for EuroScope. If you are looking for an aerodrome that isn't accessible via the `F+#` shortcut, you can find and open it manually from this folder.

#### Everything else

!!! warning

    Do not touch anything else inside the RPHI folder unless you know what you are doing. Modifying other files may break your EuroScope setup.

---

## Need Help?

If you run into any issues, create a post on [**#controller-support**](https://discord.com/channels/275064722678743042/1312782960474460242).

[^1]: A4(b) Account holders shall connect to VATSIM using only one of the following name conventions: Their real, registered name (e.g., **Joseph Smith**). Their real, registered given name, followed by the first initial of their surname (e.g., **Joseph S.**) An appropriate shortening of their given name, followed by either their surname or the first initial of their surname (e.g., **Joe Smith, Joe S**.) Their real given name (e.g., **Joseph**). An appropriate shortening of their given name (e.g., **Joe**). Their first and last initial (e.g., **J.S**.) Or their VATSIM **certificate ID** number.