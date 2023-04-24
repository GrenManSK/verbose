# Verbose

## get_logger(strict=True)

- strict - If true then raise an exception if you're try to go lower than level 0

## Subfunctions

- text: str - Message to display
- end: str - Message to display at end of string
- toprint: bool - Set to false if you want to just get value from function it will not print anything, if set to true then if will also print and return value
- where: after | before | inbetween - Decide where message will be printed after altered level or before

### .stay(text: str = '', end: str = '\n', toprint: bool = True)

- Retains the current level and prints the message

### .next(self, text: str = '', end: str = '\n', by: int = 1, toprint: bool = True, where: after | before | inbetween = verbose.after)

- Add 'by' to current level and print message in altered level

### .prev(self, text: str = '', end: str = '\n', by: int = 1, toprint: bool = True, where: after | before | inbetween = verbose.after)

- Remove 'by' from current level and print message in altered level
  