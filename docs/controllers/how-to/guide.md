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

!!! info "**Updater**"

    VATPHIL Updater can be found [here](https://vats.im/ph/install)

---

# Folder Guide

This guide explains the folders you actually use as a controller. In normal use you only open one profile, and everything else loads by itself. You do not need to touch most files.

## The Main Folder

This is the top folder you point EuroScope at. The important items here are the profiles, which end in `.prf`.

### Profiles (.prf)

A profile is the single file you open to start controlling. Opening it loads the correct map, screens, settings, and plugins for that role. Pick the profile that matches the position you are signing on as:

1. **Manila ACC** for the en route centre.
2. **The TMA profiles** (Bacolod, Bicol, Clark, Davao, Kalibo, Laoag, Mactan, Manila, Puerto Princesa, Tambler) for those approach areas.
3. **FSS** for the regional Flight Service (radio) aerodromes.
4. **Custom** for a blank starting point.

### .sct, .ese, .rwy

These hold the map and the aeronautical data such as fixes, airways, runways, and airspace. You never open these directly. Your profile loads them for you. Just keep them in this folder and keep them up to date.

### vATIS Profile (.json)

This is the ATIS setup. You import it into the vATIS app, not into EuroScope.

## The RPHI Folder

Everything the profiles rely on lives inside `RPHI`. The folder you will care about most is `ASR`, and occasionally `Settings`.

### ASR (your screens)

An ASR is a saved screen layout: the map detail, the ranges, and the label style you see on screen. They are grouped so you can find the right one fast:

1. **A Luzon, B Visayas, C Mindanao** hold the ground, tower, and approach screens for each region group.
2. **D FSS** holds the Flight Service aerodrome screens, one per field.
3. The loose screens in the ASR folder (Manila Control and similar) are the centre screens.

While connected you switch between screens using the number fast keys or the open screen menu. You only edit these if you are building a layout, or making a custom version for yourself.

### Settings

This holds the colours, label styles, lists, and the login profiles that decide which positions you can connect as. It is already configured for you.

### Plugins

These are the tools that add features on top of EuroScope, such as TopSky, the ground radar, CDM, the AFV voice bridge, bookings, and the direction finder. They load automatically with your profile.

### Sounds, Alias, ICAO, NavData

Support data that runs in the background. Sounds are the alert tones. Alias holds the chat command shortcuts you can type while connected. ICAO and NavData hold the aircraft, airline, airport, and airway reference data used for flight plans and the map. You do not need to open any of these.

## Need Help?

If you run into any issues, create a post on [**#controller-support**](https://discord.com/channels/275064722678743042/1312782960474460242).

[^1]: A4(b) Account holders shall connect to VATSIM using only one of the following name conventions: Their real, registered name (e.g., **Joseph Smith**). Their real, registered given name, followed by the first initial of their surname (e.g., **Joseph S.**) An appropriate shortening of their given name, followed by either their surname or the first initial of their surname (e.g., **Joe Smith, Joe S**.) Their real given name (e.g., **Joseph**). An appropriate shortening of their given name (e.g., **Joe**). Their first and last initial (e.g., **J.S**.) Or their VATSIM **certificate ID** number.
