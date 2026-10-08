# oobindiff: Sovereign BINARY DIFFER

<div align="center">

```
================================================================================
                                oobindiff
               Sovereign openOODA BINARY DIFFER
================================================================================
```

**Sovereign BINARY DIFFER**  
*Structural binary differ identifying patch blocks and byte sequence displacements.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oobindiff/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oobindiff-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oobindiff/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oobindiff/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oobindiff-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oobindiff/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oobindiff [options] <FILE_A> <FILE_B>

Capability-bounded binary file comparator and differential hunk analyzer.

Options:
  -h, --help               display this help and exit
  -v, --version            output version information and exit
  -s, --summary            display aggregate similarity and metrics only
  -u, --hunks              display contiguous mutated difference hunks
  -o, --offset <N>         start offset for detailed byte comparisons [default: 0]
  -n, --limit <N>          maximum difference rows to display [default: 100]
      --json               output telemetry as formatted JSON
      --mcp                run as Model Context Protocol stdio server
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oobindiff` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `bindiff_compare`: Compare two files and report match metrics, similarity percentage, and mutation hunks.
* `bindiff_hunks`: List contiguous mutated byte ranges and offsets between binary targets.
* `bindiff_similarity`: Fast computation of matching byte counts, mismatches, and percentage similarity.
* `bindiff_stats`: Query oobindiff differential engine specifications and capabilities.

```bash
oobindiff --mcp
```

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict comparison bounds, offset validation, and hunk clamping.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
