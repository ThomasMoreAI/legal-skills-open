# Assets

Place your `demo.gif` here after recording with `record_demo.sh`.

The README references: `assets/demo.gif`

## How to generate the GIF

```bash
# 1. Install tools
brew install asciinema        # macOS
pip install agg               # GIF converter

# 2. Record and convert
chmod +x record_demo.sh demo_script.sh
./record_demo.sh

# 3. Move to this folder
mv demo.gif assets/
```
