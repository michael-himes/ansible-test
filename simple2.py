---
- hosts: all
  tasks:
    - name: print message
      debug:
        msg: Hello World
    - name: stall
      pause:
        seconds: 30
    - name: echo variable
      debug:
        msg: echo "{{ variable| default("default_value") }}"
