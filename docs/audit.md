# Initial scientific and numerical audit

Reviewed on 2026-09-28. Cell numbers below are zero-based JSON cell indices in
`notebooks/cstr_exploration.ipynb`. These are agent checks, pending researcher review.

## Evidence checked

| Check | Status and source |
|---|---|
| Parameter copies | Checked: all 11 parameters in cell 3 match `data/reactor_parameters.yml`. |
| Balance equations | Checked: cell 5 implements cell 0's material and energy balances. Material residual is mol/min; energy residual is J/min. |
| Reaction and cooling signs | Checked: negative `dHr` produces positive heat release. `-UA*(T-Tc)` removes heat when the reactor is warmer. |
| Temperatures | Checked: all supplied temperatures are absolute K, including the Arrhenius expression. |
| Nominal convergence | Checked in `results/baseline/execution.txt`: the single solve returned flag 1, with residual norm about 9.90e-10. Cell 7 would still print a result on failure. |
| Accepted-state criteria | Checked, cell 9: flag 1, residual norm <= 1e-6, concentration bounds, positive temperature. Explicit finite-value checks are missing. |
| Starting guesses | Checked, cell 9: 300 through 440 K in 5 K increments; concentration initialized on the material balance. This finite grid does not establish completeness. |
| Distinct states | Checked, cell 9: sorted by temperature, deduplicated within 0.01 K. Close roots near a fold could merge. |
| Sweep | Checked, cell 11: coolant 285 through 315 K in 0.5 K steps. This run covers all 61 conditions, with 145 rows. |
| Output validity | Checked: every CSV value is finite, concentration and conversion are in [0, 1], temperatures are positive, row counts match reported multiplicity, and stored residual norms meet the threshold. |
| Figure connections | Checked visually in `results/baseline/steady_state_locus.png`: no false line connects the cold branch to the hot single-state region. Cell 13 splits lines when multiplicity changes. |
| Original preservation | Checked: notebook and YAML SHA-256 hashes match the originals in Downloads. `results/baseline/manifest.json` records source and output hashes. |

## Numerical observations

At coolant temperature 300 K, the solver found:

| Temperature (K) | Concentration (mol/L) | Conversion |
|---:|---:|---:|
| 311.9589775 | 0.9547232446 | 0.04527675544 |
| 348.9249258 | 0.5192643743 | 0.4807356257 |
| 385.1305120 | 0.09276256907 | 0.9072374309 |

The first sweep row is Tc = 285 K, T = 300.5705582 K, CA = 0.9838788242 mol/L.
Three accepted states were found at 42 sampled conditions, from Tc = 290.5 to
311 K inclusive. These observations reproduce the narrative for this solver and
grid. They do not establish that all mathematical roots were found.

## Questions to resolve before trusting a refactor

- The residual norm combines different units without scaling. The threshold must
  be preserved for baseline comparisons, then assessed explicitly if changed.
- Add finite-value checks before accepting states. Reject nonfinite parameters.
- Cell 11 drops any condition with zero accepted roots; its summary can conceal
  failures. No missing condition occurred in this run.
- Cell 13 does not break lines across missing coolant samples. Temperature ranks
  are local labels, not continuation identities.
- State counts refer to the sampled range and roots found. A grid does not prove
  exact fold locations, stability, ignition, or extinction. No dynamic model was
  evaluated. The parameters describe a teaching case, not measured equipment.

## Execution limitation

The installed Jupyter stack could not start a usable kernel. The sandbox first
blocked Windows connection-file permissions; the approved outside-sandbox run
then failed in ZeroMQ with `Bad file descriptor (...epoll.cpp:100)`. A Windows
selector-event-loop retry failed in the same way.

The successful baseline uses `scripts/capture_baseline.py --plain-python` to run
every unchanged code cell, in order, in a fresh Python process. It saves the CSV,
PNG, original notebook, console transcript, version information, and hashes.
It does not verify Jupyter rich displays or a fresh notebook kernel. The original
notebook contains no IPython-only magics. A pandas warning about the installed
optional bottleneck version is retained in the transcript; execution completed.
