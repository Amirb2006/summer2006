# Summer EE Engineering Portfolio

This repository is my learning portfolio for electrical engineering, with a focus on signal processing, embedded systems, control engineering, and scientific Python. It is organized to show my progression from Python fundamentals toward applied engineering problems, data analysis, and practical modeling.

The examples here are intentionally hands-on and educational. They are designed to reflect the way I learn by building small, readable engineering experiments around real concepts such as waveforms, filtering, measurement handling, and basic numerical methods.

## Repository Structure

- foundation/ — Python basics, functions, file handling, exception handling, and simple data structures
- signal_processing/ — NumPy exercises, waveform generation, plotting, filtering, and telemetry data
- embedded_systems/ — STM32-focused notes and future firmware work
- matlab/ — MATLAB learning materials and engineering examples

## Project Highlights

| File | Engineering concept |
| --- | --- |
| foundation/functions.py | Power and RMS calculations |
| foundation/exception_handling.py | Safe handling of numerical edge cases |
| signal_processing/dc_power_supply_simulation.py | Basic DC supply and signal behavior |
| signal_processing/moving_average_filter.py | Noise reduction and digital filtering |
| signal_processing/telemetry.csv | Example measurement data for analysis |
| embedded_systems/README.md | STM32 learning context |

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\\Scripts\\activate       # Windows
pip install -r requirements.txt
```

After setup, run any example directly with Python. For example:

```bash
python signal_processing/moving_average_filter.py
```

This portfolio is intentionally practical and educational. The goal is to demonstrate clear engineering thinking, hands-on experimentation, and steady growth across core EE topics.

