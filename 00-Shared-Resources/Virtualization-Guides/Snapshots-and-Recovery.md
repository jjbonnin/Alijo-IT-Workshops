# VM Snapshots & Recovery Guide
**Alijó IT Workshops | Shared Virtualization Reference**

## 1. Why Use Snapshots?
Snapshots capture the exact state of a virtual machine (disk, memory, and settings) at a specific point in time. They allow instructors and students to recover a broken system in seconds without reinstalling the operating system.

## 2. Creating the Workshop Baseline (Instructor Pre-Lab)
Before students touch the VM, create a clean reference state:
1. Boot the VM, log in, and verify that networking, DNS, and required lab files are working properly.
2. Power off the VM cleanly (`sudo poweroff`).
3. Open **Oracle VM VirtualBox Manager**, select the VM, and click the **Snapshots** menu icon (top right of the VM panel).
4. Click **Take** (camera icon).
5. Name the snapshot exactly: `BASELINE – BEFORE WORKSHOP`
6. Add a brief description (e.g., *Clean OS state with network verified*) and click **OK**.

## 3. Restoring a VM to Baseline (Recovery Procedure)
Use this procedure between student groups, before a surprise challenge, or if a VM becomes unrecoverable:
1. Close the running VM window and select **Power off the machine**.
2. In **VirtualBox Manager** → **Snapshots**, select `BASELINE – BEFORE WORKSHOP`.
3. Click **Restore** (arrow icon).
4. **Uncheck** *"Create a snapshot of the current machine state"* (unless you need to save broken evidence for grading) and click **Restore**.
5. Start the VM normally.
