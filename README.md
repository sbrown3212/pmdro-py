# PMDRO - CLI Pomodoro Timer

## TODO

- [ ] Add notification to 'run_timer()' function.
- [ ] Create pause command.
- [ ] Implement threads (to be able to run 'pause' command).

## Implement Later

- [ ] User config
- [ ] Processes (for persistent timer to run in the background)

## Things to talk about

### Difficulties

- not knowing before hand that certain features would not work.
  - `Click`: not allowing one command `option` to behave as a flag with no argument, but behave as an argument if a value is provided.
  - Persistence:
    - I wanted persistence, so a background process seemed to be the best option.
    - But processes can't prompt the user for input, so prompting to start the break timer was not an option.
- Timer class:
  - At first I attempted to have timer state in a class.
  - But then I found that other `click` commands would not be aware of this current instance.
  - So I decided to write state to a file instead.
- Over engineering before getting a basic timer to work.

### Simple loop vs Threads vs Processes

- Simple loop
  - Pros:
    - simple
  - Cons:
    - hijacks the terminal (unable to pause timer)
    - does not persist if terminal is closed
- Threading
  - Pros:
    - Allows for user input while timer is running (allows for other commands).
  - Cons:
    - A bit more complicated
    - still does not persist if terminal is closed
- Background Process
  - Pros:
    - Persists if terminal is closed
  - Cons:
    - Most complicated option
    - Background processes can't prompt user for input
    - Might not be able to do progress bar ???
