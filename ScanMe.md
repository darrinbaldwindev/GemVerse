# ScanMe

Use this file as the first reference point for assistants working in this Space.

## Trigger phrase

If the user says **"do scanme"**, assistants should treat that as an instruction to read this file first and then scan the Space files for the latest relevant context.

## Always-scan rule

Assistants should scan the files in the Space at the start of every new task, every resumed session, and every project-specific request.
This is the default behavior, not an optional step.

## Instruction to all assistants

Before starting any project-specific task, scan the files available in this Space and use the current Space files as the latest assistant-readable source of truth.

## Required behavior

- Check the files in the Space before assuming context.
- Prefer files in the Space over any older file names mentioned in past chat messages.
- If multiple similar files exist, prefer the file with versioning and time in the name or the file with the most current version, date, and time inside the file.
- Treat the most recent uploaded Space file as the current assistant-readable version.
- Read the relevant workflow and project-context files before making project-specific recommendations.
- If a needed file is not present in the Space, ask for the minimum required file.

## File priority order

Use this order when deciding what to read:

1. `ScanMe.md`
2. `SESSION-LOG.md`
3. `Assistant Workflow Template Global with Versioning and Time.md`
4. `Assistant Workflow Template with Versioning and Time.md`
5. `Shared Project Context Template with Versioning and Time.md`
6. Any project-specific shared context file uploaded later

## How to determine the latest file

When more than one relevant file exists:
- Check `Current version`
- Check `Last updated date`
- Check `Last updated time`
- Prefer the newest matching file in the Space

## Working rule

The Space is the live assistant workspace.
If a file exists in the Space, assistants should assume it is the latest file available to them unless the user says otherwise.

## Default instruction example

When the user says "do scanme", "check the files", or references `ScanMe.md`, assistants should interpret that as:

```text
Read ScanMe.md first.
Scan the Space files.
Use the current versioned Space files as the latest available context.
Check version, last updated date, and last updated time where relevant.
If a project-specific shared context file exists, read that before making project-specific recommendations.
```

## User note

Keep this file in the Space so assistants can be directed to it at the start of a task.
