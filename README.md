# polymetals
Custom Polybar script that displays live precious metal futures prices (Silver, Gold, Platinum, Palladium, and/or Copper) sourced from Yahoo Finance.

## Requirements
* **Python 3.6+**
* **[yahoo_fin](https://pypi.org/project/yahoo-fin/)** — fetches live futures prices from Yahoo Finance. Install with:
  ```
  pip install yahoo_fin
  ```
  > **Note:** `yahoo_fin` depends on `requests_html` and `pandas` as transitive dependencies; these are installed automatically. `argparse` is part of the Python standard library and does not need to be installed separately.

## Flags
| Flag | Long form | Description |
|------|-----------|-------------|
| `-s` | `--silver`    | Silver price (USD per troy oz) |
| `-g` | `--gold`      | Gold price (USD per troy oz) |
| `-p` | `--platinum`  | Platinum price (USD per troy oz) |
| `-a` | `--palladium` | Palladium price (USD per troy oz) |
| `-c` | `--copper`    | Copper price (USD per lb) |

## Polybar Module Example
```ini
[module/polymetals]
type = custom/script
; Combine any flags: -s -g -p -a -c
exec = ~/.config/polybar/scripts/polymetals/polymetals.py -a -c -p
interval = 60
label = %output%
```

## Example Output
![polymetals](screenshots/example.png)

```
Pd: $1063.2/oz | Cu: $4.1/lb | Pt: $990.5/oz
```

## How to Use
1. Install the required Python module:
   ```
   pip install yahoo_fin
   # or, using the provided requirements file:
   pip install -r requirements.txt
   ```
2. Copy `polymetals.py` to your Polybar scripts folder (e.g. `~/.config/polybar/scripts/polymetals/`).
3. Make the script executable:
   ```
   chmod +x ~/.config/polybar/scripts/polymetals/polymetals.py
   ```
4. Add the module block shown above to your Polybar config, adjusting the `exec` path and flags as needed.
5. Reload Polybar.

## Troubleshooting
* **Prices show `N/A`** — the script could not reach Yahoo Finance. Check your internet connection or whether the `yahoo_fin` API is currently broken (Yahoo Finance occasionally changes their endpoints).
* **`ModuleNotFoundError: No module named 'yahoo_fin'`** — run `pip install yahoo_fin` (or `pip3 install yahoo_fin` depending on your environment).
* **Script is not executable** — run `chmod +x polymetals.py`.
