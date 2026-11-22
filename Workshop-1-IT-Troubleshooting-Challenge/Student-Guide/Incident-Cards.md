# Incident Cards — Workshop 1

Your team will be assigned incidents from this list during the main solving round. The surprise incident (Incident 06) will be handed out separately later in the workshop.

---

## INCIDENT 01 – INCORRECT IP CONFIGURATION

**Reported symptoms:** A workstation cannot reach other devices on the local network. The network icon may show a connection, but the assigned IPv4 configuration appears incorrect or incomplete.

**Your tasks:**
1. Inspect interfaces and IP settings.
2. Check the routing table.
3. Compare the configuration with the lab network information supplied by the teacher.
4. Identify the incorrect or missing setting.
5. Apply the approved correction or request a VM network reset.
6. Verify local connectivity and record the evidence.

**Useful commands:**
`ip address`
`ip route`
`ping -c 4 <LAB_GATEWAY>`

> **Safety note:** Do not invent an IP address or change the school network. Use only the addressing details provided by the teacher.

---

## INCIDENT 02 – DNS RESOLUTION FAILURE

**Reported symptoms:** The VM appears to have network connectivity, but websites cannot be opened by domain name. A connection test to a known IP address may succeed while a domain lookup fails.

**Your tasks:**
1. Test connectivity to a known IP address.
2. Test name resolution for a domain.
3. Inspect the VM's DNS configuration.
4. Identify whether the issue is DNS-specific.
5. Apply the teacher-approved DNS correction or restore the network profile.
6. Verify name resolution and explain the difference between IP connectivity and DNS.

**Useful commands:**
`ping -c 4 1.1.1.1`
`getent hosts example.com`
`resolvectl status`

> **Safety note:** Do not change the physical router or school DNS infrastructure. Make changes only inside the disposable VM and with teacher approval.

---

## INCIDENT 03 – STOPPED SYSTEM SERVICE

**Reported symptoms:** A required service is not responding. The service may be inactive, failed, or unable to start. The team must identify its state before attempting a restart.

**Your tasks:**
1. Identify the service name provided by the teacher.
2. Inspect its status and recent logs.
3. Determine whether it is stopped or has failed.
4. With teacher approval, start or restart the service.
5. Check the service status again and test the related function.
6. Record the relevant status output.

**Useful commands:**
`systemctl status <SERVICE_NAME>`
`journalctl -u <SERVICE_NAME> -n 30 --no-pager`

> **Safety note:** Do not disable security services or change services unrelated to the task.

---

## INCIDENT 04 – INCORRECT FILE PERMISSIONS

**Reported symptoms:** A user cannot read or execute a file in the lab directory. The file exists, but its permissions or ownership may not allow the required operation.

**Your tasks:**
1. Confirm the file path and current user.
2. Inspect file and directory permissions.
3. Identify the minimum permission required.
4. Propose the safest correction and obtain teacher approval.
5. Apply the minimum necessary change.
6. Test access as the intended user and record before/after permissions.

**Useful commands:**
`whoami`
`ls -l <FILE_PATH>`
`ls -ld <DIRECTORY_PATH>`

> **Safety note:** Never use `chmod 777` as a shortcut. Do not change permissions on system directories or files outside the prepared lab folder.

---

## INCIDENT 05 – APPLICATION DOES NOT START

**Reported symptoms:** A supplied application or script does not start as expected. It may show an error, close immediately, or fail to launch.

**Your tasks:**
1. Reproduce the problem and record the exact error.
2. Check whether the file exists and whether it is executable.
3. Check the process and relevant logs.
4. Identify a likely cause before changing anything.
5. Apply the teacher-approved fix.
6. Launch the application again and verify the expected behaviour.

**Useful commands:**
`ls -l <APPLICATION_PATH>`
`file <APPLICATION_PATH>`
`ps aux`
`journalctl -n 30 --no-pager`

> **Safety note:** Do not install unknown software or run downloaded scripts. Use only the application supplied in the lab.

---

## INCIDENT 06 – SURPRISE INCIDENT (CONNECTIVITY LOST AFTER A CHANGE)

**Scenario:** A VM that was working earlier can no longer reach the lab gateway or an external IP address. The team has inherited the machine after a configuration change. The cause is not stated.

**Your tasks:**
1. Describe exactly what is failing and what still works.
2. Check the interface state, IP address, and routing table.
3. Test the gateway before testing an external destination.
4. Compare the current configuration with the team's initial baseline.
5. Identify the most likely cause and support it with evidence.
6. Restore the approved configuration, then repeat the tests.
7. Document the change that caused the fault, if the evidence allows you to identify it.

**Success criteria:** The team follows a logical diagnostic sequence, avoids random changes, restores connectivity, and provides evidence.
