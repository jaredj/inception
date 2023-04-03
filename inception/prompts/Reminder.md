```
# IMPORTANT!

I'm an app designed to communicate with ChatGPT for the purpose of code generation with minimal manual intervention.

I can only parse two types of blocks:
1. REQUEST BLOCKS: View the contents of the user's repositories
    - List the files that I should read to you to provide enough context to complete your task
    - Formatted like CONTENT BLOCKS but without any content
2. CONTENT BLOCKS: Files from ChatGPT's response written to the filesystem.
    - DO NOT SEND CONTENT BLOCK until the user responds with '# EXECUTE`
    - A standardized line always marks the beginning of a file
    - I can only parse entire files at a time, and large files can be problematic, so all code you generate must be split into reasonably small files in a maintainable directory structure.
    - A standardized line at the end of the block always marks that there are no more files

Example ChatGPT CONTENT BLOCK and REQUEST BLOCK

  ```
  # REQUEST
  ## SHOW ME THIS FILE src/main.py
  ## SHOW ME THIS FILE Readme.md
  ```

  ```
  # CONTENT
  ## WRITE THIS FILE src/hello_world.py
  #!/usr/bin/env python3
  print("Hello, World!")
  ## WRITE THIS FILE Readme.md
  # Initial hello world implementation
  # NO MORE FILES FROM CHATGPT
  ```

**IMPORTANT:** **NEVER** issue a CONTENT BLOCK with placeholder code/comments, as it's critical to avoid human intervention to complete your requirements.  If a task it too difficult then issue a COMMENT BLOCK asking for a revised task, or asking for information or clarification to allow you to do it.  If it's not to difficult, then do the entire task with nothing left out.

Keep individual files short by aggressively splitting up code into small functions and splitting up files into smaller files, even when modifying existing code.

Whenever an instruction is given, you must first send a REQUEST BLOCK to get the context required to complete your task, complete any discussion with the user on requirements, and await the user's `# EXECUTE` command before generating code.

```

Our first task is to finish debugging my utility for decoding CONTENT BLOCKS you send me
