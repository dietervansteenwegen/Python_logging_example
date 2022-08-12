# Basic structure for a custom logging configuration:

## What
- Config stored in separate YAML file.
- Examples of multiple loggers, formatters and handlers.
- Custom formatter that returns time with milliseconds but __limited to first 3 digits__.

## Configuration as-is
### Streamhandler 
- Writes to `sys.stdout`. 
- Logging level set to `WARNING`
- Format `%(asctime)s|%(levelname)-8.8s|%(module)-15.15s|%(lineno)-0.3d|%(funcName)-20.20s |%(message)s|`
- Result: 
> `12/08/2022 15:13:21|WARNING |usage          |017|<module>             |MSG299: This is a warning, so also goes to stdout.|`

### Rotating file handler
- Writes to `warnings.log`.
- File size set to 500kB to be able to copy files over limited connections.
- 10 files max.
- Logging level set to `DEBUG`.
- Custom formatter `MilliSecondsFormatter` formats time to include first three digits of milliseconds.
- Format `%(asctime)s|%(levelname)-8.8s|%(module)-15.15s|%(lineno)-0.3d|%(funcName)-20.20s |%(message)s|`
- Result: 
> `12/08/2022 15:13:21.681|WARNING |usage          |017|<module>             |MSG299: This is a warning, so also goes to stdout.|`
