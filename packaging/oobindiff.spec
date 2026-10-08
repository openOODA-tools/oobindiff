Name:           oobindiff
Version:        0.2.0
Release:        1%{?dist}
Summary:        Structural binary differ identifying patch blocks and byte sequence displacements.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobindiff
Source0:        oobindiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobindiff is a sovereign, capability-bounded BINARY DIFFER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobindiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobindiff-uninstall

%files
/usr/bin/oobindiff
/usr/bin/oobindiff-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA binary differ with dual CLI/MCP interface
